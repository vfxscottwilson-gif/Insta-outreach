// Public front door for the Database dashboard. Every request is passed to the owner's PC through a
// Cloudflare tunnel whose current address the PC writes into KV key "origin" (install/online-supervisor.mjs).
// The visitor always uses the same workers.dev address, even when the tunnel address changes.
const SKIP = new Set(['connection', 'keep-alive', 'proxy-authenticate', 'proxy-authorization', 'te', 'trailer', 'transfer-encoding',
  'upgrade', 'host', 'content-length', 'cf-connecting-ip', 'cf-ipcountry', 'cf-ray', 'cf-visitor', 'cf-worker', 'x-forwarded-for', 'x-real-ip'])

const offline = () => new Response(
  '<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><meta http-equiv=refresh content=20>' +
  '<title>Database is offline</title><body style="margin:0;display:grid;place-items:center;min-height:100vh;background:#141416;color:#ececef;font:16px system-ui">' +
  '<div style="max-width:420px;padding:24px;text-align:center"><h1 style="font-size:22px">Database is offline for a moment</h1>' +
  '<p style="color:#a5a5b0">The computer that runs it is restarting or switched off. This page retries by itself every 20 seconds.</p></div>',
  { status: 503, headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store', 'retry-after': '20' } })

export default {
  async fetch(request, env) {
    const url = new URL(request.url)
    const origin = await env.ORIGIN_KV.get('origin', { cacheTtl: 30 })
    if (!origin) return offline()
    const target = new URL(url.pathname + url.search, origin)
    const headers = new Headers()
    for (const [k, v] of request.headers) if (!SKIP.has(k.toLowerCase())) headers.set(k, v)
    headers.set('X-Forwarded-Proto', 'https')
    headers.set('X-Forwarded-Host', url.host)
    headers.set('X-Client-IP', request.headers.get('CF-Connecting-IP') || '')
    let res
    try {
      // Buffer the (small) request body so the origin gets a normal Content-Length, not a chunked stream.
      const body = request.method === 'GET' || request.method === 'HEAD' ? undefined : await request.arrayBuffer()
      res = await fetch(target, { method: request.method, headers, body, redirect: 'manual' })
    } catch (e) {
      return offline()
    }
    if (res.status === 530 || res.status === 502 || res.status === 503 || res.status === 504) return offline() // tunnel down
    const out = new Headers(res.headers)
    const loc = out.get('Location')
    if (loc) {
      try {
        const l = new URL(loc, target)
        if (l.origin === new URL(origin).origin) out.set('Location', url.origin + l.pathname + l.search + l.hash)
      } catch (e) { /* leave as is */ }
    }
    return new Response(res.body, { status: res.status, statusText: res.statusText, headers: out })
  },
}
