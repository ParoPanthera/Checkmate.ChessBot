import chess
import random
from abc import ABC, abstractmethod

PIECE_VALUES = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}
BONUS_ATTACK = 3
BONUS_DEFENSE = 1
CHECK_BONUS = 5


class ChessBotClass(ABC):
    @abstractmethod
    def __call__(self, board_fen: str) -> chess.Move:
        pass


class ChessBot(ChessBotClass):
    def __init__(self):
        self.previous_moves = set()

    def evaluate_move(self, board: chess.Board, move: chess.Move) -> int:
        score = 0
        if board.is_capture(move):
            captured_piece = board.piece_at(move.to_square)
            score += PIECE_VALUES.get(captured_piece.piece_type, 0) + BONUS_ATTACK if captured_piece else 0
        if board.gives_check(move):
            score += CHECK_BONUS
        return score

    def __call__(self, board_fen: str) -> chess.Move:
        board = chess.Board(board_fen)
        legal_moves = list(board.legal_moves)
        if not legal_moves:
            return random.choice(legal_moves)

        best_move = max(legal_moves, key=lambda move: self.evaluate_move(board, move),
                        default=random.choice(legal_moves))

        move_uci = best_move.uci()
        if move_uci in self.previous_moves:
            alternative_moves = [m for m in legal_moves if m.uci() not in self.previous_moves]
            if alternative_moves:
                best_move = max(alternative_moves, key=lambda move: self.evaluate_move(board, move), default=best_move)

        self.previous_moves.add(best_move.uci())
        return best_move
