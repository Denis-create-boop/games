(()=>{
'use strict';
const canvas=document.querySelector('#game'),ctx=canvas.getContext('2d'),nc=document.querySelector('#next'),ng=nc.getContext('2d'),hc=document.querySelector('#hold'),hg=hc.getContext('2d'),hud=document.querySelector('#hud'),pauseButton=document.querySelector('[data-action=pause]');
const shapes=[[[1,1,1,1]],[[1,1],[1,1]],[[0,1,0],[1,1,1]],[[1,0,0],[1,1,1]],[[0,0,1],[1,1,1]],[[0,1,1],[1,1,0]],[[1,1,0],[0,1,1]]],colors=['#5ee1e8','#f5d75d','#b693fa','#658df7','#f5a359','#8de36d','#f47a8a'];
let board,p,next,held,used,score,lines,phase,last=0,elapsed=0,bag,best=0,combo,flash=0;
try{best=Number(localStorage.getItem('arcade-tetris-best'))||0}catch{}
function level(){return 1+Math.floor(lines/10)}
function piece(){if(!bag.length){bag=[0,1,2,3,4,5,6];for(let i=6;i>0;i--){let j=Math.floor(Math.random()*(i+1));[bag[i],bag[j]]=[bag[j],bag[i]]}}return make(bag.pop())}
function make(i){return {id:i,shape:shapes[i].map(r=>r.slice()),color:colors[i],x:Math.floor((10-shapes[i][0].length)/2),y:0}}
function valid(a,x=a.x,y=a.y,s=a.shape){return s.every((r,j)=>r.every((v,i)=>!v||(x+i>=0&&x+i<10&&y+j>=0&&y+j<20&&!board[y+j][x+i])))}
function save(){if(score>best){best=score;try{localStorage.setItem('arcade-tetris-best',String(best))}catch{}}}
function reset(){board=Array.from({length:20},()=>Array(10).fill(null));bag=[];p=piece();next=piece();held=null;used=false;score=lines=elapsed=flash=0;combo=-1;phase='ready';pauseButton.textContent='Старт';draw()}
function start(){if(phase==='ready'||phase==='paused'){phase='running';elapsed=0;pauseButton.textContent='Пауза';draw()}}
function toggle(){if(phase==='over'){reset();start()}else if(phase==='running'){phase='paused';pauseButton.textContent='Продолжить';draw()}else start()}
function advance(){p=next;next=piece();used=false;elapsed=0;if(!valid(p)){phase='over';pauseButton.textContent='Снова';save()}}
function lock(){p.shape.forEach((r,j)=>r.forEach((v,i)=>{if(v)board[p.y+j][p.x+i]=p.color}));let oldLevel=level();board=board.filter(r=>r.some(v=>!v));let n=20-board.length;while(board.length<20)board.unshift(Array(10).fill(null));if(n){combo++;score+=[0,100,300,500,800][n]*oldLevel+50*Math.max(0,combo)*oldLevel;lines+=n;flash=180}else combo=-1;save();advance()}
function down(manual=false){if(valid(p,p.x,p.y+1)){p.y++;if(manual){score++;save()}}else lock();elapsed=0}
function action(a){if(a==='pause'){toggle();return}if(phase==='ready')start();if(phase!=='running')return;
if(a==='left'&&valid(p,p.x-1))p.x--;
if(a==='right'&&valid(p,p.x+1))p.x++;
if(a==='down')down(true);
if(a==='drop'){let n=0;while(valid(p,p.x,p.y+1)){p.y++;n++}score+=2*n;lock()}
if(a==='rotate'){let s=p.shape[0].map((_,i)=>p.shape.map(r=>r[i]).reverse());outer:for(let dy of [0,-1,-2])for(let dx of [0,-1,1,-2,2])if(valid(p,p.x+dx,p.y+dy,s)){p.x+=dx;p.y+=dy;p.shape=s;break outer}}
if(a==='hold'&&!used){let previous=held;held=p.id;if(previous===null){p=next;next=piece()}else p=make(previous);used=true;elapsed=0;if(!valid(p)){phase='over';pauseButton.textContent='Снова';save()}}
draw()}
function cell(g,x,y,col,size=30,ghost=false){if(ghost){g.strokeStyle=col;g.lineWidth=2;g.strokeRect(x*size+4,y*size+4,size-8,size-8);return}g.fillStyle=col;g.fillRect(x*size+1,y*size+1,size-2,size-2);g.fillStyle='#ffffff38';g.fillRect(x*size+3,y*size+3,size-6,5);g.fillStyle='#00000025';g.fillRect(x*size+3,(y+1)*size-7,size-6,4)}
function preview(g,fig){g.fillStyle='#101622';g.fillRect(0,0,120,120);if(!fig)return;let s=24,ox=(120/s-fig.shape[0].length)/2,oy=(120/s-fig.shape.length)/2;fig.shape.forEach((r,y)=>r.forEach((v,x)=>{if(v)cell(g,ox+x,oy+y,fig.color,s)}))}
function draw(){ctx.fillStyle='#101622';ctx.fillRect(0,0,300,600);ctx.strokeStyle='#202b3e';ctx.lineWidth=1;ctx.beginPath();for(let x=0;x<=10;x++){ctx.moveTo(x*30,0);ctx.lineTo(x*30,600)}for(let y=0;y<=20;y++){ctx.moveTo(0,y*30);ctx.lineTo(300,y*30)}ctx.stroke();board.forEach((r,y)=>r.forEach((v,x)=>{if(v)cell(ctx,x,y,v)}));if(phase!=='over'){let gy=p.y;while(valid(p,p.x,gy+1))gy++;p.shape.forEach((r,y)=>r.forEach((v,x)=>{if(v){if(gy!==p.y)cell(ctx,p.x+x,gy+y,p.color,30,true);cell(ctx,p.x+x,p.y+y,p.color)}}))}
if(flash>0){ctx.fillStyle='rgba(183,244,107,'+(flash/180*.13)+')';ctx.fillRect(0,0,300,600)}
if(phase!=='running'){ctx.fillStyle='#101622ba';ctx.fillRect(0,0,300,600);ctx.textAlign='center';ctx.fillStyle='#edf2ff';ctx.font='bold 25px system-ui';ctx.fillText(phase==='over'?'Игра окончена':phase==='paused'?'Пауза':'TETRIS',150,275);ctx.font='15px system-ui';ctx.fillText(phase==='over'?'Пробел — снова':phase==='paused'?'Пробел — продолжить':'Пробел — старт',150,310)}
preview(ng,next);preview(hg,held===null?null:make(held));document.querySelector('#holdbox').classList.toggle('used',used);
const status='Очки: '+score+' · Линии: '+lines+' · Уровень: '+level()+' · Рекорд: '+best+(combo>0?' · Комбо ×'+(combo+1):'');if(hud.textContent!==status)hud.textContent=status;
}
function loop(t){const dt=Math.min(t-last,100);last=t;if(phase==='running'){elapsed+=dt;let changed=flash>0;flash=Math.max(0,flash-dt);if(elapsed>=Math.max(85,750*Math.pow(.82,level()-1))){down();changed=true}if(changed)draw()}requestAnimationFrame(loop)}
document.addEventListener('keydown',e=>{let a={ArrowLeft:'left',ArrowRight:'right',ArrowUp:'rotate',ArrowDown:'down',Enter:'drop',Space:'pause',KeyC:'hold',KeyP:'pause'}[e.code];if(!a||e.target.tagName==='BUTTON')return;e.preventDefault();if(e.repeat&&['pause','hold','drop','rotate'].includes(a))return;action(a)});
document.querySelectorAll('[data-action]').forEach(b=>b.onclick=()=>{action(b.dataset.action);b.blur()});document.querySelector('#restart').onclick=e=>{reset();e.target.blur()};window.addEventListener('blur',()=>{if(phase==='running')toggle()});reset();requestAnimationFrame(loop);
})();