from .board import Board
from enum import Enum,auto
from .match import Match
from .player import Player
import pyglet

class RoundType(Enum):
   COMPUTER_VS_COMPUTER = auto()
   COMPUTER_VS_HUMAN = auto()

class DifficultyLevel(Enum):
   LOW = auto()
   MEDIUM = auto()
   HIGH = auto()
class Game:
    
    def __init__(self, round_type = RoundType.COMPUTER_VS_COMPUTER,
                 match = Match(Player("Chip"), Player("Chop"))):
       
       #Save the received values 
       self.round_type = round_type
       self.match = match
       # We won´t receive a board from the outside (that is why its not present
       # in init) we will create a fresh one for every game
       self.board = Board()
    
    def start(self):
       #Print logo of the game
       #Create match
       # #Start game loop 
       self.print_logo()

       self._configure_by_user()
   
    def _configure_by_user(self):
       
       """
       User will choose the setting for the game
       """
      
      #CHoose type of game 
       
    
      
       
    def print_logo(self):
       logo = pyglet.text.Label("Connect4", font_name="Arial", font_size=28)
       print(logo)



