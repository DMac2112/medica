const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const sandbox = { Intl, Date };
if (fs.existsSync(__dirname + '/../schedule.js')) vm.runInNewContext(fs.readFileSync(__dirname + '/../schedule.js', 'utf8'), sandbox);
const plan = sandbox.ClinicSchedule;
test('POZ opening and closing boundaries use Warsaw time', () => {
 assert.ok(plan, 'Schedule API must exist');
 assert.equal(plan.today(new Date('2026-10-13T05:59:00Z')).poz.phase, 'before');
 assert.equal(plan.today(new Date('2026-10-13T06:00:00Z')).poz.phase, 'open');
 assert.equal(plan.today(new Date('2026-10-13T16:00:00Z')).poz.phase, 'after');
});
test('blood draws have their own hours, independent of POZ', () => {
 assert.ok(plan, 'Schedule API must exist');
 const result = plan.today(new Date('2026-10-13T05:30:00Z'));
 assert.equal(result.blood.phase, 'open');
 assert.equal(result.poz.phase, 'before');
 assert.equal(plan.today(new Date('2026-10-13T09:00:00Z')).blood.phase, 'after');
});
test('weekends and holiday exceptions do not display doctors as present', () => {
 assert.ok(plan, 'Schedule API must exist');
 for (const date of ['2026-10-17T10:00:00Z','2026-11-11T10:00:00Z','2026-04-06T10:00:00Z','2026-12-24T10:00:00Z']) {
  const result = plan.today(new Date(date));
  assert.equal(result.poz.phase, 'closed');
  assert.equal(result.doctors.length, 0);
 }
});
test('Friday ambiguity stays explicit rather than inventing a shift', () => {
 assert.ok(plan, 'Schedule API must exist');
 const result = plan.today(new Date('2026-10-16T10:00:00Z'));
 const doctor = result.doctors.find(d => d.name === 'Paweł Andrzejczak');
 assert.equal(doctor.uncertain, true);
 assert.equal(doctor.start, null);
 assert.match(doctor.hours, /nieparzyste 8:00–18:00/);
});
test('Tuesday schedule includes resident and paediatrician at sourced times', () => {
 assert.ok(plan, 'Schedule API must exist');
 const result = plan.today(new Date('2026-10-13T13:00:00Z'));
 assert.equal(result.doctors.length, 6);
 assert.equal(result.doctors.find(d => d.name === 'Irena Grzeluszka-Tobiasz').hours, '9:00–12:30');
 assert.equal(result.doctors.find(d => d.name === 'Paweł Krzywda').start, 900);
});
test('Warsaw day differs from UTC near midnight and in winter', () => {
 assert.ok(plan, 'Schedule API must exist');
 assert.equal(plan.today(new Date('2026-10-12T22:30:00Z')).day, 2);
 assert.equal(plan.today(new Date('2026-12-07T23:30:00Z')).day, 2);
});
test('closure sentence names today, tomorrow, or the next working date', () => {
 assert.match(plan.today(new Date('2026-10-13T05:59:00Z')).poz.message, /otwieramy dziś o 8:00/);
 assert.match(plan.today(new Date('2026-10-13T16:00:00Z')).poz.message, /otwieramy jutro o 8:00/);
 assert.match(plan.today(new Date('2026-10-16T16:00:00Z')).poz.message, /19\.10.*o 8:00/);
 assert.match(plan.today(new Date('2026-10-18T10:00:00Z')).poz.message, /otwieramy jutro o 8:00/);
 assert.match(plan.today(new Date('2026-11-10T17:00:00Z')).poz.message, /12\.11.*o 8:00/);
 assert.match(plan.today(new Date('2026-11-11T10:00:00Z')).poz.message, /do potwierdzenia/);
 assert.match(plan.today(new Date('2026-12-23T17:00:00Z')).poz.message, /28\.12.*o 8:00/);
});
