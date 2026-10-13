/* Źródło: audit/pages/oferta-poz.md i laboratorium.md. Status oznacza plan, nie obecność. */
var ClinicSchedule = (() => {
  const doctors = /* DATA */[
    {"name":"Paweł Andrzejczak","role":"Internista, medycyna rodzinna","week":["8:00–13:00","13:00–18:00","8:00–13:00","8:00–13:00","parzyste 13:00–18:00; nieparzyste 8:00–18:00"]},
    {"name":"Piotr Lisowski","role":"Specjalista medycyny rodzinnej","week":["8:00–13:00","8:00–13:00","13:00–18:00","13:00–18:00","8:00–13:00"]},
    {"name":"Agnieszka Krawczyk-Kubisiak","role":"Specjalistka medycyny rodzinnej","week":["11:00–16:00","8:00–13:00","8:00–13:00","8:00–13:00","parzyste 8:00–13:00; nieparzyste 11:00–16:00"]},
    {"name":"Irena Grzeluszka-Tobiasz","role":"Pediatra","week":["9:00–14:00","9:00–12:30","11:00–16:00","13:00–18:00","9:00–13:00"]},
    {"name":"Ewa Marciniak","role":"Specjalistka medycyny rodzinnej","week":["8:00–13:00","13:00–18:00","8:00–13:00","8:00–13:00","parzyste 13:00–18:00; nieparzyste 8:00–13:00"]},
    {"name":"Paweł Krzywda","role":"Rezydent medycyny rodzinnej","week":[null,"15:00–18:00",null,null,"15:00–18:00"]}
  ]/* END */;
  const weekdays = ['niedziela','poniedziałek','wtorek','środa','czwartek','piątek','sobota'];
  const minutes = text => { const [h,m] = text.split(':').map(Number); return h * 60 + m; };
  function easter(year) {
    const a=year%19,b=Math.floor(year/100),c=year%100,d=Math.floor(b/4),e=b%4;
    const f=Math.floor((b+8)/25),g=Math.floor((b-f+1)/3),h=(19*a+b-d-g+15)%30;
    const i=Math.floor(c/4),k=c%4,l=(32+2*e+2*i-h-k)%7,m=Math.floor((a+11*h+22*l)/451);
    return new Date(Date.UTC(year,Math.floor((h+l-7*m+114)/31)-1,(h+l-7*m+114)%31+1));
  }
  function holiday(year,month,date) {
    // Wyjątki kalendarzowe. Godziny świąteczne wymagają potwierdzenia w przychodni.
    const fixed=['1-1','1-6','5-1','5-3','8-15','11-1','11-11','12-24','12-25','12-26'];
    if(fixed.includes(`${month}-${date}`)) return true;
    const target=Date.UTC(year,month-1,date), base=easter(year).getTime();
    return [0,1,49,60].some(offset=>target===base+offset*86400000);
  }
  function today(now = new Date()) {
    const parts = Object.fromEntries(new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/Warsaw',year:'numeric',month:'numeric',day:'numeric',hour:'2-digit',minute:'2-digit',hourCycle:'h23'}).formatToParts(now).map(p=>[p.type,p.value]));
    const year=+parts.year,month=+parts.month,date=+parts.day;
    const day=new Date(Date.UTC(year,month-1,date)).getUTCDay();
    const clock=+parts.hour*60 + +parts.minute;
    const isHoliday=holiday(year,month,date), working=day>0 && day<6 && !isHoliday;
    const service=(start,end)=>({phase:!working?'closed':clock<start?'before':clock<end?'open':'after', start,end});
    const daily = working ? doctors.filter(d=>d.week[day-1]).map(d=>{
      const hours=d.week[day-1], uncertain=hours.includes('parzyste');
      const [start,end]=uncertain?[null,null]:hours.split('–').map(minutes);
      return {...d,hours,uncertain,start,end,phase:uncertain?'uncertain':clock<start?'before':clock<end?'open':'after'};
    }) : [];
    return {year,month,date,day,weekday:weekdays[day],clock,isHoliday,working,poz:service(480,1080),blood:service(450,660),doctors:daily};
  }
  return {doctors,weekdays,today};
})();
