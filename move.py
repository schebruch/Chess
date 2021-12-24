from player import Player
from piece import Piece
from typing import List
from abc import ABC, abstractmethod
class Move(ABC):
    def __init__(self, player: Player, board: List[List[Piece]]):
        self.player = player 
        self.board = board 
        
    @abstractmethod
    def isLegalMove(self) -> bool:
        pass
