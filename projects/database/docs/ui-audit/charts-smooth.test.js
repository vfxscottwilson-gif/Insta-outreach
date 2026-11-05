// Run: node docs/ui-audit/charts-smooth.test.js   (no browser, no dependencies: DOM is stubbed just enough for the file to load)
const assert = require('assert');
const path = require('path');

function load(reduced) {
  const frames = [];
  const el = () => ({ dataset: {}, style: { setProperty() {} }, classList: { add() {}, remove() {}, contains: () => false, toggle() {} },
    setAttribute() {}, appendChild() {}, insertBefore() {}, addEventListener() {}, querySelector: () => null, querySelectorAll: () => [] });
  global.window = { matchMedia: () => ({ matches: reduced, addEventListener() {} }), addEventListener() {}, innerWidth: 1280 };
  global.document = Object.assign(el(), { body: el(), documentElement: el(), createElement: el, getElementById: () => null, hidden: false });
  global.requestAnimationFrame = (f) => frames.push(f);
  global.cancelAnimationFrame = () => {};
  global.MutationObserver = class { observe() {} };
  const file = path.join(__dirname, 'charts-smooth.js');
  delete require.cache[file];
  return { api: require(file), frames };
}
function run(frames, fromMs, stepMs, endMs) {                 // fake clock: feed each queued frame a growing timestamp
  for (let t = fromMs; frames.length && t <= endMs; t += stepMs) frames.splice(0).forEach((f) => f(t));
}

// 1. formatting and easing
let { api, frames } = load(false);
assert.strictEqual(api.fmt(1234.56, 1), '1,234.6');
assert.strictEqual(api.fmt(742), '742');
assert.strictEqual(api.ease(0), 0);
assert.strictEqual(api.ease(1), 1);
let last = 0;
for (let i = 1; i <= 100; i++) { const v = api.ease(i / 100); assert(v >= last, 'ease must not go backwards'); last = v; }

// 2. tween: 0 -> 6.6 with a unit suffix; never decreases, ends exactly on the target, pins the width once
const seen = [];
const node = { dataset: { decimals: '1', suffix: '/10' }, style: {}, classList: { add() {}, remove() {} }, getBoundingClientRect: () => ({ width: 40 }) };
Object.defineProperty(node, 'textContent', { set(v) { seen.push(v); }, get() { return seen[seen.length - 1]; } });
api.countUp(node, 6.6, 700);
run(frames, 16, 16, 1000);
assert.strictEqual(seen[seen.length - 1], '6.6/10');
assert.strictEqual(node.dataset.shown, 6.6);
const nums = seen.map((s) => parseFloat(s));
assert(nums.every((v, i) => i === 0 || v >= nums[i - 1] - 1e-9), 'values rise monotonically');
assert(seen.length > 10 && seen.length < 60, 'about one write per frame: ' + seen.length);
assert.strictEqual(node.style.minWidth, '40px');

// 3. a live update starts from what is on screen, not from zero
seen.length = 0;
api.countUp(node, 8, 600);
run(frames, 2000, 16, 3000);
assert(parseFloat(seen[0]) >= 6.6 - 0.001, 'rolls up from 6.6, first frame ' + seen[0]);
assert.strictEqual(seen[seen.length - 1], '8.0/10');

// 4. reduced motion: one write, no animation frames
({ api, frames } = load(true));
const n2 = { dataset: {}, style: {}, classList: { add() {}, remove() {} }, getBoundingClientRect: () => ({ width: 10 }) };
let text = '';
Object.defineProperty(n2, 'textContent', { set(v) { text = v; }, get() { return text; } });
api.countUp(n2, 1234, 900);
assert.strictEqual(text, '1,234');
assert.strictEqual(frames.length, 0, 'no requestAnimationFrame under reduced motion');

// 5. tooltip anchor: viewBox units -> page pixels (chart drawn at half size, 100 px from the left, 50 from the top)
({ api } = load(false));
const mark = { ownerSVGElement: { getBoundingClientRect: () => ({ left: 100, top: 50, width: 300 }), viewBox: { baseVal: { width: 600 } } },
  dataset: { x: '200', y: '80' } };
assert.deepStrictEqual(api.anchor(mark, null), { x: 200, y: 90, pad: 12 });
const donut = { ownerSVGElement: null, dataset: {}, getBoundingClientRect: () => ({ left: 10, top: 20, width: 100 }) };
assert.deepStrictEqual(api.anchor(donut, { type: 'mousemove', clientX: 33, clientY: 44 }), { x: 33, y: 44, pad: 14 });
assert.deepStrictEqual(api.anchor(donut, null), { x: 60, y: 20, pad: 8 });

console.log('charts-smooth.test.js OK (format, ease, tween, live update, reduced motion, anchor)');
