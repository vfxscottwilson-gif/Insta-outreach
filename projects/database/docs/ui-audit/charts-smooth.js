// charts-smooth.js: drop-in replacement for dash/static/charts.js (proposal, docs/ui-audit). Same contract as before
// (data-count, [data-seg], .mark with <title>, [data-pulse-run]) plus: decimals in the number tween, a hover crosshair that
// glides between points, a sliding tab pill, nav pill memory, toasts, busy buttons and the approve/reject row outcome.
// Strict CSP safe: no inline styles in markup, no eval; element.style.* (CSSOM) is allowed. Builds no paths: the server draws
// every curve (chart-smoothing.py), so there is no JS copy of the monotone spline to keep in sync.
(function () {
  'use strict';
  var mq = window.matchMedia('(prefers-reduced-motion: reduce)'), reduce = mq.matches;
  if (mq.addEventListener) mq.addEventListener('change', function (e) { reduce = e.matches; });
  var ease = function (t) { return 1 - Math.pow(1 - t, 4); };               // settles like cubic-bezier(.23,1,.32,1)
  function fmt(n, d) { d = d || 0; return Number(n).toLocaleString('en-US', { minimumFractionDigits: d, maximumFractionDigits: d }); }
  function all(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  // --- Number tween: <b data-count="6.6" data-decimals="1" data-suffix="/10">. Starts from the value shown now, so a live
  //     update rolls from 742 to 745, not from 0. Reduced motion writes the final number at once. ---
  function countUp(el, to, ms) {
    var d = Number(el.dataset.decimals || 0), pre = el.dataset.prefix || '', suf = el.dataset.suffix || '',
        from = Number(el.dataset.shown || 0), t0 = 0;
    function put(v) { el.textContent = pre + fmt(v, d) + suf; el.dataset.shown = v; }
    if (el._raf) cancelAnimationFrame(el._raf);
    if (reduce || !isFinite(to) || from === to) { put(to); return; }
    el.style.minWidth = el.getBoundingClientRect().width + 'px';              // keep the final width: no layout shift while rolling
    function step(ts) {
      t0 = t0 || ts;
      var p = Math.min((ts - t0) / ms, 1);
      put(from + (to - from) * ease(p));
      if (p < 1) { el._raf = requestAnimationFrame(step); return; }
      put(to);
      el.classList.add('settled');
      setTimeout(function () { el.classList.remove('settled'); }, 400);
    }
    el._raf = requestAnimationFrame(step);
  }
  all('[data-count]').forEach(function (el, i) {
    setTimeout(function () { countUp(el, Number(el.dataset.count), 700); }, Math.min(i, 8) * 40);
  });

  // --- Tooltip + crosshair. Marks carry <title>; its text moves to aria-label on first hover so the browser tip does not double ours.
  //     Marks with data-x / data-y (viewBox units) also move the chart's crosshair (.xh) and focus dots (.fp, .fp2). ---
  var tip = document.createElement('div'), cur = null, hideT = 0;
  tip.className = 'tip';
  tip.setAttribute('role', 'tooltip');
  document.body.appendChild(tip);
  function textOf(mark) {
    var t = mark.querySelector('title');
    if (t) { mark.setAttribute('aria-label', t.textContent); mark.dataset.tip = t.textContent; t.remove(); }
    return mark.dataset.tip || '';
  }
  function anchor(mark, ev) {                                                 // where the tip points, in page pixels
    var svg = mark.ownerSVGElement;
    if (svg && mark.dataset.x !== undefined && mark.dataset.y !== undefined) {
      var b = svg.getBoundingClientRect(), k = b.width / svg.viewBox.baseVal.width;
      return { x: b.left + Number(mark.dataset.x) * k, y: b.top + Number(mark.dataset.y) * k, pad: 12 };
    }
    if (ev && /^mouse/.test(ev.type)) return { x: ev.clientX, y: ev.clientY, pad: 14 };
    var r = mark.getBoundingClientRect();
    return { x: r.left + r.width / 2, y: r.top, pad: 8 };
  }
  function place(a) {
    var w = tip.offsetWidth, h = tip.offsetHeight,
        x = Math.max(8, Math.min(a.x - w / 2, window.innerWidth - w - 8)), y = a.y - h - a.pad;
    if (y < 8) y = a.y + a.pad;
    tip.style.transform = 'translate(' + Math.round(x) + 'px,' + Math.round(y) + 'px)';
  }
  function crosshair(mark, on) {
    var svg = mark.ownerSVGElement, has = mark.dataset.x !== undefined;
    if (!svg) return;
    var first = on && has && !svg.classList.contains('hot');
    if (first) svg.classList.add('snap');                                     // first hover jumps there, later moves glide
    svg.classList.toggle('hot', on && has);
    if (on && has) {
      var x = Number(mark.dataset.x), xh = svg.querySelector('.xh'), fp = svg.querySelector('.fp:not(.fp2)'), fp2 = svg.querySelector('.fp2');
      if (xh) xh.style.transform = 'translateX(' + x + 'px)';
      if (fp) fp.style.transform = 'translate(' + x + 'px,' + Number(mark.dataset.y) + 'px)';
      if (fp2) {
        fp2.style.opacity = mark.dataset.y2 === undefined ? '0' : '';
        if (mark.dataset.y2 !== undefined) fp2.style.transform = 'translate(' + x + 'px,' + Number(mark.dataset.y2) + 'px)';
      }
    }
    if (first) requestAnimationFrame(function () { requestAnimationFrame(function () { svg.classList.remove('snap'); }); });
  }
  function show(mark, ev) {
    var text = textOf(mark);
    if (!text) return;
    clearTimeout(hideT);
    var i = text.indexOf(': ');
    tip.textContent = '';
    if (i > 0) {
      var l = document.createElement('span'), v = document.createElement('b');
      l.textContent = text.slice(0, i); v.textContent = text.slice(i + 2);
      tip.appendChild(l); tip.appendChild(v);
    } else tip.textContent = text;
    tip.classList.toggle('snap', !tip.classList.contains('on'));              // first placement: no flight from the last position
    place(anchor(mark, ev));
    tip.classList.add('on');
    if (cur && cur.ownerSVGElement !== mark.ownerSVGElement) crosshair(cur, false);   // same chart: keep it lit so the crosshair glides
    cur = mark;
    crosshair(mark, true);
  }
  function hide() {                                                           // 60 ms grace: mouseout + mouseover between two marks must not blink
    clearTimeout(hideT);
    hideT = setTimeout(function () { tip.classList.remove('on'); if (cur) crosshair(cur, false); cur = null; }, 60);
  }
  document.addEventListener('mouseover', function (e) { var m = e.target.closest && e.target.closest('.mark'); if (m) show(m, e); });
  document.addEventListener('mousemove', function (e) { if (cur && cur.dataset.x === undefined) place(anchor(cur, e)); });   // donut: follow the pointer
  document.addEventListener('mouseout', function (e) {
    var m = e.target.closest && e.target.closest('.mark');
    if (m && !(e.relatedTarget && m.contains(e.relatedTarget))) hide();
  });
  document.addEventListener('focusin', function (e) { var m = e.target.closest && e.target.closest('.mark'); if (m) show(m); });
  document.addEventListener('focusout', function (e) { if (e.target.closest && e.target.closest('.mark')) hide(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') hide(); });
  window.addEventListener('scroll', function () { if (!(document.activeElement && document.activeElement.closest('.mark'))) hide(); }, true);

  // --- Segmented control: panels as before, plus a pill that slides (translateX, 220 ms) instead of the highlight jumping. ---
  all('[data-seg]').forEach(function (seg) {
    var name = seg.dataset.seg, tabs = all('[role=tab]', seg), pill = document.createElement('span');
    pill.className = 'pill';
    pill.setAttribute('aria-hidden', 'true');
    seg.insertBefore(pill, seg.firstChild);
    seg.classList.add('js');
    seg.style.setProperty('--n', tabs.length);
    function slide(tab) { seg.style.setProperty('--idx', tabs.indexOf(tab)); }
    slide(tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0] || tabs[0]);
    requestAnimationFrame(function () { requestAnimationFrame(function () { pill.classList.add('go'); }); });   // no slide on first paint
    function pick(tab, focus) {
      tabs.forEach(function (t) { var on = t === tab; t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1; });
      slide(tab);
      all('[data-seg-panel="' + name + '"]').forEach(function (p) {
        var on = p.dataset.val === tab.dataset.val;
        if (on && p.hidden) { p.hidden = false; p.classList.remove('swap'); void p.offsetWidth; p.classList.add('swap'); }   // display:none -> block replays the chart draw-in
        else if (!on) p.hidden = true;
      });
      if (focus) tab.focus();
      try { var u = new URL(tab.href); history.replaceState(null, '', u.pathname + u.search); } catch (err) { /* ignore */ }
    }
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function (e) { e.preventDefault(); pick(tab); });
      tab.addEventListener('keydown', function (e) {
        var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (d) { e.preventDefault(); pick(tabs[(i + d + tabs.length) % tabs.length], true); }
      });
    });
  });

  // --- Pulse: every 60 s ask /api/pulse for rows synced since the run id the page was rendered with. Fixed: the old file never
  //     started polling when the page was opened in a background tab; poll() already skips hidden tabs, so always schedule it. ---
  var hero = document.querySelector('[data-pulse-run]');
  if (hero) {
    var since = hero.dataset.pulseRun, out = document.querySelector('[data-pulse-out]'), seen = 0;
    var poll = function () {
      if (document.hidden) return;
      fetch('/api/pulse?since=' + encodeURIComponent(since), { credentials: 'same-origin', headers: { Accept: 'application/json' } })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (d) {
          if (!d || !(d.new_rows > seen)) return;
          seen = d.new_rows;
          if (out) { out.textContent = d.new_rows.toLocaleString('en-US') + ' new since you opened this page'; out.hidden = false; }
          all('[data-live]', hero.closest('main') || document).forEach(function (el) { if (d[el.dataset.live] !== undefined) countUp(el, d[el.dataset.live], 600); });
          hero.classList.remove('pulse'); void hero.offsetWidth; hero.classList.add('pulse');
        })
        .catch(function () { /* offline: try again next minute */ });
    };
    setInterval(poll, 60000);
    document.addEventListener('visibilitychange', function () { if (!document.hidden) poll(); });
  }

  // --- Flash messages and toasts: non-errors leave by themselves after 5 s (hover pauses). ---
  function autoDismiss(f, ms) {
    var t = setTimeout(go, ms);
    function go() { f.classList.add('out'); setTimeout(function () { f.remove(); }, 220); }
    f.addEventListener('mouseenter', function () { clearTimeout(t); });
    f.addEventListener('mouseleave', function () { t = setTimeout(go, 2000); });
  }
  all('.flash:not(.error)').forEach(function (f) { autoDismiss(f, 5000); });
  function toast(msg, kind) {
    var box = document.getElementById('toasts');
    if (!box) { box = document.createElement('div'); box.id = 'toasts'; box.setAttribute('aria-live', 'polite'); document.body.appendChild(box); }
    var t = document.createElement('div'), s = document.createElement('span');
    t.className = 'flash ' + (kind || 'ok');
    t.setAttribute('role', 'status');
    s.textContent = msg;
    t.appendChild(s);
    box.appendChild(t);
    autoDismiss(t, 4000);
  }

  // --- Nav pill: one highlight that glides from the previous page's item to this one (full page loads, so the old
  //     position is kept in sessionStorage). Without JS the plain [aria-current] background still shows. ---
  var nav = document.querySelector('.side nav'), here = nav && nav.querySelector('a[aria-current=page]');
  if (nav && here) {
    var pill = document.createElement('span');
    pill.className = 'navpill';
    pill.setAttribute('aria-hidden', 'true');
    nav.insertBefore(pill, nav.firstChild);
    nav.classList.add('has-pill');
    var put = function (y) {
      pill.style.width = here.offsetWidth + 'px'; pill.style.height = here.offsetHeight + 'px';
      pill.style.left = here.offsetLeft + 'px'; pill.style.transform = 'translateY(' + y + 'px)';
    };
    var prev = NaN;
    try { var raw = sessionStorage.getItem('navY'); prev = raw === null ? NaN : Number(raw); } catch (err) { /* private mode */ }
    put(isFinite(prev) && prev !== here.offsetTop && !reduce ? prev : here.offsetTop);
    requestAnimationFrame(function () { requestAnimationFrame(function () { pill.classList.add('go'); put(here.offsetTop); }); });
    try { sessionStorage.setItem('navY', here.offsetTop); } catch (err) { /* ignore */ }
    new MutationObserver(function () { pill.classList.remove('go'); put(here.offsetTop); requestAnimationFrame(function () { pill.classList.add('go'); }); })
      .observe(document.documentElement, { attributes: true, attributeFilter: ['data-sidebar'] });   // sidebar collapse changes the link width
  }

  // --- Busy buttons: any form that really posts shows a spinner on its button and ignores a second click. ---
  document.addEventListener('submit', function (e) {
    var f = e.target;
    if (e.defaultPrevented || !f.matches || f.matches('form[data-outcome]')) return;   // admin.js confirm() declined, or handled below
    var b = e.submitter || f.querySelector('button[type=submit]');
    if (b) b.setAttribute('data-busy', '');
  });
  window.addEventListener('pageshow', function () { all('[data-busy]').forEach(function (b) { b.removeAttribute('data-busy'); }); });

  // --- Approve / reject: <form data-outcome> posts in the background, the row leaves toward the side of the decision, a toast
  //     confirms. Any failure falls back to the normal submit of the SAME button (requestSubmit keeps its formaction). ---
  document.addEventListener('submit', function (e) {
    var f = e.target;
    if (e.defaultPrevented || !f.matches || !f.matches('form[data-outcome]') || f.dataset.plain) return;
    var b = e.submitter, url = (b && b.formAction) || f.action, no = /reject/.test(url), row = f.closest('tr');
    e.preventDefault();
    function plain() { f.dataset.plain = '1'; f.requestSubmit(b); }
    if (!row) { plain(); return; }
    fetch(url, { method: 'POST', body: new FormData(f), credentials: 'same-origin', headers: { 'X-Requested-With': 'fetch' } })
      .then(function (r) {
        if (!r.ok) throw new Error(r.status);
        row.classList.add(no ? 'out-no' : 'out-ok');
        toast(no ? 'Rejected' : 'Approved', no ? 'warn' : 'ok');
        setTimeout(function () { row.remove(); }, 260);
      })
      .catch(plain);
  });

  if (typeof module !== 'undefined' && module.exports) module.exports = { ease: ease, fmt: fmt, countUp: countUp, anchor: anchor, toast: toast };
})();
