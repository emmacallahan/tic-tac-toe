print("Let's play Tic-Tac-Toe!")
board_columns = '   1 2 3'
board_row_A = '\n A _|_|_'
board_row_B = '\n B _|_|_'
board_row_C = '\n C  | | '

def print_board():
    print(board_columns, board_row_A, board_row_B, board_row_C)

print_board()
player_symbol = 'O'
def switch_player_symbol(player_symbol):
    if player_symbol == 'O':
        player_symbol == 'X'
        return player_symbol
    else:
        return player_symbol



print(player_symbol)

print('Player '+player_symbol+', please select a space:')
switch_player_symbol(player_symbol)
print('Player '+player_symbol+', please select a space:')

##def check_for_winning_combination():
##    for char in board_vertical_A,board_vertical_B,board_vertical_C:
##       if
