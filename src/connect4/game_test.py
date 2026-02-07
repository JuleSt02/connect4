import pytest

from .game import Game
from .board import Board

def test_creation():
    #Testing if isntance game is propperly created
    g = Game
    assert g!= None

def test_game_is_over():
    game = Game()

    win_x = ([["o", "x", "x", "x"],
            [None,None,None,None],
                [None,None,None,None],
                [None,None,None,None]])
    
    win_o = ([["o", "x", "x", None],
            ["o","x","x",None],
            ["o",None,None,None],
            ["o",None,None,None]])
    
    unfinished = ([["o", "x", "x", None],
                  [None,None,None,None],
                [None,None,None,None],
                [None,None,None,None]])

    #When game starts it creates a Board instance
    #self.board = Board(), so game.board is an attribute of the Game object
    #For testint we reassign  game.board to win_x (board state created for testing)
    #the Game methos will check this data to evaluate whether the game is over
    game.board = win_x
    assert game._is_game_over() == True

    game.board = win_o
    assert game._is_game_over() == True

    game.board = unfinished
    assert game._is_game_over() == False

    