(()=>{
'use strict';
const canvas=document.querySelector('#game'), g=canvas.getContext('2d'), hud=document.querySelector('#hud');
const mode=document.querySelector('#difficulty'), startButton=document.querySelector('#dino-start'), pauseButton=document.querySelector('[data-action=pause]');
const W=900,H=380,ground=310,X=80;
const settings={easy:{speed:250,gap:1.8},normal:{speed:310,gap:1.5},hard:{speed:390,gap:1.3}};
const sprites={};
for(const [name,path] of Object.entries({run1:'dino/DinoRun1.png',run2:'dino/DinoRun2.png',jump:'dino/DinoJump.png',duck1:'dino/DinoDuck1.png',duck2:'dino/DinoDuck2.png',cactus:'cactus/LargeCactus1.png',small:'cactus/SmallCactus1.png',cluster:'cactus/LargeCactus2.png',bird1:'birds/Bird1.png',bird2:'birds/Bird2.png'})){const img=new Image();img.src='/assets/dino/'+path;sprites[name]=img}
let state, last=0, duck=false, best=0;
function recordKey(){return 'arcade-dino-best-'+mode.value}
function readBest(){try{return Number(localStorage.getItem(recordKey()))||0}catch{return 0}}
function saveBest(){if(state.score>best){best=Math.floor(state.score);try{localStorage.setItem(recordKey(),String(best))}catch{}}}
function reset(){best=readBest();duck=false;state={phase:'ready',y:0,v:0,jumps:0,score:0,coins:0,time:0,distance:0,spawn:1.2,bonus:7,obstacles:[],items:[],particles:[],shield:false,slow:0,invincible:0};mode.disabled=false;startButton.textContent='Начать игру';pauseButton.textContent='Пауза';updateHud()}
function start(){if(state.phase==='over')reset();if(state.phase==='ready'){state.phase='running';mode.disabled=true;startButton.textContent='Игра идёт';updateHud()}}
function jump(){if(state.phase==='over'||state.phase==='ready'){if(state.phase==='over')reset();start();return}if(state.phase==='running'&&state.jumps<2){state.v=state.jumps===0?650:530;state.jumps++;duck=false;burst(X+24,ground-state.y, '#d5c29f',7)}}
function pause(){if(state.phase==='running'){state.phase='paused';pauseButton.textContent='Продолжить'}else if(state.phase==='paused'){state.phase='running';pauseButton.textContent='Пауза'}updateHud()}
function updateHud(){hud.textContent='Очки: '+Math.floor(state.score)+' · Монеты: '+state.coins+' · Рекорд: '+Math.max(best,Math.floor(state.score))+' · Уровень: '+(1+Math.floor(state.time/20))+(state.shield?' · Щит':'')+(state.slow>0?' · Замедление':'')+(state.phase==='over'?' · Игра окончена':state.phase==='paused'?' · Пауза':'')}
function burst(x,y,color,count=8){for(let i=0;i<count;i++)state.particles.push({x,y,vx:(Math.random()-.5)*160,vy:-Math.random()*130,life:.5,color})}
function spawn(){const types=state.time>12?['small','cactus','cluster','bird']:['small','cactus'];const type=types[Math.floor(Math.random()*types.length)];const sizes={small:[33,43],cactus:[36,65],cluster:[64,65],bird:[58,39]};const [w,h]=sizes[type];state.obstacles.push({type,x:W+30,y:type==='bird'?ground-87:ground-h,w,h});const speed=settings[mode.value].speed+Math.min(state.time*4,250);state.spawn=Math.max(.85,settings[mode.value].gap*settings[mode.value].speed/speed)+Math.random()*.65}
function player(){let crouch=duck&&state.y===0;return{x:X+8,y:ground-state.y-(crouch?38:65)+5,w:crouch?65:45,h:crouch?28:55}}
function intersects(a,b){return a.x<b.x+b.w&&a.x+a.w>b.x&&a.y<b.y+b.h&&a.y+a.h>b.y}
function update(dt){if(state.phase!=='running')return;state.time+=dt;state.score+=dt*10;state.slow=Math.max(0,state.slow-dt);state.invincible=Math.max(0,state.invincible-dt);
const speed=(settings[mode.value].speed+Math.min(state.time*4,250))*(state.slow>0?.58:1);state.distance+=speed*dt;
if(state.y>0||state.v>0){state.v-=1650*dt;state.y=Math.max(0,state.y+state.v*dt);if(!state.y){state.v=0;state.jumps=0}}
state.spawn-=dt;if(state.spawn<=0)spawn();state.bonus-=dt;
if(state.bonus<=0){const r=Math.random();let type=r<.18?'shield':r<.34?'slow':'coin';let y=type==='coin'?(Math.random()<.5?ground-65:ground-150):ground-65;for(let i=0;i<(type==='coin'?3:1);i++)state.items.push({type,x:W+40+i*42,y,w:26,h:26});state.bonus=type==='coin'?2.6+Math.random()*2:9}
for(let o of state.obstacles){o.x-=speed*dt;if(!o.hit&&intersects(player(),{x:o.x+5,y:o.y+5,w:o.w-10,h:o.h-8})){o.hit=true;if(state.shield){state.shield=false;state.invincible=1.1;burst(o.x,o.y,'#77d6ff',18)}else if(!state.invincible){state.phase='over';saveBest();mode.disabled=false;startButton.textContent='Играть снова';break}}}
for(let item of state.items){item.x-=speed*dt;if(!item.hit&&intersects(player(),item)){item.hit=true;if(item.type==='coin'){state.coins++;state.score+=25}else if(item.type==='shield'){state.shield=true}else state.slow=5;burst(item.x,item.y,item.type==='coin'?'#ffd35c':'#80d8f9',12)}}
state.obstacles=state.obstacles.filter(o=>o.x>-100&&!o.hit);state.items=state.items.filter(o=>o.x>-40&&!o.hit);for(let p of state.particles){p.x+=p.vx*dt;p.y+=p.vy*dt;p.vy+=240*dt;p.life-=dt}state.particles=state.particles.filter(p=>p.life>0);updateHud()}
function sprite(name,x,y,w,h){const im=sprites[name];if(im&&im.complete&&im.naturalWidth)g.drawImage(im,x,y,w,h);else{g.fillStyle='#697b66';g.fillRect(x,y,w,h)}}
function circle(x,y,r,color){g.fillStyle=color;g.beginPath();g.arc(x,y,r,0,Math.PI*2);g.fill()}
function mountain(offset,height,color){g.fillStyle=color;g.beginPath();g.moveTo(0,ground);for(let i=-1;i<=7;i++){const x=i*190-offset;g.lineTo(x,ground-40);g.lineTo(x+95,ground-height-(i%2)*24);g.lineTo(x+190,ground-40)}g.lineTo(W,ground);g.closePath();g.fill()}
function draw(t){const night=Math.floor(state.time/25)%2===1;const sky=g.createLinearGradient(0,0,0,H);sky.addColorStop(0,night?'#101a37':'#a6d6e7');sky.addColorStop(1,night?'#40536a':'#f4dfaf');g.fillStyle=sky;g.fillRect(0,0,W,H);circle(740,65,33,night?'#e0e9f8':'#ffe9a1');
if(night){for(let i=0;i<38;i++)circle((i*113+19)%W,(i*47+11)%180,1+(i%3===0), '#dce8ff')}else{g.fillStyle='#ffffff99';for(let i=0;i<5;i++){const x=((i*220-state.distance*.1)%1100+1100)%1100-70;g.beginPath();g.ellipse(x,90+i%2*36,52,15,0,0,Math.PI*2);g.fill()}}
mountain(state.distance*.08%190,145,night?'#34455d':'#b0ba9b');mountain(state.distance*.18%190,80,night?'#293d49':'#869f82');g.fillStyle=night?'#26342f':'#b9a47e';g.fillRect(0,ground,W,H-ground);g.fillStyle=night?'#6b8a80':'#6d805c';g.fillRect(0,ground,W,3);
for(let i=0;i<18;i++){g.fillStyle=night?'#53635a':'#8e815f';g.fillRect(((i*65-state.distance)%1170+1170)%1170,ground+17+i%3*13,12+i%4*4,3)}
const h=duck&&!state.y?38:65;let name=state.y>0?'jump':duck?'duck'+(Math.floor(t/130)%2+1):'run'+(Math.floor(t/120)%2+1);if(!state.invincible||Math.floor(t/90)%2===0)sprite(name,X,ground-state.y-h,duck&&!state.y?78:65,h);
if(state.shield){g.strokeStyle='#75dbff';g.lineWidth=4;g.beginPath();g.arc(X+31,ground-state.y-33,46,0,Math.PI*2);g.stroke()}for(const o of state.obstacles)sprite(o.type==='bird'?'bird'+(Math.floor(t/150)%2+1):o.type,o.x,o.y,o.w,o.h);
for(const item of state.items){circle(item.x+13,item.y+13,13,item.type==='coin'?'#ffd65f':item.type==='shield'?'#63ccf7':'#b6a0ff');g.fillStyle='#253328';g.font='bold 16px system-ui';g.textAlign='center';g.fillText(item.type==='coin'?'★':item.type==='shield'?'S':'T',item.x+13,item.y+19)}
for(const p of state.particles){g.globalAlpha=Math.min(1,p.life*2);circle(p.x,p.y,3,p.color)}g.globalAlpha=1;
if(state.phase!=='running'){g.fillStyle='#101b24bb';g.fillRect(0,0,W,H);g.fillStyle='#f5f9ff';g.textAlign='center';g.font='bold 34px system-ui';g.fillText(state.phase==='over'?'Забег завершён':state.phase==='paused'?'Пауза':'DINO ADVENTURE',W/2,155);g.font='19px system-ui';g.fillText(state.phase==='over'?'Очки: '+Math.floor(state.score)+' · Монеты: '+state.coins:state.phase==='paused'?'P — продолжить':'Нажмите «Начать игру» или пробел',W/2,195)}}
function loop(t){let dt=Math.min((t-last)/1000||0,.035);last=t;update(dt);draw(t);requestAnimationFrame(loop)}
document.addEventListener('keydown',e=>{if(['SELECT','INPUT','TEXTAREA','BUTTON'].includes(e.target.tagName))return;if(['Space','ArrowUp','ArrowDown','KeyP'].includes(e.code)){e.preventDefault();if(e.code==='ArrowDown')duck=true;else if(!e.repeat){if(e.code==='KeyP')pause();else jump()}}});
document.addEventListener('keyup',e=>{if(e.code==='ArrowDown')duck=false});window.addEventListener('blur',()=>{duck=false;if(state.phase==='running')pause()});
document.querySelector('[data-action=jump]').onclick=e=>{jump();e.currentTarget.blur()};const db=document.querySelector('[data-action=duck]');db.onpointerdown=e=>{duck=true;db.setPointerCapture(e.pointerId)};db.onpointerup=db.onpointercancel=db.onlostpointercapture=()=>{duck=false;db.blur()};pauseButton.onclick=e=>{pause();e.currentTarget.blur()};startButton.onclick=e=>{start();e.currentTarget.blur()};document.querySelector('#restart').onclick=e=>{reset();e.currentTarget.blur()};mode.onchange=reset;reset();requestAnimationFrame(loop);
})();
