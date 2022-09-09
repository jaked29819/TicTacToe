import unittest
from board import Board
from Brain import Brain

class BrainTester(unittest.TestCase):

    def test_CountWins(self):
        """
        o| |
        x|o|x
        x| |
        """
        myBoard = Board()
        thisBrain = Brain()

        myBoard.markSquare(0,0,'O')
        myBoard.markSquare(1,0,'X')
        myBoard.markSquare(1,1,'O')
        myBoard.markSquare(1,2,'X')
        myBoard.markSquare(2,0,'X')
        movesAvailable = myBoard.getAvailableMoves()

        self.assertEqual(len(movesAvailable),4)
        #force to count posible wins if O plays in 0,1 (top, middle)
        result = thisBrain.getWinCount(myBoard, [0,1],'O')
        self.assertEqual(result,6)
        result = thisBrain.getWinCount(myBoard, [0,2],'O')
        self.assertEqual(result,4)
        result = thisBrain.getWinCount(myBoard, [2,1],'O')
        self.assertEqual(result,4)
        result = thisBrain.getWinCount(myBoard, [2,2],'O')
        self.assertEqual(result,1)


        """
        o|x|x
        x|o|x
        x|x|
        """
        myBoard.markSquare(0,1,'X')
        myBoard.markSquare(0,2,'X')
        myBoard.markSquare(2,1,'X')
        
        movesAvailable = myBoard.getAvailableMoves()

        self.assertEqual(len(movesAvailable),1)
        result = thisBrain.getWinCount(myBoard, movesAvailable[0],'O')
        self.assertEqual(result,1)
        
        """
        o| |x
        x|o|x
        x|x|
        """
        myBoard.mimicBoard(Board())
        myBoard.markSquare(0,0,'O')
        myBoard.markSquare(0,2,'X')
        myBoard.markSquare(1,0,'X')
        myBoard.markSquare(1,1,'O')
        myBoard.markSquare(1,2,'X')
        myBoard.markSquare(2,0,'X')
        myBoard.markSquare(2,1,'X')
        movesAvailable = myBoard.getAvailableMoves()

        self.assertEqual(len(movesAvailable),2)
        result = thisBrain.getWinCount(myBoard, movesAvailable[0],'O')
        self.assertEqual(result,-1)
        

    def test_NextMove(self):
        myBoard = Board()
        thisBrain = Brain()

        myBoard.markSquare(0,0,'O')
        myBoard.markSquare(1,0,'X')
        myBoard.markSquare(1,1,'O')
        myBoard.markSquare(1,2,'X')
        myBoard.markSquare(2,0,'X')

        result = thisBrain.getNextMove(myBoard)
        self.assertEqual(result,[2,2])


class BoardTester(unittest.TestCase):

    def test_VericalWins(self):
        #Check virtical wins
        myBoard = Board()
        myBoard.markSquare(1,0,'O')
        myBoard.markSquare(1,1,'O')
        myBoard.markSquare(1,2,'O')
        result = myBoard.checkWin(False)

        self.assertEqual(result,'O')

    def test_HorizontalWins(self):
        #check horizontal wins
        myBoard = Board()
        myBoard.markSquare(0,0,'O')
        myBoard.markSquare(1,0,'O')
        myBoard.markSquare(2,0,'O')
        result = myBoard.checkWin(False)

        self.assertEqual(result,'O')

    def test_DiagnalWins(self):
        #check diagnal wins
        myBoard = Board()
        myBoard.markSquare(0,0,'O')
        myBoard.markSquare(1,1,'O')
        myBoard.markSquare(2,2,'O')
        result = myBoard.checkWin(False)

        self.assertEqual(result,'O')

    def test_BoardInit(self):
        #checks that Board(myBoard) works
        myBoard = Board()
        myBoard.markSquare(0,0,'O')
        myBoard.markSquare(1,1,'O')
        myBoard.markSquare(2,2,'O')
        result = myBoard.checkWin(False)

        self.assertEqual(result,'O')

        myNewBoard = Board()
        myNewBoard.mimicBoard(myBoard)
        result = myNewBoard.checkWin(False)

        self.assertEqual(result,'O')
    
    def test_markSquareOutOfBounds(self):
        myBoard = Board()
        #check player not in bounds
        result = myBoard.markSquare(0,0,'A',False)
        self.assertFalse(result)

        #check row not in bounds
        result = myBoard.markSquare(10,0,'X',False)
        self.assertFalse(result)

        #check col not in bounds
        result = myBoard.markSquare(0,10,'X',False)
        self.assertFalse(result)

        #check square not already used
        myBoard.markSquare(0,0,"X",False)
        result = myBoard.markSquare(0,0,"O",False)
        self.assertFalse(result)

    def test_availableMoves(self):
        myBoard = Board()
        availableMoves = myBoard.getAvailableMoves()
        result = [0,0] in availableMoves
        self.assertTrue(result)

        myBoard.markSquare(0,0,'X',False)
        myBoard.markSquare(1,1,'O',False)
        availableMoves = myBoard.getAvailableMoves()
        result = [0,0] in availableMoves or [1,1] in availableMoves
        self.assertFalse(result)

