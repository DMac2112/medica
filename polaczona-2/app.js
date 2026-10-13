/* Plan tygodniowy z zegara urządzenia; nie informacja o dostępności wizyt. */
(function () {
  'use strict';
  function easter(year) {
    const a = year % 19, b = Math.floor(year / 100), c = year % 100;
    const d = Math.floor(b / 4), e = b % 4, f = Math.floor((b + 8) / 25);
    const g = Math.floor((b - f + 1) / 3), h = (19 * a + b - d - g + 15) % 30;
    const i = Math.floor(c / 4), k = c % 4, l = (32 + 2 * e + 2 * i - h - k) % 7;
    const m = Math.floor((a + 11 * h + 22 * l) / 451);
    return new Date(Date.UTC(year, Math.floor((h + l - 7 * m + 114) / 31) - 1, (h + l - 7 * m + 114) % 31 + 1));
  }
  function todayPlan(now) {
    const parts = Object.fromEntries(new Intl.DateTimeFormat('en-GB', {timeZone:'Europe/Warsaw',year:'numeric',month:'2-digit',day:'2-digit',weekday:'short'}).formatToParts(now).map(p => [p.type,p.value]));
    const weekday = new Intl.DateTimeFormat('pl-PL', {timeZone:'Europe/Warsaw',weekday:'long'}).format(now);
    const day = `${parts.month}-${parts.day}`, year = Number(parts.year);
    const fixed = ['01-01','01-06','05-01','05-03','08-15','11-01','11-11','12-25','12-26'];
    if (year >= 2025) fixed.push('12-24');
    const key = `${parts.year}-${day}`;
    const movable = [0,1,49,60].map(offset => {
      const date = easter(year); date.setUTCDate(date.getUTCDate() + offset);
      return date.toISOString().slice(0,10);
    });
    if (fixed.includes(day) || movable.includes(key)) return {label:`Dziś, ${weekday} · POZ`,hours:'Święto',note:'Zobacz pomoc poza godzinami POZ'};
    if (['Sat','Sun'].includes(parts.weekday)) return {label:`Dziś, ${weekday} · POZ`,hours:'Nieczynne',note:'Zobacz pomoc poza godzinami POZ'};
    return {label:`Dziś, ${weekday} · POZ`,hours:'8:00–18:00',note:'Plan dnia · godziny do potwierdzenia'};
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = {todayPlan};
  if (typeof document === 'undefined') return;
  function update() {
    const plan = todayPlan(new Date());
    const todayLink = document.querySelector('[data-today-link]');
    if (todayLink) todayLink.href = plan.hours === '8:00–18:00' ? 'godziny.html#godziny' : 'kontakt.html#pomoc';
    for (const field of ['label','hours','note']) {
      const element = document.querySelector(`[data-today="${field}"]`);
      if (element) element.textContent = plan[field];
    }
  }
  function revealHash() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    if (!target) return;
    const disclosure = target.closest('details');
    if (disclosure) disclosure.open = true;
  }
  update(); revealHash();
  window.addEventListener('hashchange', revealHash);
  window.addEventListener('pageshow', update);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) update(); });
  window.setInterval(update, 60000);
})();
