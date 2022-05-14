

def print_board(board: list) -> None:
    """Printing of the TicTacToe's board

    Args:
        board (list): list of 9 elements who contain all move of player (X or O)
    """
    print("\n {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} \n".format(board[6], board[7], board[8]))
