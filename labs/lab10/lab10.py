"""
Name: Robert Stenback
TicTacToe.py
"""
def build():
    x = [1,2,3,4,5,6,7,8,9]
    return x

def display(board):
    print(board[0],'|', board[1], '|', board[2],
          '\n', '-------')
    print(board[3], '|', board[4], '|', board[5],
          '\n', '-------')
    print(board[6], '|', board[7], '|', board[8])

def fill_spot(board, pos, char):
    if is_legal(board, pos) is True:
        board[pos] = char
    else:
        print('this spot is already taken')

def is_legal(board, pos):
    if type(board[pos]) is int:
        return True
    else:
        return False

def play_game():
    x = build()
    display(x)
    char = 'X'
    while game_over(x, char) == False:
        p1_move = 'a'
        while p1_move == 'a':
            try:
                p1_move = eval(input('Player ' + char + ', which spot would you like? [enter a number]:'))
            except:
                print('Please enter a number')
        pos = p1_move - 1
        is_legal(x, pos)
        fill_spot(x, pos, char)
        display(x)
        if game_won(x, char) == True:
            print(char + ' wins!!')
            break
        game_over(x, char)
        if char == 'X':
            char = 'O'
        else:
            char = 'X'


def game_won(board, char):
    if board[0:3] == [char, char, char]:
        return True
    elif board[3:6] == [char, char, char]:
        return True
    elif board[6:9] == [char, char, char]:
        return True
    elif board[0:9:4] == [char, char, char]:
        return True
    elif board[2:9:2] == [char, char, char]:
        return True
    elif board[0::3] == [char, char, char]:
        return True
    elif board[1::3] == [char, char, char]:
        return True
    elif board[2::3] == [char, char, char]:
        return True
    else:
        return False

def game_over(board, char):
    acc = 0
    for _ in board:
        if _ == 'X' or _ == 'O':
            acc = acc + 1
    if game_won(board, char) == True:
        return True
    elif acc == 9:
        print('the board is full, no winner')
        return True
    else:
        return False





def main():
    play_game()
    pass


main()
