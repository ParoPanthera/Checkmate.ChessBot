import chess
from yourname_chessbot import ChessBot  # Import your bot

def play_game():
    board = chess.Board()
    bot = ChessBot()

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = bot(board.fen())
        else:
            move = bot(board.fen())

        print(f"Bot Move: {move}")
        board.push(move)
        print(board)

    print("Game Over!")
    bot.calculate_final_score(board)

play_game()
