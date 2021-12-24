class Piece:
    def __init__(self, color, pieceName):
        if color not in {'W', 'B'}:
            raise Exception("Color must be White (W) or Black (B)")
        if pieceName not in {"Rook", "Knight", "Bishop", "King", "Queen", "Pawn"}:
            raise Exception("Piece must be valid")
        self.color = color 
        self.pieceName = pieceName