from include.include import *

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = True

while 1:
    print_board(board)
    move = int(input("Enter your move : "))
    player = move_player(board, move, player)
    if winning_move(board):
        break


print_board(board)
if player:
    print("'O' player won !")
else:
    print("'X' player won !")
