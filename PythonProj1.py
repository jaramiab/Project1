#printing game/tic tac toe board
gameBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in gameBoard:
    board_keys.append(key)

#Board must print every time after a player makes their move
#We will utilize the print function to print board after every move

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#Main function
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(gameBoard)
        print("YOUR TURN NOW," + turn + ".MAKE YOUR MOVE!")

        move = input()        

        if gameBoard[move] == ' ':
            gameBoard[move] = turn
            count += 1
        else:
            print("THIS PLACE IS FILLED.\nMOVE TO A DIFFERENT SPOT!")
            continue

        #Checks to see if either player has won the game after 5 moves
        if count >= 5:
            if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ': #going across first row
                printBoard(gameBoard)
                print("\nGAME OVER!\n")                
                print(" **** " +turn + " WON! ****")                
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ': #across middle column
                printBoard(gameBoard)
                print("\nGAME OVER!.\n")                
                print(" **** " +turn + " WON! ****")
                break
            elif gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ': #across bottom row
                printBoard(gameBoard)
                print("\nGAME OVER!\n")                
                print(" **** " +turn + " WON! ****")
                break
            elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ': #down left column
                printBoard(gameBoard)
                print("\nGAME OVER!\n")                
                print(" **** " +turn + " WON! ****")
                break
            elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ': #down middle row
                printBoard(gameBoard)
                print("\nGAME OVER!\n")                
                print(" **** " +turn + " WON! ****")
                break
            elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ': #down right row
                printBoard(gameBoard)
                print("\nGAME OVER!\n")                
                print(" **** " +turn + " WON! ****")
                break 
            elif gameBoard['7'] == gameBoard['5'] == gameBoard['3'] != ' ': #diagonal row
                printBoard(gameBoard)
                print("\nGAME OVER!\n")                
                print(" **** " +turn + " WON! ****")
                break
            elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ': #diagonal row
                printBoard(gameBoard)
                print("\nGAME OVER!\n")                
                print(" **** " +turn + " WON! ****")
                break 

        #a tie is announced when both players, X and O, do not win
        if count == 9:
            print("\nGAME OVER.\n")                
            print("WE HAVE A TIE!")

        #Each player alternates after every move
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    #asking the users if they want to play tic tac toe again/rematch
    restart = input("DO YOU WANT TO REMATCH?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            gameBoard[key] = " "

        game()

if __name__ == "__main__":
    game()
