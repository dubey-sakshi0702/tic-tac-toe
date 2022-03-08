import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
def change_player(player):
    if player=='Player 1':
        return 'Player 2'
    else:
        return 'Player 1'
def board_input(board):
    i=0
    while i not in [1,2,3,4,5,7,8,9]:
        i=int(input('enter a no 1 to 9\n'))
        if board[i]==' ':
            return i
        else:
            continue
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
def display_board(board):

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
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 
boar1=['0','1','2','3','4','5','6','7','8','9']
boar2=['$',' ',' ',' ',' ',' ',' ',' ',' ',' ']

print('welcome to tic tac toe')
t=input('want to play?(enter y/Y to play)')
if t=='y' or t== 'Y':
    print("welcome players\n\n\n ")
c=player_input()
display_board(boar1)
print("\n\n\n")
t=1
display_board(boar2)
player=choose_first()

while t<9:
    if player=='Player 1':
        a=0
    else:
        a=1
    y=board_input(boar2)
    boar2[y]=c[a]
    display_board(boar2)
    if win(boar2,c[a])==True:
       print(f'{player} won')
       break
    player=change_player(player)