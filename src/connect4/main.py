
from .settings import BOARD_ROWS, BOARD_COLUMNS, VICTORY_STREAK
from .logic import inverted_board,  has_streak 
from .board import Board
from .game import Game

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
