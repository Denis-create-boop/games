import random
import chess
from flask import Blueprint, jsonify, request

bp = Blueprint('chess_api', __name__)
VALUES = {1:100,2:320,3:330,4:500,5:900,6:0}

def evaluate(board):
    value = 0
    for square, piece in board.piece_map().items():
        rank = chess.square_rank(square)
        file = chess.square_file(square)
        center = 7 - abs(3.5-file) - abs(3.5-rank)
        advance = rank if piece.color else 7-rank
        bonus = 6*center if piece.piece_type in (2,3) else 3*advance if piece.piece_type == 1 else 0
        value += (VALUES[piece.piece_type]+bonus)*(1 if piece.color else -1)
    return value if board.turn else -value

def search(board, depth, alpha, beta, ply=0):
    if board.is_checkmate(): return -100000+ply
    if board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves(): return 0
    if depth == 0: return evaluate(board)
    moves = sorted(board.legal_moves, key=lambda m: (board.is_capture(m), bool(m.promotion)), reverse=True)
    best = -1000000
    for move in moves:
        board.push(move)
        score = -search(board, depth-1, -beta, -alpha, ply+1)
        board.pop()
        best = max(best, score)
        alpha = max(alpha, score)
        if alpha >= beta: break
    return best

@bp.post('/api/chess')
def api():
    data = request.get_json(silent=True) or {}
    if not isinstance(data, dict): return jsonify(error='Некорректный запрос'), 400
    history = data.get('moves', [])
    if not isinstance(history,list) or len(history)>600: return jsonify(error='Некорректная партия'),400
    board = chess.Board()
    notation = []
    try:
        for uci in history:
            move = board.parse_uci(uci)
            if not move or board.is_game_over(): raise ValueError()
            notation.append(board.san(move))
            board.push(move)
    except (ValueError, TypeError, AttributeError):
        return jsonify(error='Недопустимый ход'),400
    if data.get('computer') and not board.is_game_over(claim_draw=True):
        difficulty = data.get('difficulty','normal')
        moves = list(board.legal_moves)
        random.shuffle(moves)
        depth = {'easy':1,'normal':2,'hard':3}.get(difficulty,2)
        best = -1000000
        chosen = moves[0]
        for move in moves:
            board.push(move)
            score = -search(board,depth-1,-1000000,-best)
            board.pop()
            if difficulty == 'easy': score += random.randint(-100,100)
            if score > best: best, chosen = score, move
        notation.append(board.san(chosen))
        board.push(chosen)
    outcome = board.outcome(claim_draw=True)
    return jsonify(fen=board.fen(),moves=[m.uci() for m in board.move_stack],notation=notation,
                   legal=[m.uci() for m in board.legal_moves], check=board.is_check(),
                   result=outcome.result() if outcome else None,
                   reason=outcome.termination.name if outcome else None)
