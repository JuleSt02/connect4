from .board import Board
from .player import Player, HumanPlayer
from .oracle import BaseOracle
from .logic import is_valid, is_col_range, is_int, column_full



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


