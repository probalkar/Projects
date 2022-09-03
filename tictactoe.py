import os
import time

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player=1

win=1
draw=-1
running=0
stop=1

game=running
mark='X'

#This functions draws game board
def DrawBoard():
    print(" %c | %c | %c " %(board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " %(board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " %(board[7],board[8],board[9]))
    print("   |   |   ")

#This function checks position is empty or not
def CheckPosition(x):
    if(board[x]==' '):
        return True
    else:
        return False

#This function checks player has won or not
def CheckWin():
    global game
    #Horizontal winning condition
    if(board[1]==board[2] and board[2]==board[3] and board[1]!=' '):
        game=win
    elif(board[4]==board[5] and board[5]==board[6] and board[4]!=' '):
        game=win
    elif(board[7]==board[8] and board[8]==board[9] and board[7]!=' '):
        game=win
    
    #Vertical winning condition
    elif(board[1]==board[4] and board[4]==board[7] and board[1]!=' '):
        game=win
    elif(board[2]==board[5] and board[5]==board[8] and board[2]!=' '):
        game=win
    elif(board[3]==board[6] and board[6]==board[9] and board[3]!=' '):
        game=win

    #Diagonal winning condtion
    elif(board[1]==board[5] and board[5]==board[9] and board[5]!=' '):
        game=win
    elif(board[3]==board[5] and board[5]==board[7] and board[5]!=' '):
        game=win

    #Match Tie or Draw condition
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        game=draw
    else:
        game=running

print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
print("Please Wait...")
time.sleep(3)
while(game==running):
    os.system('cls')
    DrawBoard()
    if(player%2!=0):
        print("Player 1's chance")
        mark='X'
    else:
        print("Player 2's chance")
        mark='O'
    choice=int(input("Enter the position beteen [1-9] where you want to mark : "))
    if(CheckPosition(choice)):
        board[choice]=mark
        player+=1
        CheckWin()

os.system('cls')
DrawBoard()
if(game==draw):
    print("Game Draw")
elif(game==win):
    player-=1
    if(player%2!=0):
        print("Player 1 Won")
    else:
        print("Player 2 Won")