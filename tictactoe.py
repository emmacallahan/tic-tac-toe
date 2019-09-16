print("Let's play Tic-Tac-Toe!")
# board_columns = '   1 2 3'
# board_row_A = '\n A _|_|_'
# board_row_B = '\n B _|_|_'
# board_row_C = '\n C  | | '

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
player_1 = 'X'
player_2 = 'O'
current_player = player_1

def print_board():
    for row in board:
        print(row)

def is_input_valid(row, column):
    if 0 > row or row > 2 or 0 > column or column > 2:
        return False
    return True

def is_space_free(row, column):
    if board[row][column] == ' ':
        return True
    return False

def read_input():
    play_input = input(f'Player {current_player}. Your move: ')
    row, column = play_input.split(' ')
    try:
        row = int(row)
        column = int(column)
    except ValueError:
        print('ILLEGAL MOVE')
        return read_input()
    if not is_input_valid(row, column):
        print('ILLEGAL MOVE')
        return read_input()
    return row, column

def is_there_a_free_space():
    for row in board:
        if ' ' in row:
            return True
    return False

def no_winner():
    for row in board:
        if row[0] != ' ' and row[0] == row[1] == row[2]:
            return False

    for value in range(3):
        if board[0][value] != ' ' and board[0][value] == board[1][value] == board[2][value]:
            return False

    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return False

    if board[2][0] != ' ' and board[2][0] == board[1][1] == board[0][2]:
        return False

    return True

while no_winner() and is_there_a_free_space():
    row, column = read_input()
    while not is_space_free(row, column):
        row, column = read_input()
    board[row][column] = current_player
    print_board()
    current_player = player_1 if current_player == player_2 else player_2
    
current_player = player_1 if current_player == player_2 else player_2
print(f'PLAYER {current_player} WON!')

# def place_player_choice():
#     player_input.lower()
#     if player_input == ['A1','1A']:
#         board_row_A == '\n A X|_|_'
#
# print_board()
#
# player_symbol = 'X'
# player_input = ''
#
# def switch_player_symbol():
#     if player_symbol == 'X':
#         player_symbol == 'O'
#         return player_symbol
#     else:
#         return player_symbol
#
# player_input = input('Player '+player_symbol+', please select a space:')
#
# print(player_input)
#
# switch_player_symbol()
# print(player_input)
# place_player_choice()
# print_board()
# print(player_input)
#2D matirx with one position [[]]

##def check_for_winning_combination():
##    for char in board_vertical_A,board_vertical_B,board_vertical_C:
##       if
