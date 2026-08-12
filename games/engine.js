/* engine.js v2 — shared game engine for Loki's Mischief
   Implements the "00 // CORE" contract from the Loki Engine design bible:
     state machine idle/playing/paused/win/lose  ·  rAF loop with dt clamped to 32ms
     tap + keyboard parity  ·  localStorage loki_best_<id> (try/catch wrapped)
     pause on visibilitychange + blur (AudioContext suspended, resumed on interaction)
     audio muted by default, persistent toggle  ·  reduced-motion cuts particles 70%
     client-side 1080x1350 share card via offscreen canvas.toDataURL (no backend)

   Page contract: needs #bg (backdrop canvas) and #stage (panels). A game registers as
     Engine._game = { id, deity, lesson, mount(), onResize(w,h), onHide(), onPause(), onResume() }

   Assumptions: no build step, no external libs, dark palette only (#080c12).
   Non-obvious logic is commented inline; the important ones:
     - dt is clamped so a backgrounded tab can't resume with a huge delta and teleport entities.
     - the backdrop loop runs independently of game state so menus stay alive, but it self-throttles
       while hidden to avoid burning CPU in a background tab.
     - best-score writes are try/catch'd because localStorage throws in private mode / quota-full.
*/
const Engine = (() => {
  const C = { void:'#080c12', card:'#111a26', border:'#1e2e45', ice:'#7dd3e0', gold:'#d4b778' };
  const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;

  let state = 'idle';                 // idle > playing > paused > win|lose
  let raf = null, last = 0, onFrame = null;
  let bg, bgx, particles = [], bgRaf = null;
  let audioCtx = null;
  let muted = true;                   // bible: audio never auto-plays
  let hudMuteBtn = null;

  // ---------- persistence (never throw: private mode / quota) ----------
  function bestKey(id){ return 'loki_best_'+id; }
  function getBest(id){
    try { const v = localStorage.getItem(bestKey(id)); if(!v) return 0;
      // v2 stores JSON {score,date,meta}; v1 stored a bare integer — read both.
      if(v[0]==='{'){ return parseInt(JSON.parse(v).score,10)||0; }
      return parseInt(v,10)||0;
    } catch(e){ return 0; }
  }
  function setBest(id, v, meta){
    try {
      if(v > getBest(id))
        localStorage.setItem(bestKey(id), JSON.stringify({score:v, date:new Date().toISOString().slice(0,10), meta:meta||null}));
    } catch(e){ /* storage unavailable — scores are a nicety, never fatal */ }
  }
  function getMeta(id){ try { const v=localStorage.getItem(bestKey(id)); return (v&&v[0]==='{')?JSON.parse(v):null; } catch(e){ return null; } }

  // ---------- Yggdrasil procedural backdrop ----------
  function initBg(){
    bg = document.getElementById('bg'); if(!bg) return; bgx = bg.getContext('2d');
    resizeBg();
    // reduced-motion: 70% fewer particles per the bible's a11y rule
    const n = REDUCED ? 21 : 70;
    for(let i=0;i<n;i++) particles.push(spawn());
    loopBg();
  }
  function spawn(){
    return { x:Math.random()*innerWidth, y:Math.random()*innerHeight,
      vy:-(0.15+Math.random()*0.5), r:0.6+Math.random()*1.8,
      a:0.2+Math.random()*0.6, hue:Math.random()<0.5?C.ice:C.gold };
  }
  function resizeBg(){ if(bg){ bg.width=innerWidth; bg.height=innerHeight; } }
  function loopBg(){
    if(document.hidden){ bgRaf = setTimeout(loopBg, 500); return; } // throttle in background tab
    bgx.clearRect(0,0,bg.width,bg.height);
    bgx.fillStyle=C.void; bgx.fillRect(0,0,bg.width,bg.height);
    bgx.strokeStyle='rgba(30,46,69,0.5)'; bgx.lineWidth=2;
    drawBranch(bg.width/2, bg.height, bg.height*0.34, -Math.PI/2, REDUCED?5:7);
    for(const p of particles){
      p.y += p.vy; if(p.y < -5){ Object.assign(p, spawn(), {y:bg.height+5}); }
      bgx.globalAlpha=p.a; bgx.fillStyle=p.hue;
      bgx.beginPath(); bgx.arc(p.x,p.y,p.r,0,7); bgx.fill();
    }
    bgx.globalAlpha=1; bgRaf = requestAnimationFrame(loopBg);
  }
  function drawBranch(x,y,len,ang,d){
    if(d<=0||len<6) return;
    const x2=x+Math.cos(ang)*len, y2=y+Math.sin(ang)*len;
    bgx.beginPath(); bgx.moveTo(x,y); bgx.lineTo(x2,y2); bgx.stroke();
    drawBranch(x2,y2,len*0.72,ang-0.35,d-1);
    drawBranch(x2,y2,len*0.72,ang+0.35,d-1);
  }

  // ---------- audio: one lazy AudioContext, master gain 0.15, muted default ----------
  function ensureAudio(){
    if(!audioCtx){
      audioCtx = new (window.AudioContext||window.webkitAudioContext)();
      Engine.master = audioCtx.createGain(); Engine.master.gain.value = 0.15;
      Engine.master.connect(audioCtx.destination);
    }
    // browsers start contexts suspended until a gesture
    if(audioCtx.state === 'suspended') audioCtx.resume();
    return audioCtx;
  }
  function blip(freq=440, dur=0.08, type='sine', vol=0.2){
    if(muted) return;
    try {
      const ctx = ensureAudio();
      const o=ctx.createOscillator(), g=ctx.createGain();
      o.type=type; o.frequency.value=freq;
      // envelope 0.01 -> vol -> 0.001 (bible: gain envelope, no clicks)
      g.gain.setValueAtTime(0.0001, ctx.currentTime);
      g.gain.exponentialRampToValueAtTime(Math.max(0.001,vol), ctx.currentTime+0.012);
      g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime+dur);
      o.connect(g); g.connect(Engine.master); o.start(); o.stop(ctx.currentTime+dur+0.02);
    } catch(e){ /* audio is decorative — never break the game for it */ }
  }
  function setMuted(m){
    muted = !!m;
    try { localStorage.setItem('loki_muted', muted?'1':'0'); } catch(e){}
    if(muted && audioCtx && audioCtx.state==='running') audioCtx.suspend();
    if(hudMuteBtn) hudMuteBtn.textContent = muted ? '🔇' : '🔊';
  }
  function toggleMute(){ setMuted(!muted); if(!muted) ensureAudio(); }

  // ---------- main loop + pause ----------
  function startLoop(fn){
    onFrame = fn; last = performance.now();
    if(raf) cancelAnimationFrame(raf);
    const tick = (t) => {
      // clamp dt at 32ms: a resumed background tab must not jump entities across the board
      const dt = Math.min(32, t - last) / 1000; last = t;
      if(state === 'playing' && onFrame) onFrame(dt);
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
  }
  function stopLoop(){ if(raf){ cancelAnimationFrame(raf); raf=null; } }
  function setState(s){ state = s; }

  function pause(show){
    if(state !== 'playing') return;
    state = 'paused';
    if(audioCtx && audioCtx.state === 'running') audioCtx.suspend();
    if(Engine._game && Engine._game.onPause) Engine._game.onPause();
    if(show !== false) showPauseOverlay();
  }
  function resume(){
    if(state !== 'paused') return;
    hidePauseOverlay();
    last = performance.now();               // reset so dt doesn't include the paused span
    state = 'playing';
    if(!muted && audioCtx && audioCtx.state === 'suspended') audioCtx.resume();
    if(Engine._game && Engine._game.onResume) Engine._game.onResume();
  }
  function showPauseOverlay(){
    if(document.getElementById('pauseOv')) return;
    const d = document.createElement('div');
    d.id = 'pauseOv';
    d.setAttribute('role','dialog'); d.setAttribute('aria-label','Paused');
    d.innerHTML = '<div class="panel"><h1>Paused</h1><p>The Norns wait.</p>' +
      '<div class="row"><button class="btn" id="resumeBtn">Resume</button></div></div>';
    document.body.appendChild(d);
    d.querySelector('#resumeBtn').onclick = resume;
  }
  function hidePauseOverlay(){ const d=document.getElementById('pauseOv'); if(d) d.remove(); }

  // ---------- HUD: persistent mute + pause controls (tap targets >= 44px via engine.css) ----------
  function mountControls(){
    if(document.getElementById('engineCtl')) return;
    const wrap = document.createElement('div'); wrap.id='engineCtl';
    const mute = document.createElement('button');
    mute.className='ectl'; mute.id='muteBtn'; mute.type='button';
    mute.setAttribute('aria-label','Toggle sound'); mute.textContent = muted?'🔇':'🔊';
    mute.onclick = toggleMute; hudMuteBtn = mute;
    const pb = document.createElement('button');
    pb.className='ectl'; pb.id='pauseBtn'; pb.type='button';
    pb.setAttribute('aria-label','Pause or resume'); pb.textContent='⏸';
    pb.onclick = () => { state==='paused' ? resume() : pause(); };
    wrap.appendChild(mute); wrap.appendChild(pb);
    document.body.appendChild(wrap);
  }

  // ---------- share card: 1080x1350, generated client-side, no server ----------
  function shareCard(opts){
    const W=1080, H=1350;
    const cv = document.createElement('canvas'); cv.width=W; cv.height=H;
    const x = cv.getContext('2d');
    // background + vignette
    x.fillStyle = C.void; x.fillRect(0,0,W,H);
    const g = x.createRadialGradient(W/2,H*0.38,60,W/2,H*0.38,H*0.8);
    g.addColorStop(0,'#12203040'); g.addColorStop(1,'#05080d');
    x.fillStyle=g; x.fillRect(0,0,W,H);
    // gold frame
    x.strokeStyle=C.gold; x.lineWidth=6; x.strokeRect(40,40,W-80,H-80);
    x.strokeStyle='rgba(212,183,120,.28)'; x.lineWidth=2; x.strokeRect(60,60,W-120,H-120);
    // grain (bible: grain texture + foil gradient)
    for(let i=0;i<2600;i++){
      x.globalAlpha = Math.random()*0.05;
      x.fillStyle = Math.random()<0.5?'#ffffff':'#000000';
      x.fillRect(Math.random()*W, Math.random()*H, 2, 2);
    }
    x.globalAlpha = 1;
    x.textAlign='center';
    x.fillStyle=C.gold; x.font='900 40px Cinzel, serif';
    x.fillText("LOKI'S MISCHIEF", W/2, 160);
    x.fillStyle='#64748b'; x.font='600 22px Inter, sans-serif';
    x.fillText((opts.game||'').toUpperCase(), W/2, 202);
    // headline
    x.fillStyle='#e2e8f0'; x.font='700 62px Cinzel, serif';
    wrapText(x, opts.title || 'Well Met', W/2, 340, W-200, 70);
    // score foil
    const fg = x.createLinearGradient(W/2-260,0,W/2+260,0);
    fg.addColorStop(0,'#8a6f34'); fg.addColorStop(.5,'#f0d998'); fg.addColorStop(1,'#8a6f34');
    x.fillStyle=fg; x.font='900 150px Cinzel, serif';
    x.fillText(String(opts.score ?? ''), W/2, 560);
    if(opts.sub){ x.fillStyle=C.ice; x.font='600 30px Inter, sans-serif'; x.fillText(opts.sub, W/2, 620); }
    // runes strip (decorative, colorblind-safe: glyph shapes not colour)
    x.fillStyle='rgba(125,211,224,.55)'; x.font='400 54px serif';
    x.fillText('ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ ᚷ ᚹ', W/2, 720);
    // lesson block
    x.fillStyle='#94a3b8'; x.font='400 30px Inter, sans-serif';
    wrapText(x, '✦ ' + (opts.lesson||''), W/2, 830, W-220, 44);
    // footer
    x.fillStyle=C.gold; x.font='600 26px Inter, sans-serif';
    x.fillText('lokibeinblodsson-ctrl.github.io/lokis-mischief', W/2, H-130);
    x.fillStyle='#475569'; x.font='400 22px Inter, sans-serif';
    x.fillText(new Date().toISOString().slice(0,10), W/2, H-92);
    return cv.toDataURL('image/png');
  }
  function wrapText(x, text, cx0, y, maxW, lh){
    const words = String(text).split(/\s+/); let line='', yy=y;
    for(const w of words){
      const test = line ? line+' '+w : w;
      if(x.measureText(test).width > maxW && line){ x.fillText(line, cx0, yy); line=w; yy+=lh; }
      else line = test;
    }
    if(line) x.fillText(line, cx0, yy);
    return yy;
  }
  async function share(opts){
    const url = shareCard(opts);
    const name = `loki-${opts.game||'score'}-${Date.now()}.png`;
    try {
      // Web Share API with a real file where supported (mobile); download elsewhere.
      const blob = await (await fetch(url)).blob();
      const file = new File([blob], name, {type:'image/png'});
      if(navigator.canShare && navigator.canShare({files:[file]})){
        await navigator.share({files:[file], title:"Loki's Mischief", text:opts.title||''});
        return;
      }
    } catch(e){ /* fall through to download */ }
    const a=document.createElement('a'); a.href=url; a.download=name; a.click();
  }

  // ---------- end screen ----------
  function showEnd(opts){
    setState(opts.won ? 'win' : 'lose');
    stopLoop();
    const id = (Engine._game && Engine._game.id) || opts.game || 'game';
    const prev = getBest(id);
    setBest(id, opts.score|0, opts.meta);
    const isRecord = (opts.score|0) > prev;
    const el = document.getElementById('stage');
    el.innerHTML = `<div class="panel">
      <h1>${opts.title||'Well Met'}</h1>
      <p>Score <b style="color:var(--gold)">${opts.score}</b>${opts.sub?(' · '+opts.sub):''}</p>
      <p style="font-size:12px;color:${isRecord?'var(--ice)':'#64748b'}">
        ${isRecord ? '★ New personal best!' : 'Best: '+prev}</p>
      <div class="lesson">✦ ${opts.lesson||''}</div>
      <div class="row">
        <a class="btn ghost" href="../${opts.deity||'index'}.html">See ${cap(opts.deity||'the')} lesson →</a>
        <a class="btn ice" href="https://blodsson.gumroad.com" target="_blank" rel="noopener">Get the workflow →</a>
      </div>
      <div class="row">
        <button class="btn" id="againBtn" type="button">Play again</button>
        <button class="btn ghost" id="shareBtn" type="button">Share card</button>
      </div></div>`;
    el.querySelector('#againBtn').onclick = () => location.reload();
    el.querySelector('#shareBtn').onclick = () => share({
      game: id, title: opts.title||'', score: opts.score, sub: opts.sub||'', lesson: opts.lesson||'' });
  }
  function cap(s){ return String(s).charAt(0).toUpperCase()+String(s).slice(1); }

  // ---------- canvas fit ----------
  function fitCanvas(cv){
    const w=Math.max(1,innerWidth), h=Math.max(1,innerHeight);
    cv.width=w; cv.height=h;
    return {w,h};
  }

  function init(){
    try { muted = (localStorage.getItem('loki_muted') ?? '1') === '1'; } catch(e){ muted = true; }
    initBg();
    mountControls();
    addEventListener('resize', () => { resizeBg(); if(Engine._game&&Engine._game.onResize) Engine._game.onResize(innerWidth,innerHeight); });
    addEventListener('orientationchange', () => { setTimeout(()=>{ if(Engine._game&&Engine._game.onResize) Engine._game.onResize(innerWidth,innerHeight); },300); });
    // bible: pause on visibilitychange AND blur, resume only on explicit interaction
    document.addEventListener('visibilitychange', () => {
      if(document.hidden){ if(Engine._game&&Engine._game.onHide) Engine._game.onHide(); pause(); }
    });
    addEventListener('blur', () => pause());
    // Esc / P toggles pause everywhere (keyboard parity)
    addEventListener('keydown', (e) => {
      if(e.key==='Escape' || e.key==='p' || e.key==='P'){ state==='paused' ? resume() : pause(); }
      if(e.key==='m' || e.key==='M'){ toggleMute(); }
    });
  }

  return { C, REDUCED, init, startLoop, stopLoop, setState, get state(){return state;},
    pause, resume, bestKey, getBest, setBest, getMeta,
    blip, setMuted, toggleMute, get muted(){return muted;}, ensureAudio,
    showEnd, shareCard, share, fitCanvas, wrapText, _game:null, master:null };
})();
window.addEventListener('DOMContentLoaded', Engine.init);
