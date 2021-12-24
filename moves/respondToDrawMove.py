from ..move import Move
from ..player import Player
from ..piece import Piece
from typing import List

class RespondTorawMove(Move):
    def __init__(self, player: Player, board: List[List[Piece]], response: bool):
        super().__init__(player, board)
        self.response = response
        
    def isLegalMove(self) -> bool:
        return True

    def getResponse(self) -> bool:
        return self.response
    
    def setResponse(self, response: bool) -> None:
        self.response = response