// Screenshots the public login page at desktop and phone width. Usage: node shot-login.cjs <public url> <output folder>
const { createRequire } = require('module')
const req = createRequire('F:/Github Repos/projects/levelup-crm/app/package.json')
const { chromium } = req('playwright')
const [BASE, OUT] = process.argv.slice(2)
;(async () => {
  const b = await chromium.launch()
  for (const [name, w, h] of [['login-1280', 1280, 760], ['login-390', 390, 800]]) {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: w < 500 ? 2 : 1 })
    await p.goto(BASE + '/login', { waitUntil: 'networkidle' }); await p.waitForTimeout(1500)
    await p.screenshot({ path: `${OUT}/${name}.png` }); await p.close()
  }
  await b.close(); console.log('saved')
})()
