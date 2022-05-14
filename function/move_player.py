from time import sleep


def move_player(board: list, move: int, player: bool) -> bool:
    if board[move - 1] == ' ':
        if player:
            board[move - 1] = 'X'
            return False
        else:
            board[move - 1] = 'O'
            return True
    else:
        print("\nWrong move, try again !\n")
        sleep(1)
        return player
