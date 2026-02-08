#CHECK LOOP, CHECK GAME ERRORS WITH EXECUTING LOOP, MISSING PARAMETERS. 
#CHECK GAME, different from course

from .board import Board
from enum import Enum,auto
from .match import Match
from .player import Player, HumanPlayer
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
       self.print_logo()
       #Create match
       self._configure_by_user()
         # #Start game loop 
       self._start_game_loop()
   
    def _start_game_loop(self):
       """Starts game,creates loop, finished with a GAME OVER"""
       
       while True:
          #We obtain the current player
          current_player = self.match.next_player
          #Play
          current_player.play(self.board)
          #display  move
          self.display_move(current_player)
          #display the board
          self.display_board()
          #if the game is over
          if self._is_game_over(self):
             #display final result
             self.display_result(self)
    
    def display_move(self, player):
       print(f"{player._name} {player._char} has moved in column {player.last_move}")

    def display_board(self):
       print(self.board)
    #Needs to be modified
    def display_result(self,player1, player2):
       """
       If the game is over, it displays the result
       """
       if self.has_victory_player(player1._char):
        print(f"The winner is {player1._name} !!!") 
       elif self.has_victory_player(player2._char):
        print(f"The winner is {player2._name} !!!")
       else:
         print(f"No winners for today, its a tie between {player1._name} and {player2._name}")
   

    
    def _is_game_over(self, player1, player2):
       
       """
       Predicate that checkst if there is either a victory of one of the players or a full board(tie) resulting in GAME OVER.
       """
       result = False
       if self.has_victory_player(player1._char) or self.has_victory_player(player2._char):
          result = True
       elif self.board_is_full_tie():
          result = True
       return result
       
    def has_victory_player(self,char):
       result = False
       if self.board.is_victory(char):
          result = True
       return result
   
    def board_is_full_tie(self):
       """
      Method that checks if all of the columns of the board are full.
       """
       counter = 0
       #Itterate over all cols calling the mehotd is_full of board 
       for i in range(len(self.board)):
          if self.board.is_full(i):
             counter += 1
       return counter == len(self.board)

    def print_logo(self):
     logo = pyglet.text.Label("Connect4", font_name="Arial", font_size=28)
     print(logo)
   
    def _configure_by_user(self):
       
       """
       User will choose the setting for the game
       """
      #Ask user to choose the type od game
       self.round_type = self._get_round_type()
       
       #Creates match
       self.match = self._make_match()
    
    def _get_round_type(self):
       """
       Ask user
       """
       print("""Select type of round: 
            1) Computer vs Computer
            2) Computer vs  Human
            """)
       response = ""
       round_type = None
       # Loop that continues if the response is different from 1 AND different from 2
       # If either one is False ex. response = 1 Condition evaluates to False, loop breaks
       while response != "1" and response != "2":
          response = input("Please press 1 or 2: ")
          if response == "1":
             round_type = RoundType.COMPUTER_VS_COMPUTER
          else:
             round_type = RoundType.COMPUTER_VS_HUMAN
       return round_type

    def _make_match(self):
     """
     Player1 will always be a computer
     """
     if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
         #both players are computers
         player1 = Player("Ex-Machina")
         player2 = Player("Wall-E")
     else:
         #pc vs human
         player1 = Player("Robocop")
         #We accept direct input for now
         player2 = HumanPlayer(name=input("Enter your name human: "))
      #We return and create the Match
     return Match(player1, player2)
    
       
    
      
       



