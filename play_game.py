from game import Game 
from player import Player

if __name__ == "__main__":
    game = Game(Player("Sam", "W"), Player("Cam", "B"))
    while game.winner == False and game.draw == False:
        game.assignTurn()