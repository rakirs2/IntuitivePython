import random

TTT_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def choices_condition():
    if player1 == player2:
        print("please input something else")
        input()
        pass
    elif player1 != player2:
        pass
    else:
        print(" redo that no valid input")
        input()


def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def player1wins():
    print('player1 you win \nplayer2 you lose')


def player2wins():
    print('player2 you win \nplayer1 you lose')


def see_if_wins(symbol):
    if ((board[0] == board[1] == board[2] == symbol) or
            (board[3] == board[4] == board[5] == symbol) or
            (board[6] == board[7] == board[8] == symbol) or
            (board[0] == board[3] == board[6] == symbol) or
            (board[1] == board[4] == board[7] == symbol) or
            (board[2] == board[5] == board[8] == symbol) or
            (board[0] == board[4] == board[8] == symbol) or
            (board[2] == board[4] == board[6] == symbol)):
        return True
    else:
        return False


def player1_turn():
    global player1, position
    print('the options are:')
    print(TTT_list)
    player1 = input()
    position = TTT_list.index(player1)
    board[position] = "x"
    print_board()
    TTT_list[position] = " "


def player2_turn():
    global player2, position
    print('the options are:')
    print(TTT_list)
    player2 = random.choice(TTT_list)
    choices_condition()
    position = TTT_list.index(player2)
    board[position] = "o"
    print_board()
    TTT_list[position] = " "

while True:
    print('hello are you wanting to play a game of tic tac toe and make sure to have your own opponent')
    x = input()
    if x == 'no' or x == ' no':
        break
    if x == 'yes' or x == ' yes':
        print('read the dashes from left to right top to bottom and every dash has a number 0-8.')
        print_board()
        player1_turn()
        player2_turn()
        player1_turn()
        player2_turn()
        player1_turn()
        if see_if_wins(symbol='x'):
            player1wins()
            break
        print(TTT_list)
        print('player2 pick between things above with no spaces.')
        player23 = random.choice(TTT_list)
        choices_condition()
        position = TTT_list.index(player23)
        board[position] = "o"
        print_board()
        if see_if_wins(symbol='o'):
            print_board()
            player2wins()
            break
        print(TTT_list)
        print('player1 pick between things above with no spaces.')
        player14 = input()
        choices_condition()
        position = TTT_list.index(player14)
        board[position] = "x"
        print_board()
        if see_if_wins(symbol='x'):
            print_board()
            player1wins()
            break
        print(TTT_list)
        print('player2 pick between things above with no spaces.')
        player24 = random.choice(TTT_list)
        choices_condition()
        position = TTT_list.index(player24)
        board[position] = "o"
        print_board()
        if see_if_wins(symbol='o'):
            print_board()
            player2wins()
            break
        print(TTT_list)
        print('player1 pick between things above with no spaces.')
        player15 = input()
        choices_condition()
        position = TTT_list.index(player15)
        board[position] = "x"
        print_board()
        if see_if_wins(symbol='x'):
            print_board()
            player1wins()
            break
        else:
            print("tie")
            break
