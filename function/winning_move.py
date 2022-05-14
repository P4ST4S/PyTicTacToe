def winning_move(board: list) -> bool:
    if (board[0] == board[1] == board[2] != ' ') or \
        (board[3] == board[4] == board[5] != ' ') or \
            (board[6] == board[7] == board[8] != ' ') or \
            (board[0] == board[4] == board[8] != ' ') or \
            (board[2] == board[4] == board[6] != ' '):
        return True
