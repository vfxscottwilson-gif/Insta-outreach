// Checks the public address end to end: login page, real login with a demo account, a few pages, logout.
// Usage: node online-check.cjs <public url> <credentials file> [screenshot folder]
const { createRequire } = require('module')
const req = createRequire('F:/Github Repos/projects/levelup-crm/app/package.json')
const { chromium } = req('playwright')
const fs = require('fs')
const [BASE, CREDS, SHOTS] = process.argv.slice(2)
const c = fs.readFileSync(CREDS, 'utf8').split('\n').map(l => l.trim().split(/\s+/)).find(p => p[0] === 'admin')
;(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 1280, height: 860 } }); const p = await ctx.newPage()
  const out = []; const errs = []
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text().slice(0, 100)) })
  const step = (n, ok, extra = '') => out.push(`${ok ? 'PASS' : 'FAIL'} ${n} ${extra}`)
  let r = await p.goto(BASE + '/admin/login', { waitUntil: 'domcontentloaded' }); step('admin login page', r.status() === 200, 'HTTP ' + r.status())
  await p.fill('#email', c[1]); await p.fill('#password', c[2])
  await Promise.all([p.waitForNavigation({ waitUntil: 'domcontentloaded', timeout: 45000 }), p.press('#password', 'Enter')])
  step('signed in', !p.url().includes('/login'), 'now at ' + new URL(p.url()).pathname)
  step('stays on the public address', p.url().startsWith(BASE), new URL(p.url()).host)
  for (const path of ['/', '/leads', '/countries', '/admin/approvals']) {
    r = await p.goto(BASE + path, { waitUntil: 'domcontentloaded' }); step('page ' + path, r.status() === 200, 'HTTP ' + r.status())
  }
  const cookies = await ctx.cookies(); step('session cookie set', cookies.length > 0, cookies.map(k => `${k.name}(secure=${k.secure},httpOnly=${k.httpOnly},sameSite=${k.sameSite})`).join(' '))
  if (SHOTS) { await p.goto(BASE + '/', { waitUntil: 'networkidle' }); await p.waitForTimeout(1600); await p.screenshot({ path: SHOTS + '/online-dashboard.png' }) }
  await p.close(); await b.close()
  console.log(out.join('\n')); console.log('console errors:', errs.length ? errs.join(' | ') : 'none')
})().catch(e => { console.log('FAIL script error', e.message); process.exit(1) })
