from ..move import Move
from ..player import Player
from ..piece import Piece
from typing import List

class DrawOffer(Move):
    def __init__(self, player: Player, board: List[List[Piece]]):
        super().__init__(player, board)
        
    def isLegalMove(self) -> bool:
        return True
