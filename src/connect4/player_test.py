from .board import Board
from .player import Player, HumanPlayer
from .oracle import BaseOracle
from .logic import is_valid, is_col_range, is_int, column_full



def test_play():

    """
    We check if play uses the first available column. We check only the play from our Player"""

    before = Board.from_list([[None, None, None, None],
                              ["x","x", "o", "o"],
                              ["x","x", "o", "o"],
                              [None, None, None, None]] )
    after = ([["x", None, None, None],
                              ["x","x", "o", "o"],
                              ["x","x", "o", "o"],
                              [None, None, None, None]] )


    player = Player("Chip", "x")

    player.play(before)
    #Python reads after as a list of lists not as a Board Object so it needs to be
    #converted to a BoardInstance first.
    assert before == Board.from_list(after)


def test_is_valid():
    valid = Board.from_list([[None, None, None, None],
                        ["x","x", "o", "o"],
                        ["x","x", "o", "o"],
                        [None, None, None, None]] )

    
    assert is_col_range(0)
    assert is_int("1")
    assert is_int("holi") == False
    assert is_col_range(5) == False
    assert column_full(1, valid)
    assert column_full(0, valid) == False

        