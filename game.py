from player import Player
from piece import Piece  
class Game:
    DIMENSION = 8
    #initialize the board with the pieces
    #initialize the game players 
    #assume player1 has white and player2 has black
    def __init__(self, player1: Player, player2: Player):        
        self.__moveCount = 0
        self.__player1 = player1
        self.__player2 = player2 
        self.__activePlayer = player1
        self.__draw = False
        self.__drawOffered = False
        self.__winner = None
        self.initializeBoard()

    #the chess board will have black on top (at position (0,0)) and white on the bottom (at position(7,0))
    def initializeBoard(self):
        #initialize our 8x8 grid to null values
        self.__board = [[None for i in range(self.DIMENSION)] for j in range(self.DIMENSION)]
        self.__board[0][0] = Piece("B", "Rook")
        self.__board[0][1] = Piece("B", "Knight")
        self.__board[0][2] = Piece("B", "Bishop")
        self.__board[0][3] = Piece("B", "King")
        self.__board[0][4] = Piece("B", "Queen")
        self.__board[0][5] = Piece("B", "Bishop")
        self.__board[0][6] = Piece("B", "Knight")
        self.__board[0][7] = Piece("B", "Rook")

        self.__board[7][0] = Piece("W", "Rook")
        self.__board[7][1] = Piece("W", "Knight")
        self.__board[7][2] = Piece("W", "Bishop")
        self.__board[7][3] = Piece("W", "King")
        self.__board[7][4] = Piece("W", "Queen")
        self.__board[7][5] = Piece("W", "Bishop")
        self.__board[7][6] = Piece("W", "Knight")
        self.__board[7][7] = Piece("W", "Rook")

        #initializing the pawns
        for i in range(self.DIMENSION):
            self.__board[1][i] = Piece("B", "Pawn")
            self.__board[6][i] = Piece("W", "Pawn")    
    
    #after a player makes a move the player will assign its turn attribute to false 
    def handleActivePlayerTurn(self):
        try: 
            move = self.__activePlayer.makeMove()
        #illegal moves
        #implement custom exceptions later 
        except Exception as e:
            print("Illegal move")
            return  



    #prints the chess board where pieces are abbreviated
    #come back later 
    def printBoard(self):
        print('\n'.join(['\t'.join(["{}({})".format(cell.pieceName, cell.color) if cell != None else "" for cell in row ]) for row in self.board]))
 

