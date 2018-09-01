#tic tac toe game
board = [' ' for x in range(10)] # this stores x and 0 in game

def insertletter(letter, pos):
    board[pos] = letter          #insert the letter in our board

def spaceIsFree(pos):
    return board[pos] == ' '    #check the space is free or not in the board

def printBoard(board):          #it will print the board 
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):              #bo stands for board and le stands for letter and it checks if we have a winner on board or not               
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or

    (bo[4] == le and bo[5] == le and bo[6] == le) or #these are the possible outcomes how a player can win

    (bo[1] == le and bo[2] == le and bo[3] == le) or

    (bo[1] == le and bo[4] == le and bo[7] == le) or

    (bo[2] == le and bo[5] == le and bo[8] == le) or

    (bo[3] == le and bo[6] == le and bo[6] == le) or

    (bo[1] == le and bo[5] == le and bo[9] == le) or

    (bo[3] == le and bo[5] == le and bo[7] == le))

def playerMove():              #asking the player where to move
    run = True
    while run:
        move = input('Select a positin to a place an \'x\' (1-9)')
        try:                   #using try and except just to make sure the player is giving a valid number or not
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertletter("x",move)
                else:
                    print("sorry this space is occupied")
            else:
                print("please type a number within range")
        except:
            print("please type a number")

def compMove():
    possibleMoves =[ x for x, letter in enumerate(board) if letter == ' ' and x!=00] #it will give a list of possible moves
    move = 0

    for let in ['o','x']:      
        for i in possibleMoves:
            boardCopy = board[:] #we are making a clone of board here
            boardCopy[i] = let   
            if isWinner(boardCopy,let): #we check if the boardcopy is wins or not
                move=i
                return move

    cornersOpen = []      
    for i in possibleMoves:        
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:       #check the number of corners
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:  #check if the centre is open
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:       #check the number of edges
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):        #create a random number and return a number
    import random
    ln = len(li)
    r = random.randrange(0,ln)  
    return li[r]




def isBoardFull(board):             # to check whether the board is full or not
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():         #here we execute functions and commands
   print('ZERO KAATA!')
   printBoard(board)

   while not(isBoardFull(board)):
       if not(isWinner(board,'o')): #check to see if the computer won or not
         playerMove()
         printBoard(board)
       else:
           print("Sorry 0\'s won this time")
           break

       if not (isWinner(board, 'X')):  #check we won or not
           move = compMove()
           if move == 0:            #if no moves are left then it's a tie
               print("tie game")
           else:
               insertletter('o',move)
               print('Computer placed an \'o\' in position',move,':')
               printBoard(board)


       else:
           print("x\'s won this time! Congratulations!!!")
           break

   if isBoardFull(board):
     print('Tie game!')

main()

