# turn(), line 120 has the try except block

def draw_board(row, col):
    print('\n')
    for r in range(row):
        border = 0
        for c in range(col):
            if c == 0:
                print(f"        \033[{get_color_code(SQUARES[r][c])} {SQUARES[r][c]} \033[49m|", end='')
            elif c != col-1:
                print(f"\033[{get_color_code(SQUARES[r][c])} {SQUARES[r][c]} \033[49m|", end='')
                border += 1
            else:
                print(f"\033[{get_color_code(SQUARES[r][c])} {SQUARES[r][c]} \033[49m ")
        if r != row -1:
            print("        --" + "-----" * border)
    print("\n")

def get_color_code(symbol):
    if symbol == "X":
        return "45m"
    elif symbol == "O":
        return "46m"
    else:
        return "39m"


def take_square(col,symbol):
    if SQUARES[0][col] != "~":
        print(f"     TRY ANOTHER ROW, {symbol}!")
        return False
    for row in range(5,-1,-1):
        if SQUARES[row][col] == "~":
            SQUARES[row][col] = symbol
            draw_board(6,7)
            return row


def check_for_win(row, square, symbol):
    check_diagnal(row,square,symbol)
    if check_vertical(row,square,symbol) \
    or check_horizontal(row, square, symbol) \
    or check_diagnal(row,square,symbol):
        return True


def check_horizontal(row, square, symbol):
    row_str = ''.join(SQUARES[row])
    if symbol*4 in row_str:
        return True
    return False


def check_vertical(row,square,symbol):
    if row > 2:
        return False
    if SQUARES[row + 1][square] == symbol \
    and SQUARES[row + 2][square] == symbol \
    and SQUARES[row + 3][square] == symbol:
        return True
    return False


def check_diagnal(row,square,symbol):
    total = 1

    # down and left
    x = row + 1
    y = square - 1
    while x <= 5 and y >= 0:
        if SQUARES[x][y] == symbol:
            total += 1
            x += 1
            y -= 1
        else:
            break

    # up right
    x = row - 1
    y = square + 1
    while y <= 6 and x >= 0:
        if SQUARES[x][y] == symbol:
            total += 1
            x -= 1
            y += 1
        else:
            break
    if total >= 4:
        return True

    # reset
    total = 1

    # up and left
    x = row - 1
    y = square - 1
    while x >= 0 and y >= 0:
        if SQUARES[x][y] == symbol:
            total += 1
            x -= 1
            y -= 1
        else:
            break

    # down and right
    x = row + 1
    y = square + 1
    while y <= 6 and x <= 5:
        if SQUARES[x][y] == symbol:
            total += 1
            x += 1
            y += 1
        else:
            break
    if total >= 4:
        return True
    else:
        return False

def turn(symbol):
    while True:
        user_input = input(f"     GOOD LUCK, {symbol}!   ")
        if user_input in ['q', 'quit', 'e', 'exit']:
            exit()
        try:
            int(user_input)
            if(int(user_input) < 1 or int(user_input) > 7):
                raise ValueError
            return int(user_input) - 1
        except ValueError:
            print(f"     OH NO! {symbol}, Please enter a number 1-7 to play a column")
        except Exception as e:
            print("There was a problem with your input: ", e)
    

def game():
    print('''
      _________  _  ___  _____________________
     / ___/ __ \/ |/ / |/ / __/ ___/_  __/ / /
    / /__/ /_/ /    /    / _// /__  / / /_  _/
    \___/\____/_/|_/_/|_/___/\___/ /_/   /_/  

    ''')
    print("   Enter a number 1-7 to play a column.")
    print("   The first player to 4 in a row wins!")
    print("   Enter \"quit\" or \"exit\" to end the game.")
    TURNS=1
    draw_board(6,7)

    while True:
        symbol = "O" if TURNS % 2 == 0 else "X"
        row = False
        square = False
        while not row:
            symbol = "O" if TURNS % 2 == 0 else "X"
            square = turn(symbol)
            row = take_square(square, symbol)
        if check_for_win(row,square,symbol):
            print(f"     {symbol} WINS!")
            break
        TURNS += 1

SQUARES = [
    ['~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~'],
    ['~', '~', '~', '~', '~', '~', '~']
]

game()
