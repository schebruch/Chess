from piece import Piece
class Player:
    def __init__(self, name, color, time = 15):
        self.name = name 
        self.color = color 
        self.time = time 
        self.castleLeftEligible = True 
        self.castleRightEligible = True 
        #for storing the captured set
        self.opponenetPieces = {}

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
        pass 

    def inCheck(self, board):
        pass 
        