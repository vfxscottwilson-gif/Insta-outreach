// Run: node --test "F:\Github Repos\projects\database\install\backup.test.mjs"
import test from 'node:test'
import assert from 'node:assert/strict'
import { createServer } from 'node:http'
import { execFileSync } from 'node:child_process'
import { mkdtempSync, rmSync, writeFileSync, readdirSync, existsSync } from 'node:fs'
import { randomBytes } from 'node:crypto'
import { tmpdir } from 'node:os'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { decrypt, encrypt, fetchBackup, fsStore, putBackup, restoreBackup, rotate, splitParts, stamp, supabaseStore } from './backup-lib.mjs'

const here = dirname(fileURLToPath(import.meta.url))
const tmp = () => mkdtempSync(join(tmpdir(), 'dashbk-test-'))
const key = randomBytes(32)
const name = (i) => `dash-202611${String(i).padStart(2, '0')}-030000.db.gz.enc`

test('encrypt/decrypt round trip', () => {
  const plain = randomBytes(5000)
  const blob = encrypt(plain, key)
  assert.equal(blob.subarray(0, 8).toString(), 'DASHBK01')
  assert.equal(blob.length, 8 + 12 + plain.length + 16)
  assert.deepEqual(decrypt(blob, key), plain)
})

test('wrong key fails', () => {
  assert.throws(() => decrypt(encrypt(Buffer.from('secret'), key), randomBytes(32)), /wrong key/)
})

test('tampered file fails (header, IV, ciphertext, tag, truncation)', () => {
  const blob = encrypt(randomBytes(500), key)
  for (const pos of [2, 10, 100, blob.length - 3]) {
    const bad = Buffer.from(blob)
    bad[pos] ^= 1
    assert.throws(() => decrypt(bad, key), /bad header|wrong key/, `byte ${pos}`)
  }
  assert.throws(() => decrypt(blob.subarray(0, blob.length - 1), key), /wrong key/)
  assert.throws(() => decrypt(Buffer.alloc(10), key), /bad header/)
})

test('rotation keeps the newest 14 (with parts), never touches other files', async () => {
  const dir = tmp()
  try {
    const s = fsStore(dir)
    for (let i = 1; i <= 20; i++) await putBackup(s, name(i), randomBytes(300), i === 2 ? 100 : Infinity) // backup 2 is split in 3 parts
    writeFileSync(join(dir, 'backup.log'), 'x'); writeFileSync(join(dir, 'notes.enc'), 'x'); writeFileSync(join(dir, '.gitignore'), '*')
    assert.equal(await rotate(s, 14), 14)
    const left = readdirSync(dir).filter((f) => f.startsWith('dash-')).sort()
    assert.equal(left.length, 14)
    assert.equal(left[0], name(7))
    assert.equal(left.at(-1), name(20))
    assert.ok(!readdirSync(dir).some((f) => f.includes('.part')), 'parts of the deleted backup are gone')
    for (const f of ['backup.log', 'notes.enc', '.gitignore']) assert.ok(existsSync(join(dir, f)), f)
  } finally { rmSync(dir, { recursive: true, force: true }) }
})

test('split into small parts and reassemble; missing part is detected', async () => {
  const dir = tmp()
  try {
    const s = fsStore(dir)
    const enc = encrypt(randomBytes(10000), key)
    assert.equal(splitParts(enc, 3000).length, 4)
    assert.deepEqual(await putBackup(s, name(1), enc, 3000), [1, 2, 3, 4].map((i) => `${name(1)}.part00${i}`))
    assert.deepEqual(await fetchBackup(s, name(1)), enc)
    await s.del([`${name(1)}.part003`])
    await assert.rejects(fetchBackup(s, name(1)), /incomplete/)
  } finally { rmSync(dir, { recursive: true, force: true }) }
})

