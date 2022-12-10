import random
while True: 
    player2 = None
    rpslist =  ["rock","paper","scissors"]
    print("Do you want to play a game of rock paper scissors yes or no")
    y=input()
    if y==('yes'):
        print('pick between rock,paper,or scissors')
    if y==('no'):
        break
    player1=input()

    if player1 in rpslist:
        player2 = random.choice(rpslist)
        print(player2)   

    if player2==('rock') and player1==('rock'):
        print('tie')
    if player2==('paper') and player1==('rock'):
        print('player 2 wins')
    if player2==('rock') and player1==('rock'):
        while False:
            'break'
