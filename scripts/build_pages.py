from pathlib import Path
import shutil
import re
from app import app, GAMES
root=Path(__file__).resolve().parents[1]
out=root/"site"
if out.exists(): shutil.rmtree(out)
out.mkdir()
shutil.copytree(root/"static",out/"static")
shutil.copytree(root/"Dino"/"images",out/"assets"/"dino")
with app.test_client() as client:
    for route in ["/"]+["/play/"+g for g in GAMES]:
        response=client.get(route)
        assert response.status_code==200
        html=response.get_data(as_text=True)
        def rewrite(m):
            attr,path=m.groups()
            return f'{attr}="/games{path}'+('' if path.startswith('/static/') or path.endswith('/') else '/')+'"'
        html=re.sub(r'(href|src)="(/(?!/)[^"]*)"',rewrite,html)
        dest=out/route.strip("/")/"index.html"
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(html,encoding="utf-8")
dino=out/"static"/"dino.js"
dino.write_text(dino.read_text(encoding="utf-8").replace("'/assets/dino/'","'/games/assets/dino/'"),encoding="utf-8")
chess=out/"static"/"chess.js"
source=chess.read_text(encoding="utf-8")
start=source.index("async function call(")
end=source.index("\nasync function sync(",start)
source='import { browserChess } from "./chess_browser.js";\n'+source[:start]+'''async function call(moves,computer=false){return browserChess(moves,computer,activeDifficulty)}'''+source[end:]
chess.write_text(source,encoding="utf-8")
(out/".nojekyll").touch()
