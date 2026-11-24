from pathlib import Path
from flask import Flask, render_template, abort, send_from_directory
from chess_api import bp
app = Flask(__name__)
app.register_blueprint(bp)
ROOT = Path(__file__).resolve().parent
GAMES = {
    'dino': {'name':'Dino', 'icon':'🦖', 'description':'Бегите через сменяющиеся пейзажи, собирайте монеты и бонусы.', 'controls':'Пробел / ↑ — двойной прыжок, ↓ — пригнуться, P — пауза.'},
    'tetris': {'name':'Tetris', 'icon':'🧩', 'description':'Собирайте линии, используйте удержание фигур и улучшайте рекорд.', 'controls':'← → движение · ↑ поворот · ↓ вниз · Enter сброс · C удержание · Пробел / P старт и пауза.'},
    'chess': {'name':'Chess 3D', 'icon':'♞', 'description':'Объёмные шахматы: три уровня сложности и разные стили.', 'controls':'Выберите фигуру и клетку назначения.'},
}
@app.get('/')
def index():
    return render_template('index.html', games=GAMES)
@app.get('/play/<game>')
def play(game):
    if game not in GAMES:
        abort(404)
    return render_template('chess.html' if game == 'chess' else 'play.html', game=game, info=GAMES[game])
@app.get('/assets/<game>/<path:filename>')
def assets(game, filename):
    dirs = {'dino': ROOT/'Dino'/'images'}
    if game not in dirs:
        abort(404)
    return send_from_directory(dirs[game], filename)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
