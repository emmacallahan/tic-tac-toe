print("Let's play Tic-Tac-Toe!")
board_columns = '   1 2 3'
board_row_A = '\n A _|_|_'
board_row_B = '\n B _|_|_'
board_row_C = '\n C  | | '

def print_board():
    print(board_columns, board_row_A, board_row_B, board_row_C)

def place_player_choice():
    player_input.lower()
    if player_input == ['A1','1A']:
        board_row_A = '\n A X|_|_'

print_board()

player_symbol = 'X'
player_input = ''

def switch_player_symbol():
    if player_symbol == 'X':
        player_symbol == 'O'
        return player_symbol
    else:
        return player_symbol

player_imput = input('Player '+player_symbol+', please select a space:')

print(player_input)

switch_player_symbol()
print(player_input)
place_player_choice()
print_board()
print(player_input)

##def check_for_winning_combination():
##    for char in board_vertical_A,board_vertical_B,board_vertical_C:
##       if
