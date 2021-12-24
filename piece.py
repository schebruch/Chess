class Piece:
    def __init__(self, color, pieceName):
        if color not in {'W', 'B'}:
            raise Exception("Color must be White (W) or Black (B)")
        if pieceName not in {"Rook", "Knight", "Bishop", "King", "Queen", "Pawn"}:
            raise Exception("Piece must be valid")
        self.__color = color 
        self.__pieceName = pieceName
    
    def setColor(self, color): 
        self.__color = color 
    
    def setPieceName(self, pieceName):
        self.__pieceName = pieceName
    
    def getColor(self):
        return self.__color

    def getPieceName(self):
        return self.__pieceName