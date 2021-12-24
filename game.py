from player import Player
from piece import Piece  
class Game:
    DIMENSION = 8
    #initialize the board with the pieces
    #initialize the game players 
    def __init__(self, player1, player2):
        self.moveCount = 0
        self.player1 = player1
        self.player2 = player2 
        self.draw = False
        self.initializeBoard()

    #the chess board will have black on top (at position (0,0)) and white on the bottom (at position(7,0))
    def initializeBoard(self):
        #initialize our 8x8 grid to null values
        self.board = [[None for i in range(self.DIMENSION)] for j in range(self.DIMENSION)]
        self.board[0][0] = Piece("B", "Rook")
        self.board[0][1] = Piece("B", "Knight")
        self.board[0][2] = Piece("B", "Bishop")
        self.board[0][3] = Piece("B", "King")
        self.board[0][4] = Piece("B", "Queen")
        self.board[0][5] = Piece("B", "Bishop")
        self.board[0][6] = Piece("B", "Knight")
        self.board[0][7] = Piece("B", "Rook")

        self.board[7][0] = Piece("W", "Rook")
        self.board[7][1] = Piece("W", "Knight")
        self.board[7][2] = Piece("W", "Bishop")
        self.board[7][3] = Piece("W", "King")
        self.board[7][4] = Piece("W", "Queen")
        self.board[7][5] = Piece("W", "Bishop")
        self.board[7][6] = Piece("W", "Knight")
        self.board[7][7] = Piece("W", "Rook")

        #initializing the pawns
        for i in range(self.DIMENSION):
            self.board[1][i] = Piece("B", "Pawn")
            self.board[6][i] = Piece("W", "Pawn")    

    #prints the chess board where pieces are abbreviated
    #come back later 
    def printBoard(self):
        print('\n'.join(['\t'.join(["{}({})".format(cell.pieceName, cell.color) if cell != None else "" for cell in row ]) for row in self.board]))
 

