const test = require('node:test');
const assert = require('node:assert/strict');
const { todayPlan } = require('../app.js');
test('zwykły wtorek: plan POZ, nie status dostępności', () => {
  assert.deepEqual(todayPlan(new Date('2026-10-13T10:00:00Z')), {label:'Dziś, wtorek · POZ', hours:'8:00–18:00', note:'Plan dnia · godziny do potwierdzenia'});
});
test('weekend odsyła do pomocy poza POZ', () => {
  assert.equal(todayPlan(new Date('2026-10-17T10:00:00Z')).hours,'Nieczynne');
});
test('święto nie pokazuje zwykłych godzin', () => {
  assert.equal(todayPlan(new Date('2026-11-11T10:00:00Z')).hours,'Święto');
  assert.equal(todayPlan(new Date('2027-03-29T10:00:00Z')).hours,'Święto');
});
test('dzień liczony w Warszawie, również na granicy UTC', () => {
  assert.equal(todayPlan(new Date('2026-10-16T22:30:00Z')).hours,'Nieczynne');
});
test('zmiana godziny nie udaje informacji o wolnej wizycie', () => {
  assert.equal(todayPlan(new Date('2026-10-13T18:30:00Z')).hours,'8:00–18:00');
});