test('restore refuses to overwrite an existing file', async () => {
  const dir = tmp()
  try {
    const out = join(dir, 'x.db'); writeFileSync(out, 'keep me')
    await assert.rejects(restoreBackup({ store: fsStore(join(dir, 's')), key, name: 'latest', out }), /refusing to overwrite/)
  } finally { rmSync(dir, { recursive: true, force: true }) }
})

test('stamp uses Pakistan time (UTC+5)', () => {
  assert.equal(stamp(new Date('2026-11-04T22:00:12Z')), '20261105-030012')
})

test('supabaseStore talks the documented REST shapes (fake local server)', async () => {
  const objs = new Map(), seen = []
  const srv = createServer((req, res) => {
    const chunks = []
    req.on('data', (c) => chunks.push(c)).on('end', () => {
      const body = Buffer.concat(chunks), url = decodeURIComponent(req.url)
      seen.push({ m: req.method, url, apikey: req.headers.apikey, auth: req.headers.authorization, upsert: req.headers['x-upsert'], ct: req.headers['content-type'] })
      const send = (code, data) => { res.writeHead(code, { 'content-type': 'application/json' }); res.end(data) }
      let m
      if (req.method === 'POST' && url === '/storage/v1/object/list/bkt') {
        const q = JSON.parse(body)
        const all = [...objs.keys()].sort().reverse().filter((n) => n.startsWith(q.prefix))
        send(200, JSON.stringify(all.slice(q.offset, q.offset + q.limit).map((n) => ({ name: n }))))
      } else if (req.method === 'POST' && (m = url.match(/^\/storage\/v1\/object\/bkt\/(.+)$/))) { objs.set(m[1], body); send(200, '{"Key":"x"}')
      } else if (req.method === 'DELETE' && url === '/storage/v1/object/bkt') { JSON.parse(body).prefixes.forEach((n) => objs.delete(n)); send(200, '[]')
      } else if (req.method === 'GET' && (m = url.match(/^\/storage\/v1\/object\/authenticated\/bkt\/(.+)$/))) { objs.has(m[1]) ? res.end(objs.get(m[1])) : send(404, '{"error":"nope"}')
      } else send(400, '{}')
    })
  })
  await new Promise((r) => srv.listen(0, '127.0.0.1', r))
  try {
    const url = `http://127.0.0.1:${srv.address().port}`
    const s = supabaseStore({ url, key: 'sb_secret_fake', bucket: 'bkt' })
    for (let i = 1; i <= 120; i++) await s.put(name(i % 30 + 1) + (i > 30 ? `.part${String(i).padStart(3, '0')}` : ''), Buffer.from('d' + i)) // 120 objects -> list must page
    assert.equal((await s.list()).length, objs.size)
    assert.ok(objs.size > 100, 'paging path used')
    const up = seen.find((x) => x.url.includes('/object/bkt/dash-'))
    assert.deepEqual([up.apikey, up.auth, up.upsert, up.ct], ['sb_secret_fake', undefined, 'true', 'application/octet-stream'])
    assert.deepEqual(await s.get(name(1)), objs.get(name(1)))
    const victims = [...objs.keys()].slice(0, 105)
    await s.del(victims)
    assert.equal(objs.size, (await s.list()).length)
    assert.ok(!victims.some((v) => objs.has(v)))
    await assert.rejects(s.get('dash-nope'), /HTTP 404/)
    const jwt = supabaseStore({ url, key: 'eyJfake.jwt.key', bucket: 'bkt' })
    await jwt.list()
    assert.equal(seen.at(-1).auth, 'Bearer eyJfake.jwt.key')
    const bad = supabaseStore({ url, key: 'sb_secret_fake', bucket: 'other' })
    await assert.rejects(bad.list(), (e) => /HTTP 400/.test(e.message) && !e.message.includes('sb_secret_fake'))
  } finally { srv.close() }
})

test('end-to-end --selftest (real app backup command, fake storage, split, restore, integrity check)', () => {
  const out = execFileSync(process.execPath, [join(here, 'backup-to-supabase.mjs'), '--selftest'], { encoding: 'utf8' })
  assert.match(out, /SELFTEST OK/)
})
