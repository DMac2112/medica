(() => {
  if (typeof ClinicSchedule === 'undefined' || !document.getElementById('board-date')) return;
  const setText = (id,text) => { const el=document.getElementById(id); if(el) el.textContent=text; };
  function update() {
    const now=new Date(), plan=ClinicSchedule.today(now);
    document.getElementById('clock-panel').hidden=false;
    setText('board-date',new Intl.DateTimeFormat('pl-PL',{timeZone:'Europe/Warsaw',weekday:'long',day:'numeric',month:'long',year:'numeric'}).format(now));
    setText('board-clock',new Intl.DateTimeFormat('pl-PL',{timeZone:'Europe/Warsaw',hour:'2-digit',minute:'2-digit',hourCycle:'h23'}).format(now));
    setText('poz-label',plan.working?'POZ dzisiaj':'POZ dzisiaj · '+(plan.isHoliday?'święto':'weekend'));
    setText('poz-hours',plan.working?'8:00–18:00':plan.isHoliday?'Plan świąteczny':'Nieczynne');
    const pozStatus=plan.isHoliday?'Godziny do potwierdzenia w rejestracji.':{before:'Teraz zamknięte · otwarcie o 8:00',open:'Teraz otwarte według grafiku',after:'Teraz zamknięte · po godzinach POZ',closed:'W weekendy POZ nie przyjmuje'}[plan.poz.phase];
    setText('poz-state',pozStatus);
    setText('blood-state',plan.isHoliday?'Święto · pobrania do potwierdzenia':{before:'Dziś od 7:30',open:'Teraz trwa pobieranie według grafiku',after:'Dzisiejsze pobrania zakończone',closed:'W weekendy punkt pobrań nieczynny'}[plan.blood.phase]);
    setText('doctors-heading',plan.working?'Kto dziś przyjmuje?':'Lekarze · '+(plan.isHoliday?'święto':'weekend'));
    const list=document.getElementById('today-doctors');
    if(list){
      list.replaceChildren();
      if(!plan.doctors.length){const p=document.createElement('p');p.className='empty-plan';p.textContent=plan.isHoliday?'W święta nie pokazujemy zwykłego grafiku. Godziny wymagają potwierdzenia.':'Brak przyjęć POZ w stałym grafiku weekendowym. Sprawdź plan na dni robocze.';list.append(p);}
      for(const d of plan.doctors){
        const row=document.createElement('div');row.className='daily-row';
        const person=document.createElement('div');
        const name=document.createElement('strong');name.textContent=d.name;
        const role=document.createElement('span');role.className='daily-role';role.textContent=d.role;person.append(name,role);
        const shift=document.createElement('div');const hours=document.createElement('div');hours.className='daily-hours';hours.textContent=d.hours;shift.append(hours);
        const state=document.createElement('div');state.className='daily-state';state.textContent=d.uncertain?'Do potwierdzenia: piątkowa zmiana':{before:'Przyjęcia później dzisiaj',open:'W godzinach przyjęć według grafiku',after:'Dzisiejsze przyjęcia zakończone'}[d.phase];shift.append(state);
        if(!d.uncertain){const track=document.createElement('div');track.className='shift-track';track.setAttribute('aria-hidden','true');const bar=document.createElement('span');track.style.setProperty('--start',`${(d.start-480)/600*100}%`);track.style.setProperty('--duration',`${(d.end-d.start)/600*100}%`);track.append(bar);shift.append(track);}
        row.append(person,shift);list.append(row);
      }
    }
    const fallback=document.getElementById('weekly-fallback');if(fallback)fallback.hidden=true;
    const scale=document.getElementById('timeline-scale');if(scale)scale.hidden=!plan.working;
  }
  update();
  window.setInterval(update,60000);
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)update();});
})();
