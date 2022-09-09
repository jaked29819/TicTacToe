from board import Board
from board import PLAYERS
from Brain import Brain

class Game:
    myBoard = Board()
    myBrain = Brain()
    myPlayer = myBrain.Player
    realPlayer = PLAYERS[0]

    myBoard.printBoard()
    input("You are player x!\nPress Enter to continue.")

    while True:
        myBoard.printBoard()
        row = int(input("Select row:"))
        col = int(input("Select col:"))
        
        while not myBoard.markSquare(row,col,realPlayer):
            row = int(input("Select row:"))
            col = int(input("Select col:"))

        if len(myBoard.getAvailableMoves()) != 0:
            AiMove = myBrain.getNextMove(myBoard)
            myBoard.markSquare(AiMove[0],AiMove[1],myPlayer)

        if myBoard.checkWin() != '':
            break
        elif len(myBoard.getAvailableMoves()) == 0:
            myBoard.printBoard()
            print("No Winner")
            break

