
#warning this code is made by beginners and any small changes will result in poor execution/ multiple errors
print('''Over the cerulean sea, you and your mate are setting asail, trying to escape from the grasp of the British Navy ship, under her Royal Majesty order, Queen Petunia.
Ain't nothing more sinner-est than stealing from Petunia's booty locked under the so-called secured bank in London.Titled in bold on the front cover of News Straight Times,
your crew the Bootleg has once strike again being featured in the monthly newspaper spread more famous than Queen Petunia's fancy wardrobe show.''')

import random

def display(): #prints column numbers
    i = 1
    while i <= 6:
        if i == 6:
            print ((" "*9), i, sep="")
            i += 1
        else:
            print ((" "*9), i, sep="", end="")
            i += 1

    num = 1
    i = 1
    while i <= 60:
        if i == 60:
            num = 0
            print (num,sep="")
        elif num == 10:
            num = 0
            print (num,end="")
        else:
            print (num,end="")
        num += 1
        i += 1

def board(ship,prob): #argument 1: number of ships in chosen game mode, argument 2: probability of ship appearing in each row

    board = []
    row = 1
    probability = prob
    ships = ship

    while row <= 20:
        rowBoard = []
        column = 1
        while column <= 60:
            surprise = random.choice(probability)
            if ship == 0:
                rowBoard.append(0)  #continue appending "empty spots" after all ships have been spawned
                column += 1
            else:
                if surprise >= 1 and surprise <= 4 and surprise in rowBoard:
                    column = column #skip 
                else:
                    if surprise == 0:
                        rowBoard.append(surprise)
                        column += 1
                    else:
                        if surprise >= 1 and surprise <= 4:
                            for i in range(5):
                                rowBoard.append(surprise)
                        column += 5
                        ship -= 1

        board.append(rowBoard)
        row += 1

