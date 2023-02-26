import random
# while True:








player1score=0
player2score=0     
rpslist =  ["rock","paper","scissors"]
while True:
    # get player input
    print('pick between rock,paper,or scissors')
    player1=input()

    # create player 2
    player2 = random.choice(rpslist)
    print('your choice: '+player1+'\ncomputer choice: '+player2)   
    # check and update score
    if player1==player2:
        print('tie')
    # player1 wins
    elif(player1=='paper' and player2=='rock' or player1=='rock' and player2=='scissors' or player1=='scissors' and player2=='paper'):
        player1score +=1
        # computer wins
    elif(player1=='rock' and player2=='paper' or player1=='scissors' and player2=='rock' or player1=='paper' and player2=='scissors'):
        player2score +=1
    # print score

    print('your score: '+str(player1score)+'\ncomputer score: '+str(player2score))
    c=input('do you want to end')
    if c=='yes' or c==" yes":
        break