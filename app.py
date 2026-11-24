from pathlib import Path
from flask import Flask, render_template, abort, send_from_directory
app = Flask(__name__)
ROOT = Path(__file__).resolve().parent
GAMES = {
    'dino': {'name':'Dino', 'icon':'🦖', 'description':'Перепрыгивайте препятствия и набирайте очки.', 'controls':'Пробел / ↑ — прыжок, ↓ — пригнуться.'},
    'tetris': {'name':'Tetris', 'icon':'🧩', 'description':'Собирайте линии из падающих фигур.', 'controls':'← → — движение, ↑ — поворот, ↓ — вниз, Enter — сброс, пробел — пауза.'},
    'slot': {'name':'Slot', 'icon':'🎰', 'description':'Аркадная имитация игровых барабанов с виртуальными очками.', 'controls':'Нажмите «Вращать». Только виртуальные очки, без денег.'},
}
@app.get('/')
def index():
    return render_template('index.html', games=GAMES)
@app.get('/play/<game>')
def play(game):
    if game not in GAMES:
        abort(404)
    return render_template('play.html', game=game, info=GAMES[game])
@app.get('/assets/<game>/<path:filename>')
def assets(game, filename):
    dirs = {'dino': ROOT/'Dino'/'images', 'slot': ROOT/'slot'/'img1'}
    if game not in dirs:
        abort(404)
    return send_from_directory(dirs[game], filename)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
