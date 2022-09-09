import os

def clearScreen():
  if os.name == 'nt':
    os.system('cls')
  else :
    os.system('clear')

PLAYERS = ['X','O']
BOARD_SIZE = 3

class Board:
    def __init__(self):
        self.board = list()
        for row in range(BOARD_SIZE):
            temp = list()
            for col in range(BOARD_SIZE):
                temp.append(" ")
            self.board.append(temp)

    def mimicBoard(self, oldBoard):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                self.board[row][col] = oldBoard.board[row][col]

    # prints the board to command line
    def printBoard(self):
        clearScreen()
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                print(self.board[row][col],end='')
                if col < BOARD_SIZE - 1:
                    print("|",end='')
            print('')
            if row < BOARD_SIZE - 1:
                for col in range(BOARD_SIZE - 1):
                    print('--',end='')
                print('-')

    # mark a square as a player
    def markSquare(self, row, col, value, verbose=True):
        if value not in PLAYERS:
            if verbose:
                print("Player " + value + " does not exist pick another")
            return False
        elif row not in range(BOARD_SIZE) or col not in range(BOARD_SIZE):
            if verbose:
                print("location (" + str(row) + "," + str(col) + ") out of bounds")
            return False
        elif self.board[row][col] in PLAYERS:
            if verbose:
                print("spot taken try another")
            return False
        else:
            self.board[row][col] = value
            return True
    
    #check to see if a player wins
    # returns player string if a players won otherwise returns ''
    def checkWin(self, verbose = True):
        for player in PLAYERS:
            #check rows to see if a players won
            for row in range(BOARD_SIZE):
                if self.board[row][:].count(player) == BOARD_SIZE:
                    if verbose:
                        self.printBoard()
                        print("Player " + player + " wins.")
                    return player
            #check col if players won
            for col in range(BOARD_SIZE):
                #for each row in board itterates through the row "lists"
                # and pulls the "column" out and packs into its own list for counting
                if [row[col] for row in self.board].count(player) == BOARD_SIZE :
                    if verbose:
                        self.printBoard()
                        print("Player " + player + " wins.")
                    return player
            #check corner to corner
            counts = 0
            for index in range(BOARD_SIZE):
                if self.board[index][index] == player:
                    counts += 1
            if counts == BOARD_SIZE:
                if verbose:
                    self.printBoard()
                    print("Player " + player + " wins.")
                return player
            counts = 0
            for index in range(BOARD_SIZE):
                # need the sub 1 since its 0 based
                if self.board[index][BOARD_SIZE - 1 - index] == player:
                    counts += 1
            if counts == BOARD_SIZE:
                if verbose:
                    print("Player " + player + " wins.")
                return player
        return ''
    
    def getAvailableMoves(self):
        availableMoves = list()
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] not in PLAYERS:
                    availableMoves.append([row,col])
        return availableMoves

if __name__ == '__main__' :
    myBoard = Board()
    
    myBoard.markSquare(0,0,'X')
    myBoard.printBoard()
    myBoard.markSquare(1,0,'O')
    myBoard.markSquare(1,1,'O')
    myBoard.markSquare(1,2,'O')
    myBoard.printBoard()
    myBoard.checkWin()
    input()
    myBoard.__init__()
    myBoard.markSquare(0,0,'X')
    myBoard.markSquare(1,0,'X')
    myBoard.markSquare(2,0,'X')
    myBoard.printBoard()
    myBoard.checkWin()
    input()
    myBoard.__init__()
    myBoard.markSquare(0,0,'X')
    myBoard.markSquare(1,1,'X')
    myBoard.markSquare(2,2,'X')
    myBoard.printBoard()
    myBoard.checkWin()
    input()
    myBoard.__init__()
    myBoard.markSquare(0,2,'X')
    myBoard.markSquare(1,1,'X')
    myBoard.markSquare(2,0,'X')
    myBoard.printBoard()
    myBoard.checkWin()
