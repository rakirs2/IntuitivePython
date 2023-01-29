x = input('hello your are wanting to play a game of tic tac toe and make sure to have your own oppenent')
if x=='no'or ' no':
    'break'
if x=='yes'or ' yes':    
    print(' a     b     c')     
    print('1  -  |  -  |  - ') 
    print(' _____|_____|_____')     
    print('2  -  |  -  |  -')  
    print(' _____|_____|_____')     
    print('3  -  |  -  |  -')  
    print('      |     |     ')  
    player1 = input(' player1/x pick between A1, A2, A3, B1, B2, B3, C1, C2, C3')
    print(player1)
    player2 = input('now player2/o pick between A1, A2, A3, B1, B2, B3, C1, C2, C3 but do not pick the same anwser')
    print(player2)
    player1 = input(' player1/x pick between A1, A2, A3, B1, B2, B3, C1, C2, C3')
    
    print(player1)
    player2 = input('now player2/o pick between A1, A2, A3, B1, B2, B3, C1, C2, C3 but do not pick the same anwser')
    
    print(player2)
    player1 = input(' player1/x pick between A1, A2, A3, B1, B2, B3, C1, C2, C3')
    
    print(player1)
    player2 = input('now player2/o pick between A1, A2, A3, B1, B2, B3, C1, C2, C3 but do not pick the same anwser')
    
    print(player2)
    p1=input('player1 please enter all your past entrees please do not add spaces')
    p2=input('now player2 please enter all your past entrees please do not add spaces')
    if p1==["A1A2A3"]:
        print('player1 you win!')
        print('player2 you lose')
        'break'
    if p1==["A1B2C3"]:
        print('player1 you win!')
        print('player2 you lose')
        'break'

    if p1==["A1B1C1"]:
        print('player1 you win!')
        print('player2 you lose')
        'break'

    if p1==["B1B2B3"]:
        print('player1 you win!')
        print('player2 you lose')
        'break'

    if p1==["C1C2C3"]:
        print('player1 you win!')
        print('player2 you lose')
        'break'
    
    if p1==["C1B2A3"]:
        print('player1 you win!')
        print('player2 you lose')
        'break'
    if p2==["A1A2A3"]:
        print('player2 you win!')
        print('player1 you lose')
        'break'
    
    if p2==["A1B2C3"]:
        print('player2 you win!')
        print('player1 you lose')
        'break'
    if p2==["A1B1C1"]:
        print('player2 you win!')
        print('player1 you lose')
        'break'
    if p2==["B1B2B3"]:
        print('player2 you win!')
        print('player1 you lose')
        'break'
    if p2==["C1C2C3"]:
        print('player2 you win!')
        print('player1 you lose')
        'break'
    if p2==["C1B2A3"]:
        print('player2 you win!')
    print('player1 you lose')
    'break'
else:
        print('tie')    
