board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
move = 0
turn = True


def draw_board(board: dict) -> str:
    display = '\n|'
    for key in board:
        if key < 9 and key % 3 == 0:
            display += f" {board[key]} |\n|"
        else:
            display += f" {board[key]} |"
    return display


def horizontal(board: dict) -> int:
    i = 1
    while i <= 7:
        if board[i] == board[i + 1] == board[i + 2] == 'O':
            return 1
        elif board[i] == board[i + 1] == board[i + 2] == 'X':
            return 2
        else:
            i += 3
    return 0


def vertical(board: dict) -> int:
    i = 1
    while i <= 3:
        if board[i] == board[i + 3] == board[i + 6] == 'O':
            return 1
        elif board[i] == board[i + 3] == board[i + 6] == 'X':
            return 2
        else:
            i += 1
    return 0


def diagonal(board: dict) -> int:
    i = 5
    if board[i] == board[i - 4] == board[i + 4] == 'O' or board[i] == board[i - 2] == board[i + 2] == 'O':
        return 1
    elif board[i] == board[i - 4] == board[i + 4] == 'X' or board[i] == board[i - 2] == board[i + 2] == 'X':
        return 2
    else:
        return 0


def win(board: dict) -> int:
    if horizontal(board) == 1 or vertical(board) == 1 or diagonal(board) == 1:
        return 1
    elif horizontal(board) == 2 or vertical(board) == 2 or diagonal(board) == 2:
        return 2
    else:
        return 0


while move < 9:
    if win(board) == 1:
        print("Player 1 wins!")
        break
    if win(board) == 2:
        print("Player 2 wins!")
        break

    if turn:
        print("\nPlayer 1's turn!")
    else:
        print("\nPlayer 2's turn!")

    user_input = input('Where do you want to place your symbol? '
                       '\nEach number corresponds to the tile they reside in.'
                       '\n| 1 | 2 | 3 |'
                       '\n| 4 | 5 | 6 |'
                       '\n| 7 | 8 | 9 |'
                       '\nPlease enter a number from 1 to 9: ')

    if int(user_input) not in range(1, 10):
        print("\nInvalid input! Please choose a number from 1 to 9.")
        continue

    if turn:
        if int(user_input) in range(1, 10) and board[int(user_input)] == " ":
            board[int(user_input)] = 'O'
        else:
            print("\nTile already taken! Please choose another tile.")
            board[int(user_input)] = board[int(user_input)]
            move -= 1
            turn = not turn

    else:
        if int(user_input) in range(1, 10) and board[int(user_input)] == " ":
            board[int(user_input)] = 'X'
        else:
            print("\nTile already taken! Please choose another tile")
            board[int(user_input)] = board[int(user_input)]
            move -= 1
            turn = not turn

    print(draw_board(board))
    turn = not turn
    move += 1

if move == 9 and not win(board):
    print("The game ends in a draw!")