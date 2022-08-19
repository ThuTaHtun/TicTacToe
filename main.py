board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
move = 0
turn = True


def draw_board(board: dict) -> str:
    display = '|'
    for key in board:
        if key < 9 and key % 3 == 0:
            display += f" {board[key]} |\n|"
        else:
            display += f" {board[key]} |"
    return display


while move < 9:
    if turn:
        print("\nPlayer 1's turn!")
        user_input = input('Where do you want to place your symbol?'
                           '\n 1 | 2 | 3 '
                           '\n 4 | 5 | 6 '
                           '\n 7 | 8 | 9 '
                           '\n Please enter the number of your choice: ')
        board[int(user_input)] = 'O'
        print(draw_board(board))
    else:
        print("\nPlayer 2's turn!")
        user_input = input('Where do you want to place your symbol?'
                           '\n 1 | 2 | 3 '
                           '\n 4 | 5 | 6 '
                           '\n 7 | 8 | 9 '
                           '\n Please enter the number of your choice: ')
        board[int(user_input)] = 'X'
        print(draw_board(board))

    turn = not turn
    move += 1

