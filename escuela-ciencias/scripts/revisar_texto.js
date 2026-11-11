#!/usr/bin/env node
// Busca referencias personales o de origen en una app de estudio antes de publicarla.
// Uso: node revisar_texto.js app.html
// Lee el texto visible de todas las pestañas y de los datos (DEF, STEPS, CAPS, preguntas, SUM).
// Debe imprimir "0 coincidencias". Si encuentra algo, reescríbelo en tono neutral.
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const file = process.argv[2];
  if (!file) { console.error('Uso: node revisar_texto.js app.html'); process.exit(2); }
  const url = 'file://' + path.resolve(file);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1300, height: 900 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto(url); await p.waitForTimeout(400);
  let txt = '';
  const n = await p.evaluate(() => typeof QT !== 'undefined' ? QT.length : 0);
  for (let i = 0; i < n; i++) { await p.evaluate(i => { setT(QT[i]); renderPanel(); }, i); txt += await p.innerText('main') + '\n'; }
  for (const v of ['leer', 'general', 'examen', 'practica']) { await p.goto(url + '#' + v); await p.waitForTimeout(400); txt += await p.innerText('main') + '\n'; }
  txt += await p.evaluate(() => {
    const g = n => (typeof window[n] !== 'undefined' ? window[n] : (() => { try { return eval(n); } catch (e) { return null; } })());
    const out = [];
    const add = v => { if (v == null) return; if (typeof v === 'string') out.push(v.replace(/<[^>]+>/g, ' ')); else if (Array.isArray(v)) v.forEach(add); else if (typeof v === 'object') Object.values(v).forEach(add); };
    ['DEF', 'STEPS', 'CAPS', 'SUM', 'MC', 'FILL', 'CASOS', 'ABS', 'PAREO', 'PAREOP', 'ENZ_M', 'STEPS2_M'].forEach(n => add(g(n)));
    return out.join('\n');
  });
  const re = /.{0,40}(🎥|🔶|⚠|\bvideo\b|\bppt\b|diapositiva|examen anterior|año pasado|profesora|marcó|\btus\b|\btu (?:clase|prueba|profe|ppt)|pregúntale|confírmalo|apuntes|\bexterno\b|subtitul|\d:\d\d\s*[–-]\s*\d:\d\d|minuto \d).{0,40}/gi;
  const m = [...new Set(txt.match(re) || [])];
  m.forEach(x => console.log('· ' + x.replace(/\s+/g, ' ')));
  console.log(m.length + ' coincidencias');
  if (errs.length) console.log('Errores de la página:', errs);
  await b.close(); process.exit(m.length ? 1 : 0);
})();
