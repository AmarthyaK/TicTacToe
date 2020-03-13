# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:42:38 2020

@author: Pragnay Amarthya
"""




nor = 11
noc = 7


db = [[' ' for x in range(noc)] for x in range(nor)]
wb = [[0 for x in range(3)] for x in range(3)]
for i in range(0,noc):
    if i%2==0:
        for j in range(0,nor):
            db[j][i]='|'
for i in range(0,nor):
    if i==3 or i==7:
        for j in range(0,noc):
            db[i][j]='_' 

dbf = [[' ' for x in range(noc)] for x in range(nor)]
for i in range(0,noc):
    if i%2==0:
        for j in range(0,nor):
            dbf[j][i]='|'
for i in range(0,nor):
    if i==3 or i==7:
        for j in range(0,noc):
            dbf[i][j]='_' 

dbf[1][1]=1
dbf[1][3]=2
dbf[1][5]=3
dbf[5][1]=4
dbf[5][3]=5
dbf[5][5]=6
dbf[9][1]=7
dbf[9][3]=8
dbf[9][5]=9
print('Welcome to Tic Tac Toe\n')
print('Player 1 = X, Player 2 = O\n')
print('Have a look at the board along with their respective positions\n')
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in dbf]))
print('Player 1 gets the first chance\n')
def askplayer(player):
    if player>2:
        print('Only two players can play this game, others can watch')
    else:
        pos = input("Enter player %d position: " %(player))
        writeboard(db,player,pos)


def writeboard(db,player,pos):
    pos = int(pos)
    
    if pos>9 or pos < 1:
        print('The position range is only from 1 to 9\n')
        print('Please type again\n')
        askplayer(player)
    
    a=0
    if player==1:
        mark = 'X'
        val=1

    else:
        mark = 'O'
        val = -1
    if pos==1:
        if db[1][1]!=' ':
            print('the place is already occupied')
            a=1
        else:
            db[1][1]=mark
            wb[0][0]=val
    if pos==2:
        if db[1][3]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            db[1][3]=mark
            wb[0][1]=val
    if pos==3:
        if db[1][5]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            db[1][5]=mark
            wb[0][2]=val
    if pos==4:
        if db[5][1]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            db[5][1]=mark 
            wb[1][0]=val
    if pos==5:
        if db[5][3]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            db[5][3]=mark  
            wb[1][1]=val
    if pos==6:
        if db[5][5]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            db[5][5]=mark
            wb[1][2]=val
    if pos==7:
        if db[9][1]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            db[9][1]=mark
            wb[2][0]=val
    if pos==8:
        if db[9][3]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            db[9][3]=mark
            wb[2][1]=val
    if pos==9:
        if db[9][5]!=' ':
            print('the place is already occupied')
            a=1            
        else:
            db[9][5]=mark
            wb[2][2]=val
    if a==1:
        askplayer(player)
    
    pass  
 


def checkwin(wb):
    wbt = [[0 for x in range(3)] for x in range(3)]
    
    for j in range(0,len(wbt)):
        for i in range(0,len(wbt)):
            wbt[i][j] = wb[j][i]
    
    
    for i in range(0,len(wb)):
        summ = sum(wb[i])
        if summ==3:
            return 1
        elif summ==-3:
            return -1
    
    for i in range(0,len(wbt)):
        summ = sum(wbt[i])
        if summ==3:
            return 1
        elif summ==-3:
            return -1
    sumdiag1=0    
    sumdiag2=0
    for i in range(0,len(wb)):
        sumdiag1=sumdiag1+wb[i][i]
        sumdiag2=sumdiag2+wb[i][2-i]
    if sumdiag1==3 or sumdiag2==3:
        return 1

    pass


i = 1

total_num_chances=1


while total_num_chances<=9:
    askplayer(i)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in db]))
    win=checkwin(wb)
    if win==1:
        print('Player 1 is the winner,Congratulations!!')
        break
    if win==-1:
        print('Player 2 is the winner,Congratulations!!')
        break
    if i==1:
        i=2
    elif i==2:
        i=1
    total_num_chances=total_num_chances+1
    if total_num_chances==10:
        print('Its a tie')
    
               
