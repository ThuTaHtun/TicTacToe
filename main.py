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


def horizontal(board: dict) -> bool:
    i = 1
    while i <= 7:
        if board[i] == board[i + 1] == board[i + 2]:
            return True
        else:
            i += 3
    return False


def vertical(board: dict) -> bool:
    i = 1
    while i <= 3:
        if board[i] == board[i + 3] == board[i + 6]:
            return True
        else:
            i += 1
    return False


def diagonal(board: dict) -> bool:
    i = 5
    if board[i] == board[i - 4] == board[i + 4]:
        return True
    elif board[i] == board[i - 2] == board[i + 2]:
        return True
    else:
        return False


def win(board: dict) -> bool:
    if horizontal(board) or vertical(board) or diagonal(board):
        return True
    else:
        return False


while move < 9:
    if turn:
        print("\nPlayer 1's turn!")
    else:
        print("\nPlayer 2's turn!")

    user_input = input('Where do you want to place your symbol?'
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

