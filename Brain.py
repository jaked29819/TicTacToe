from board import Board
from board import PLAYERS

class Brain:
    Player = 'O'
    def getWinCount(self, board, move, player):
        if player not in PLAYERS:
            print("Player is not alowed")
        tempBoard = Board()
        tempBoard.mimicBoard(board)
        tempBoard.markSquare(move[0], move[1], player)
        if tempBoard.checkWin(False) is self.Player:
            return 1
        elif tempBoard.checkWin(False) != '':
            return -1
        else:
            nextPlayer = ''
            counter = 0
            for playersList in PLAYERS:
                if playersList is not player:
                    nextPlayer = playersList
            for nextMove in tempBoard.getAvailableMoves():
                counter += self.getWinCount(tempBoard, nextMove, nextPlayer)
            return counter
            
    def getNextMove(self, board):
        moves = list()
        for move in board.getAvailableMoves():
            moves.append([move,self.getWinCount(board,move,self.Player)])
        if len(moves) == 0:
            return [-1,-1]
        mostWinsMove = moves[0]
        for move in moves:
            if mostWinsMove[1] < move[1] or move[1] == 1:
                mostWinsMove = move
        return mostWinsMove[0]
            
