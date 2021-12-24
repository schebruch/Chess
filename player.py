from piece import Piece
from typing import List
from typing import Tuple
from move import Move 
from moves.pieceMove import PieceMove

class Player:
    def __init__(self, name: str, color: str, time = 15):
        self.__name = name 
        self.__color = color 
        self.__timeRemaining = time 
        self.__castleKingEligible = True 
        self.__castleQueenEligible = True 
        #for storing the captured set
        self.__opponentPieces = {}
        self.__moveHistory = []


    def makeMove(self, board: List[List[Piece]]) -> Move:
        #can either be a piece move, draw move or resign move 
        move = self.__getDesiredMove(board)
        #check if move is legal
        if not move.isLegalMove():
            raise Exception("Illegal move attempted")
        
        # specific move handler for piece move
        if isinstance(move, PieceMove):
            #add captured piece. move.getPiece() will be null if it is not a capture
            self.addOpponentPiece(move.getPiece())
            self.__handleCastleEligible(move)

        return move 
        

    def __handleCastleEligible(self, move: Move) -> None:
        pieceMoved = move.getPiece()
        if pieceMoved.getPieceName() == "King":
            self.__castleKingEligible = False 
            self.__castleQueenEligible = False 
        #black pieces
        if self.__color == "B":
            #kingside rook
            if pieceMoved.getPieceName() == "Rook":
                if pieceMoved.getStartingPosition() == (0,0):
                    self.setCastleEligibleKingSide(False)
                elif pieceMoved.getStartingPosition() == (0,7):
                    self.setCastleEligibleQueenSide(False)
        #white pieces
        if self.__color == "W":
            #kingside rook
            if pieceMoved.getPieceName() == "Rook":
                if pieceMoved.getStartingPosition() == (7,0):
                    self.setCastleEligibleKingSide(False)
                elif pieceMoved.getStartingPosition() == (7,7):
                    self.setCastleEligibleQueenSide(False)

    #get player's desired move based on how they interact with the UI 
    def __getDesiredMove(self, board: List[List[Piece]]) -> Move:
        pass

    def setName(self, name: str) -> None:
        self.__name = name 
    
    def setColor(self, color:str) -> None:
        if color not in ["W", "B"]:
            raise Exception("Color of piece not valid")
        self.__color = color 
    
    def setTimeRemaining(self, timeRemaining) -> None:
        self.__timeRemaining = timeRemaining
    
    def setCastleEligibleQueenSide(self, castleEligible:bool) -> None:
        self.__castleQueenEligible = castleEligible

    def setCastleEligibleKingSide(self, castleEligible:bool):
        self.__castleKingEligible = castleEligible
    
    #update the dictionary with the opponent piece count 
    def addOpponentPiece(self, piece:Piece) -> None:
        if piece not in self.__opponentPieces:
            self.__opponentPieces[piece] = 1
        else:
            self.__opponentPieces[piece] += 1
    
    #update the dictionary with the opponent piece count 
    def removeOpponentPiece(self, piece:Piece) -> None:
        if piece in self.__opponentPieces:
            if self.__opponentPieces[piece] <= 0:
                raise Exception("Cannot remove piece that does not exist")
            self.__opponentPieces[piece] -= 1
        else:
            raise Exception("Cannot remove piece that does not exist")

    

    def getName(self) -> str:
        return self.__name

    def getColor(self) -> str:
        return self.__color

    def getTimeRemaining(self): 
        return self.__timeRemaining

    def getCastleEligibleKingSide(self) -> bool:
        return self.__castleKingEligible
    
    def getCastleEligibleQueenSide(self) -> bool:
        return self.__castleQueenEligible

    def getOpponentPieces(self) -> dict:
        return self.__opponentPieces
    
    def getMoveHistory(self) -> List[Move]:
        return self.__moveHistory

        