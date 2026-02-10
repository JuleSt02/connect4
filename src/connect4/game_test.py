import pytest

from .game import Game
from .board import Board
from .player import Player

def test_creation():
    #Testing if isntance game is propperly created
    g = Game
    assert g!= None


chip = Player("Chip", "x")
chop = Player("Chopp" , "o")
def test_game_is_over():
    
    game = Game()
 

    win_x = Board.from_list ([["o", "x", "x", "x"],
            [None,None,None,None],
                [None,None,None,None],
                [None,None,None,None]])
    
    win_o = Board.from_list([["o", "x", "x", None],
            ["o","x","x",None],
            ["o",None,None,None],
            ["o",None,None,None]])
    
    unfinished = Board.from_list([["o", "x", "x", "x"],
                  [None,None,None,None],
                [None,None,None,None],
                [None,None,None,None]])
    tie = Board.from_list([
                            ["x", "o", "x", "o"],
                            ["o", "x", "o", "x"],
                            ["x", "o", "x", "o"],
                            ["o", "x", "o", "x"],
                        ])
    

    #When game starts it creates a Board instance
    #self.board = Board(), so game.board is an attribute of the Game object
    #For testint we reassign  game.board to win_x (board state created for testing)
    #the Game methos will check this data to evaluate whether the game is over
    
    game.board = win_x
    assert game._is_game_over(chip, chop) == True

    game.board = win_o
    assert game._is_game_over(chip, chop) == True
    
    game.board = tie
    assert game._is_game_over(chip, chop) == True

    game.board = unfinished
    assert game._is_game_over(chip, chop) == True

   
    