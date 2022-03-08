"""This module does blah blah."""
import random
def choose_first():
    '''
    chooses the player who plays first
    '''
    if random.randint(0, 1) == 0:
        return 'Player 2'
    return 'Player 1'
def change_player(player):
    '''
    give turn to other player
    '''
    if player=='Player 1':
        return 'Player 2'
    return 'Player 1'
def board_input(board):
    '''
    get player's move position
    '''
    i=0
    while i not in [1,2,3,4,5,7,8,9] :
        i=int(input('enter a no 1 to 9\n'))
        if board[i]==' ':
            return i
        i=0
def player_input():
    '''
    lets player chose his/her's tile/marker
    '''
    marker = ''
    while marker not in ('X', 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
def display_board(board):
    '''
    display board
    '''
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def win(board,mark):
    '''
    checks if the player won
    '''
    return (board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[1] == mark and board[2] == mark and board[3] == mark) or (board[7] == mark and board[4] == mark and board[1] == mark) or (board[8] == mark and board[5] == mark and board[2] == mark) or (board[9] == mark and board[6] == mark and board[3] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark) or (board[9] == mark and board[5] == mark and board[1] == mark)
boar1=['0','1','2','3','4','5','6','7','8','9']
boar2=['$',' ',' ',' ',' ',' ',' ',' ',' ',' ']
print('welcome to tic tac toe')
T=input('want to play?(enter y/Y to play)')
while T in ('y','Y'):
    print("welcome players\n\n\n ")
    c=player_input()
    display_board(boar1)
    print("\n\n\n")
    K=1
    display_board(boar2)
    PLAYER=choose_first()
    while K<=9:
        if PLAYER=='Player 1':
            A=0
        else:
            A=1
        boar2[board_input(boar2)]=c[A]
        display_board(boar2)
        if win(boar2,c[A]):
            print(f'{PLAYER} won')
            break
        PLAYER=change_player(PLAYER)
        K+=1
    else:
        print("the game was a draw")
    T=input('want to play again?(enter y/Y to play)')
print('exit')
