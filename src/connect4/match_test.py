import pytest

from .player import Player
from .match import Match 

#Create two the variables that will store our players so they exist in the global scope
xavier = Player("Prof. Xavier")
otto = Player("Dr Octupus")

#Used so evertyhing is setup and tearedown after each test. 
def setup():
    # This way Pytho knows that we want to modify the global variable
    #  and doesn´t create a new local variable
    global xavier
    xavier = Player("Prof. Xavier")
    global otto 
    otto = Player("Dr Octupus")

def teardown():
    global xavier
    xavier = None
    global otto
    otto = None
#Check that once Match is created both players got different chars assigned
def test_different_players_different_chars():

    t = Match(xavier, otto)

#Check that no player has the char None
def test_no_player_char_none():
    t = Match(xavier, otto)
    assert xavier._char != None
    assert otto._char != None


#Check if one player gets called after anotherñ mnkl
def test_next_player_is_round_robin():
    t = Match(otto, xavier)
    p1 = t.next_player
    p2 = t.next_player
    assert p1 != p2

#Check if players know that they are opponents
def test_players_are_opponents():
    t = Match(otto, xavier)
    #Using getter from decorator property
    x = t.get_player("x")
    o = t.get_player("o")

    assert o._opponent == x
    assert x._opponent == o