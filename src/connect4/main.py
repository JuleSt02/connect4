
from .settings import BOARD_ROWS, BOARD_COLUMNS, VICTORY_STREAK
from .logic import inverted_board,  has_streak 
from .board import Board
from .game import Game

def main():
    print("Holi")
    game = Game()
    game.start()
    print("JUEGO")
    
if __name__ == "__main__":
    main()
