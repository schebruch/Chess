from ..move import Move
from ..player import Player
from ..piece import Piece
from typing import List

class PieceMove(Move):
    def __init__(self, player: Player, board: List[List[Piece]]):
        super().__init__(player, board)
        
    def isLegalMove(self) -> bool:
        return False


'''
    #updates the game board by making a move if it is eligible for the player to make 
    def makeMove(self, board, startingPosition, endingPosition):
        #the player's selected piece
        selectedPiece = board[startingPosition][endingPosition]
        #determines whether we're currently in check 
        inCheck = self.inCheck(board)

        #should be Illegal Move Exception (null square)
        if selectedPiece == None:
            raise Exception("Selected square ({},{}) has no piece".format(startingPosition, endingPosition))
        #should be Illegal Move Exception (attempted to move opponent piece)
        if selectedPiece.color != self.color:
            raise Exception("Attempted to move opponent's piece")
        
        validDestinations = self.getAllValidDestinations(selectedPiece, board, startingPosition, inCheck)

        if endingPosition not in validDestinations:
            raise Exception("The {} cannot move to square ({},{})".format(selectedPiece.pieceName, startingPosition, endingPosition))
    
        if self.discoveredCheck(startingPosition, endingPosition):
            raise Exception("This move will result in a discovered check")
        

    def getAllValidDestinations(self, selectedPiece, board, startingPosition, inCheck):
        pass 

    def discoveredCheck(self, board, startingPosition, endingPosition):
        # cases:
        # 1. moved piece is diagonal to our king
        # 2. moved piece is adjacent (left or right) to our king
        # 3. moved piece is above or below our king 

        #first, get our king's coordinates

        #checking for adjacency
        pass


    def inCheck(self, board):
        pass 

    #returns the (x,y) coordinate of the piece or None if the piece is not on the board 
    def getPieceCoordinate(self, board, piece):
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == piece:
                    return (x,y)
        return None 
'''