"""
  A simple tic-tac-toe game that can be played from the console.
  by: Marco Bislick
  Email: bislick.marcos@gmail.com

"""
import os

##-----------------------------------------------  Variables
fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
player=1
rowfield=-1
columnfield=-1
row=0
column=0
scoreplayer1=0
scoreplayer2=0
playername1=""
playername2=""
roundcounter=0
os.system('cls||clear')
#================================================

# 1 2 3          Game layout
#  | |   1
# -----  
#  | |   2
# -----  
#  | |   3

#-----------------------------------------------  Functions definition
def instructions():
    print("\nThis is a simple game of Tic-Tac-Toe. Please keep in mind that after every round, turns will be inverted and we will keep track of the total game score.\nAlso, you'll be able to choose if you want to continue or end the game.\n")

def game(fields):
    i=0
    u=0
    for row in range(1, 6):
        if row%2==1:
            u+=1
            if row != 5:
                print(u, "", end="")
            else:
                print(u,)
    for row in range(5): #0,1,2,3,4
        if row % 2 == 0: #0,2,4
            temporalrow=int(row/2)
            for column in range(5):
                if column % 2 == 0:
                    temporalcolumn= int(column/2)
                    if column !=4: #0,2
                        print(fields[temporalcolumn][temporalrow], end="")
                    else:
                        i+=1
                        print(fields[temporalcolumn][temporalrow] + "  {}".format(i))
                else:
                    print("|", end="")
        else:
            print("-----")

def fieldassignment(fields, rowfield, columnfield):
    global player
    global column
    global row
    if columnfield==1:
        column=0
    elif columnfield==2:
        column=1
    elif columnfield==3:
        column=2
    if rowfield==1:
        row=0
    elif rowfield==2:
        row=1
    elif rowfield==3:
        row=2
    os.system('cls||clear')
    if player == 1:
        if fields[column][row] == " ":
            fields[column][row] = "X"
            player=2
        else:
            print("\nThe field on row:{} and column:{} is already taken\n".format(columnfield,rowfield))
    elif player == 2:
        if fields[column][row] == " ":
            fields[column][row] = "O"
            player=1
        else:
            print("\nThe field on row:{} and column:{} is already taken\n".format(columnfield,rowfield))
    return fields, player

def inputs(scoreplayer1,scoreplayer2):
    global columnfield
    global rowfield
    global player
    global roundcounter
    if roundcounter%2==0:
        if player == 1:
            print("\n{}'s turn".format(playername1))
        else:
            print("\n{}'s turn".format(playername2))
    elif roundcounter%2==1:
        if player == 1:
            print("\n{}'s turn".format(playername2))
        else:
            print("\n{}'s turn".format(playername1))
    print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
    while columnfield<0 or columnfield>3:
        try:
            columnfield = int(input("\nPlease insert a valid column number: "))
        except:
            continue
    while rowfield<0 or rowfield>3:
        try:
            rowfield = int(input("Please insert a valid row number: "))
        except:
            continue
    return columnfield, rowfield
    
def main(scoreplayer1, scoreplayer2):
    global fields
    global player
    global rowfield
    global columnfield
    global playername1
    global playername2
    global roundcounter
    instructions()
    playername1=input("Please enter a name for player 1 (X)\n")
    playername2=input("Please enter a name for player 2 (O)\n")
    os.system('cls||clear')
    while True:
        game(fields)
        inputs(scoreplayer1, scoreplayer2)
        fieldassignment(fields, rowfield, columnfield)
        rowfield=-1
        columnfield=-1
        if (fields[0][0] + fields[1][0] + fields[2][0]) == "XXX":
            if roundcounter%2==0:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[0][1] + fields[1][1] + fields[2][1]) == "XXX":
            if roundcounter%2==0:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[0][2] + fields[1][2] + fields[2][2]) == "XXX":
            if roundcounter%2==0:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[0][0] + fields[0][1] + fields[0][2]) == "XXX":
            if roundcounter%2==0:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[1][0] + fields[1][1] + fields[1][2]) == "XXX":
            if roundcounter%2==0:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                scoreplayer1+=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[2][0] + fields[2][1] + fields[2][2]) == "XXX":
            if roundcounter%2==0:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                scoreplayer1+=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[2][0] + fields[1][1] + fields[0][2]) == "XXX":
            if roundcounter%2==0:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                scoreplayer1+=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[0][0] + fields[1][1] + fields[2][2]) == "XXX":
            if roundcounter%2==0:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
                scoreplayer1+=1
            else:   
                break
        elif (fields[0][0] + fields[1][0] + fields[2][0]) == "OOO":
            if roundcounter%2==0:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                scoreplayer2+=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[0][1] + fields[1][1] + fields[2][1]) == "OOO":
            if roundcounter%2==0:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[0][2] + fields[1][2] + fields[2][2]) == "OOO":
            if roundcounter%2==0:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[0][0] + fields[0][1] + fields[0][2]) == "OOO":
            if roundcounter%2==0:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[1][0] + fields[1][1] + fields[1][2]) == "OOO":
            if roundcounter%2==0:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[2][0] + fields[2][1] + fields[2][2]) == "OOO":
            if roundcounter%2==0:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[2][0] + fields[1][1] + fields[0][2]) == "OOO":
            if roundcounter%2==0:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
            else:   
                break
        elif (fields[0][0] + fields[1][1] + fields[2][2]) == "OOO":
            if roundcounter%2==0:
                print("{} has won this round".format(playername2))
                scoreplayer2+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            else:
                print("{} has won this round".format(playername1))
                scoreplayer1+=1
                roundcounter+=1
                print("Current game score is:\n{}={}  vs  {}={} ".format(playername1, scoreplayer1, playername2, scoreplayer2))
            instructions()
            playagain=input("Try again? (Y/N)")
            if playagain.lower() == "y":
                fields=[[" "," "," "],[" "," "," "],[" "," "," "]]
                player=1
                os.system('cls||clear')
            else:   
                break
#===============================================
#-----------------------------------------------  Main game
main(scoreplayer1, scoreplayer2)
#===============================================