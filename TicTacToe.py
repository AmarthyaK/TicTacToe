"""
@author: Pragnay Amarthya
"""




no_of_rows = 11
no_of_columns = 7


displayboard = [[' ' for x in range(no_of_columns)] for x in range(no_of_rows)]
MathBoard = [[0 for x in range(3)] for x in range(3)]
for i in range(0,no_of_columns):
    if i%2==0:
        for j in range(0,no_of_rows):
            displayboard[j][i]='|'
for i in range(0,no_of_rows):
    if i==3 or i==7:
        for j in range(0,no_of_columns):
            displayboard[i][j]='_' 

Disclaimer = [[' ' for x in range(no_of_columns)] for x in range(no_of_rows)]
for i in range(0,no_of_columns):
    if i%2==0:
        for j in range(0,no_of_rows):
            Disclaimer[j][i]='|'
for i in range(0,no_of_rows):
    if i==3 or i==7:
        for j in range(0,no_of_columns):
            Disclaimer[i][j]='_' 

Disclaimer[1][1]=1
Disclaimer[1][3]=2
Disclaimer[1][5]=3
Disclaimer[5][1]=4
Disclaimer[5][3]=5
Disclaimer[5][5]=6
Disclaimer[9][1]=7
Disclaimer[9][3]=8
Disclaimer[9][5]=9
print('Welcome to Tic Tac Toe\n')
print('Player 1 = X, Player 2 = O\n')
print('Have a look at the board along with their respective positions\n')
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in Disclaimer]))
print('Player 1 gets the first chance\n')
def askplayer(player):
    if player>2:
        print('Only two players can play this game, others can watch')
    else:
        pos = input("Enter player %d position: " %(player))
        writeboard(displayboard,player,pos)


def writeboard(displayboard,player,pos):
    pos = int(pos)
    
    if pos>9 or pos < 1:
        print('The position range is only from 1 to 9\n')
        print('Please type again\n')
        askplayer(player)
    
    a=0
    if player==1:
        mark = 'X'
        value=1

    else:
        mark = 'O'
        value= -1
    if pos==1:
        if displayboard[1][1]!=' ':
            print('the place is already occupied')
            a=1
        else:
            displayboard[1][1]=mark
            MathBoard[0][0]=value
    if pos==2:
        if displayboard[1][3]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            displayboard[1][3]=mark
            MathBoard[0][1]=value
    if pos==3:
        if displayboard[1][5]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            displayboard[1][5]=mark
            MathBoard[0][2]=value
    if pos==4:
        if displayboard[5][1]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            displayboard[5][1]=mark 
            MathBoard[1][0]=value
    if pos==5:
        if displayboard[5][3]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            displayboard[5][3]=mark  
            MathBoard[1][1]=value
    if pos==6:
        if displayboard[5][5]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            displayboard[5][5]=mark
            MathBoard[1][2]=value
    if pos==7:
        if displayboard[9][1]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            displayboard[9][1]=mark
            MathBoard[2][0]=value
    if pos==8:
        if displayboard[9][3]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            displayboard[9][3]=mark
            MathBoard[2][1]=value
    if pos==9:
        if displayboard[9][5]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            displayboard[9][5]=mark
            MathBoard[2][2]=value
    if a==1:
        askplayer(player)
    
    pass  
 


def checkwin(MathBoard):
    MathBoardTranspose = [[0 for x in range(3)] for x in range(3)]
    
    for j in range(0,len(MathBoardTranspose)):
        for i in range(0,len(MathBoardTranspose)):
            MathBoardTranspose[i][j] = MathBoard[j][i]
    
    
    for i in range(0,len(MathBoard)):
        summ = sum(MathBoard[i])
        if summ==3:
            return 1
        elif summ==-3:
            return -1
    
    for i in range(0,len(MathBoardTranspose)):
        summ = sum(MathBoardTranspose[i])
        if summ==3:
            return 1
        elif summ==-3:
            return -1
    sumdiag1=0    
    sumdiag2=0
    for i in range(0,len(MathBoard)):
        sumdiag1=sumdiag1+MathBoard[i][i]
        sumdiag2=sumdiag2+MathBoard[i][2-i]
    if sumdiag1==3 or sumdiag2==3:
        return 1
    elif sumdiag1==-3 or sumdiag2==-3:
        return -1

    pass


chance = 1

total_num_chances=1


while total_num_chances<=9:
    askplayer(chance)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in displayboard]))
    win=checkwin(MathBoard)
    if win==1:
        print('Player 1 is the winner,Congratulations!!')
        break
    if win==-1:
        print('Player 2 is the winner,Congratulations!!')
        break
    if chance==1:
        chance=2
    elif chance==2:
        chance=1
    total_num_chances=total_num_chances+1
    if total_num_chances==10:
        print('Its a tie')
    
               