####################display########################
    displayBoard = []

    for i in range(20):
        displayBoard.append(["#"]*60)
        
    print() 
    print('''"Try not to miss the battleship or you and your mates will be inmates ahaha get it.
            *wheezes* I mean in jail together forever", the parrot chirped in.
          ''')
    print()    

    booms = 1
    shipCounter = 0
    while booms <= 15:
        if shipCounter == 5:
            display()
            countRow = 1
            for row in displayBoard:
                print("".join(row), countRow)
                countRow += 1
                
            print ("Aye! Aye! Well done matey")
            attempts = booms - 1
            booms = 16
        else:
            display()
            countRow = 1
            for row in displayBoard:
                print("".join(row), countRow)
                countRow += 1
            try:
                userRow, userCol = map(int, input("Fire in the hole! (enter row and column): ").split())              
                if userRow < 1 or userRow > 20 or userCol < 1 or userCol > 60:
                    print ("Mate ye can't reach nirvana can ye. *crew members stared at yer bewildered by the epic miss*")
                    continue
            except ValueError:
                print("Type in the right column and row, mate. Savy?")
                continue
            else:
                booms += 1
                bombed = board[userRow-1][userCol-1]
                if ships == 80: #beginner mode
                    if bombed == 5:
                        print ("Are ye trying to venge the spirit! Ye already bombed the ship down")
                    else:
                        if bombed == 6:
                            print ("Shiver me timbers. Yer must be getting old.You already know there is no ship!")
                        else:
                            if bombed >= 1 and bombed <= 4:
                                shipCounter += 1
                                print ("Aye! Aye! Well done matey")
                                shipIndex = []
                                for n, i in enumerate(board[userRow-1]):
                                    if i == bombed:
                                        shipIndex.append(board[userRow-1].index(i))
                                        board[userRow-1][n] = 5
                                        for i in shipIndex:
                                            displayBoard[userRow-1][n] = "O"

                            else:
                                print ("Mate are ye ok? Ye have missed the ship. Blimey!")
                                board[userRow-1][userCol-1] = 6
                                displayBoard[userRow-1][userCol-1] = " "
                                
                elif ships == 50: #intermediate mode
                    if bombed == 4:
                        print ("Are ye trying to venge the spirit! Ye already bombed the ship down")
                    else:
                        if bombed == 5:
                            print ("Shiver me timbers. Yer must be getting old.You already know there is no ship!")
                        else:
                            if bombed >= 1 and bombed <= 3:
                                shipCounter += 1
                                print ("Aye! Aye! Well done matey")
                                shipIndex = []
                                for n, i in enumerate(board[userRow-1]):
                                    if i == bombed:
                                        shipIndex.append(board[userRow-1].index(i))
                                        board[userRow-1][n] = 4
                                        for i in shipIndex:
                                            displayBoard[userRow-1][n] = "O"
                            else:
                                print ("Mate are ye ok? Ye have missed the ship. Blimey!")
                                board[userRow-1][userCol-1] = 6
                                displayBoard[userRow-1][userCol-1] = " "
                                
                elif ships == 20: #advanced mode
                    if board[userRow-1][userCol-1] == 2: 
                        print ("Are ye trying to venge the spirit! Ye already bombed the ship down")
                    else:
                        if board[userRow-1][userCol-1] == 3:
                            print ("Shiver me timbers. Yer must be getting old.You already know there is no ship!")
                        else:
                            if board[userRow-1][userCol-1] == 1: #if position chosen == 1 in board
                                shipCounter += 1
                                print ("Aye! Aye! Well done matey")
                                shipIndex = [] #initialize index list to use for display board
                                for n, i in enumerate(board[userRow-1]): #for the row specificed by user in board list
                                        if i == 1:
                                            shipIndex.append(board[userRow-1].index(i))
                                            board[userRow-1][n] = 2
                                            for i in shipIndex:
                                                displayBoard[userRow-1][n] = "O"
                        
                            else:
                                print ("Mate are ye ok? Ye have missed the ship. Blimey!")
                                board[userRow-1][userCol-1] = 6
                                displayBoard[userRow-1][userCol-1] = " "

    if attempts >= 13 and attempts <= 15:
        print ("You are a novice. Capitan LEVEL")
    elif attempts >=10 and attempts <= 12:
        print ("Not bad. QuarterMaster LEVEL")
    elif attempts < 10:
        print ("You have the talent! FirstMate LEVEL")
    else:
        print ("You've no luck today, try again. CabinBoy LEVEL")

    userscore = (attempts)
    print("Your score is", userscore)

    scorefile = open('score.txt','r')
    score = scorefile.readlines()
    scorefile.close

    scorelist = []

    #put highscores into list
    for line in score:
        scorelist.append(line.split(" "))

    #change score to integer
    for item in scorelist:
        item[0]=int(item[0])
        
    #To check replace highscore or add highscore
    if len(scorelist)==10 :
        if userscore<(scorelist[-1][0]):
            print("Congratulations! Ye beat the highscore! :)")
            username=(input("Please enter ye name mate: ")+"\n")
            scorelist[-1]=[userscore,username]
            list.sort(scorelist)
        else:
            print("Try harder next time. :(")
                   
    else:
        print("Congratulation! Ye beat the highscore! :)")
        username=(input("Please enter ye name: ")+"\n")
        scorelist.append([userscore,username])
        list.sort(scorelist)
    
    writescore=open('score.txt','w')
    for item in scorelist:
        writescore.write(str(item[0])+" "+item[1])
    writescore.close()


    

print('''
´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´
''')
try:
    print("Press a to start the game \nPress b to display the highscore \nPress c to delete the highscore \nPress d to exit the game\n")
    ans=input()
    if ans =="a":
        try:
            difficulty = int(input("What difficulty would you like to play? (1=Beginner/2=Intermediate/3=Advance) "))
            if difficulty == 1:
                board(80, [0,1,0,2,0,3,0,4,0])
            elif difficulty == 2:
                board(50,[0,0,0,0,1,0,0,0,0,2,0,0,0,0,0,3,0,0,0])
            elif difficulty == 3:
                board(20,[0,0,0,1,0,0,0,0,0,0,0,0])
        except:
            print("Please enter 1,2 or 3")
    elif ans=="b":
        displayscore()
        loop=False
    elif ans=="c":
        deletescore()
        loop=False
    elif ans=="d":
        print("Thanks you and see you next time")
        loop=False
    else:
        print("Not valid choice try again")
except ValueError:
    print("Please enter a,b,c or d")
        


def displayscore():
    readscore = open('score.txt','r')
    score = readscore.readlines()
    readscore.close

    print("HIGH SCORE")
    for line in score:
        shipCounter=(line.split("\n"))
        print(shipCounter[0])

def deletescore():
    clearscore=open('score.txt','w')
    clearscore.close


