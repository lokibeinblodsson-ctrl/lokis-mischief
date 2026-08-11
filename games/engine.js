/* engine.js — shared game engine for Loki's Mischief
   Attach to a page that has #bg (backdrop canvas), #stage, and calls Engine.start(game).
   game = { id, deity, lesson, workflow, mount(el), onResize(w,h) }
*/
const Engine = (() => {
  const C = { void:'#080c12', card:'#111a26', border:'#1e2e45', ice:'#7dd3e0', gold:'#d4b778' };
  let state = 'idle';            // idle > playing > paused > win/lose
  let raf = null, last = 0, onFrame = null;
  let bg, bgx, particles = [];
  let audioCtx = null, muted = true;

  function bestKey(id){ return 'loki_best_'+id; }
  function getBest(id){ return parseInt(localStorage.getItem(bestKey(id))||'0',10); }
  function setBest(id,v){ if(v>getBest(id)) localStorage.setItem(bestKey(id), String(v)); }

  // ---- Yggdrasil procedural backdrop ----
  function initBg(){
    bg = document.getElementById('bg'); bgx = bg.getContext('2d');
    resizeBg();
    for(let i=0;i<70;i++) particles.push(spawn());
    loopBg();
  }
  function spawn(){
    return { x:Math.random()*innerWidth, y:Math.random()*innerHeight,
      vy:-(0.15+Math.random()*0.5), r:0.6+Math.random()*1.8,
      a:0.2+Math.random()*0.6, hue:Math.random()<0.5?C.ice:C.gold };
  }
  function resizeBg(){ bg.width=innerWidth; bg.height=innerHeight; }
  function loopBg(){
    bgx.clearRect(0,0,bg.width,bg.height);
    bgx.fillStyle=C.void; bgx.fillRect(0,0,bg.width,bg.height);
    // faint world-tree trunk
    bgx.strokeStyle='rgba(30,46,69,0.5)'; bgx.lineWidth=2;
    drawBranch(bg.width/2, bg.height, bg.height*0.34, -Math.PI/2, 7);
    for(const p of particles){
      p.y += p.vy; if(p.y< -5){ Object.assign(p, spawn(), {y:bg.height+5}); }
      bgx.globalAlpha=p.a; bgx.fillStyle=p.hue;
      bgx.beginPath(); bgx.arc(p.x,p.y,p.r,0,7); bgx.fill();
    }
    bgx.globalAlpha=1; requestAnimationFrame(loopBg);
  }
  function drawBranch(x,y,len,ang,d){
    if(d<=0||len<6) return;
    const x2=x+Math.cos(ang)*len, y2=y+Math.sin(ang)*len;
    bgx.beginPath(); bgx.moveTo(x,y); bgx.lineTo(x2,y2); bgx.stroke();
    drawBranch(x2,y2,len*0.72,ang-0.35,d-1);
    drawBranch(x2,y2,len*0.72,ang+0.35,d-1);
  }

  // ---- audio (muted default) ----
  function ensureAudio(){ if(!audioCtx) audioCtx = new (window.AudioContext||window.webkitAudioContext)(); }
  function blip(freq=440, dur=0.08, type='sine', vol=0.2){
    if(muted) return; ensureAudio();
    const o=audioCtx.createOscillator(), g=audioCtx.createGain();
    o.type=type; o.frequency.value=freq; g.gain.value=vol;
    o.connect(g); g.connect(audioCtx.destination); o.start();
    g.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime+dur);
    o.stop(audioCtx.currentTime+dur);
  }
  function setMuted(m){ muted=m; }

  // ---- main loop ----
  function startLoop(fn){ onFrame=fn; last=performance.now();
    const tick=(t)=>{ const dt=(t-last)/1000; last=t;
      if(state==='playing' && onFrame) onFrame(dt);
      raf=requestAnimationFrame(tick); };
    raf=requestAnimationFrame(tick);
  }
  function setState(s){ state=s; }

  // ---- end screen ----
  function showEnd(opts){
    setState('lose');
    const el=document.getElementById('stage');
    el.innerHTML = `<div class="panel">
      <h1>${opts.title||'Well Met'}</h1>
      <p>Score <b style="color:var(--gold)">${opts.score}</b>${opts.sub?(' · '+opts.sub):''}</p>
      <div class="lesson">✦ ${opts.lesson}</div>
      <div class="row">
        <a class="btn ghost" href="../${opts.deity}.html">See ${cap(opts.deity)}'s Lesson →</a>
        <a class="btn ice" href="https://blodsson.gumroad.com" target="_blank" rel="noopener">Get The Workflow →</a>
        <button class="btn ghost" id="shareBtn">Share</button>
      </div>
      <div class="row"><button class="btn" id="againBtn">Play Again</button></div>
    </div>`;
    document.getElementById('againBtn').onclick=()=>location.reload();
    document.getElementById('shareBtn').onclick=()=>{ const u=opts.shareCard?opts.shareCard():null;
      if(u) window.open(u,'_blank'); else alert('Share card ready — screenshot this screen!'); };
  }
  function cap(s){ return s.charAt(0).toUpperCase()+s.slice(1); }

  function init(){
    initBg();
    addEventListener('resize', ()=>{ resizeBg(); if(Engine._game&&Engine._game.onResize) Engine._game.onResize(innerWidth,innerHeight); });
    document.addEventListener('visibilitychange', ()=>{
      if(document.hidden && state==='playing'){ /* auto-pause hook */ if(Engine._game&&Engine._game.onHide) Engine._game.onHide(); }
    });
  }
  return { C, init, startLoop, setState, get state(){return state;}, bestKey, getBest, setBest,
    blip, setMuted, showEnd, _game:null };
})();
window.addEventListener('DOMContentLoaded', Engine.init);
