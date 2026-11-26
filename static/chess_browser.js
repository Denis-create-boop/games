import { Chess } from "./vendor/chess.js";
const value={p:100,n:320,b:330,r:500,q:900,k:0};
const uci=m=>m.from+m.to+(m.promotion||"");
function evaluate(b){let score=0;for(const row of b.board())for(const p of row)if(p)score+=value[p.type]*(p.color==="w"?1:-1);return score*(b.turn()==="w"?1:-1)}
function search(b,depth,alpha,beta,ply=0){
 if(b.isCheckmate())return -100000+ply;
 if(b.isDraw())return 0;
 if(!depth)return evaluate(b);
 let best=-Infinity;
 for(const m of b.moves({verbose:true}).sort((a,b)=>Number(!!b.captured)-Number(!!a.captured))){
  b.move(m.san);let score=-search(b,depth-1,-beta,-alpha,ply+1);b.undo();best=Math.max(best,score);alpha=Math.max(alpha,score);if(alpha>=beta)break;
 }
 return best;
}
export async function browserChess(moves,computer=false,difficulty="normal"){
 const b=new Chess();
 for(const m of moves)b.move({from:m.slice(0,2),to:m.slice(2,4),promotion:m[4]});
 if(computer&&!b.isGameOver()){
  await new Promise(r=>setTimeout(r,20));
  const depth={easy:1,normal:2,hard:3}[difficulty]||2;
  let best=-Infinity,chosen=null;
  for(const m of b.moves({verbose:true})){
   b.move(m.san);let score=-search(b,depth-1,-Infinity,-best);b.undo();
   if(difficulty==="easy")score+=Math.random()*200-100;
   if(score>best){best=score;chosen=m}
  }
  if(chosen)b.move(chosen.san);
 }
 let result=null,reason=null;
 if(b.isCheckmate()){result=b.turn()==="w"?"0-1":"1-0";reason="CHECKMATE"}
 else if(b.isDraw()){result="1/2-1/2";reason=b.isStalemate()?"STALEMATE":b.isInsufficientMaterial()?"INSUFFICIENT_MATERIAL":b.isThreefoldRepetition()?"THREEFOLD_REPETITION":"FIFTY_MOVES"}
 return {fen:b.fen(),moves:b.history({verbose:true}).map(uci),notation:b.history(),legal:b.moves({verbose:true}).map(uci),check:b.isCheck(),result,reason};
}
