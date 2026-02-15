#CHECK LOOP, CHECK GAME ERRORS WITH EXECUTING LOOP, MISSING PARAMETERS. 
#CHECK GAME, different from course

from .board import Board
from .oracle import BaseOracle, SmartOracle
from enum import Enum,auto
from .match import Match
from .player import Player, HumanPlayer
from pyfiglet import figlet_format
from .logic import inverted_board, reverted_matrix
from beautifultable import BeautifulTable
from .settings import BOARD_COLUMNS
class RoundType(Enum):
   COMPUTER_VS_COMPUTER = auto()
   COMPUTER_VS_HUMAN = auto()

class DifficultyLevel(Enum):
   LOW = auto()
   MEDIUM = auto()
   HIGH = auto()


class Game:
    
    def __init__(self, round_type = RoundType.COMPUTER_VS_COMPUTER,
                 match = Match(Player("Chip"), Player("Chop")), difficulty_level=DifficultyLevel.LOW):
       
       #Save the received values 
       self.round_type = round_type
       self.match = match
       self.difficulty_level = difficulty_level

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
       p1 = self.match.player1
       p2 = self.match.player2
       
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
          if self._is_game_over(p1, p2):
             #display final result
             self.display_result(p1, p2)
             break
    
    def display_move(self, player):
       print(f"{player._name} {player._char} has moved in column {player.last_move}")


    def display_board(self):
       
       # we obtain a amtrix
       matrix = self.board.columns
       matrix = reverted_matrix(matrix)
       # create a beautifultable
       bt = BeautifulTable()
       for col in matrix:
          #bt.columns.append is a traspose operation so list -> col automat.
          bt.columns.append((col))
       bt.columns.header = [str(i) for i in range(BOARD_COLUMNS)]
       # print
       print(bt)
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
       elif self.board.all_full():
          result = True
       return result
       
    def has_victory_player(self,char):
       result = False
       if self.board.is_victory(char):
          result = True
       return result
   

    def print_logo(self):
     logo = figlet_format("Connect4")
     print(logo)
   
    def _configure_by_user(self):
       
       """
       User will choose the setting for the game
       """
      #Ask user to choose the type od game
       self.round_type = self._get_round_type()
       
       #Creates match
       self.match = self._make_match()

       #Choose difficulty
       if self.round_type == RoundType.COMPUTER_VS_HUMAN:
          self.difficulty_level = self._get_difficulty_level()

    def _get_difficulty_level(self):
       
       """
       Ask user to choose the level of difficulty.
       """
   
       print("""Choose your opponent, human.
             
            1) Bender: You might as well kiss a Wookiee
            2) T-800: Great, kid. Don´t get cocky
            3) T-1000: May the Force be with you
            """)
       level = DifficultyLevel.LOW
       response = ""
       while  response != "1" and response != "2" and response != "3":
          
          response = input("Please press 1, 2 or 3: ")
          if response == "1":
             level = DifficultyLevel.LOW
          elif response == "2":
             level = DifficultyLevel.MEDIUM
          else:
             level = DifficultyLevel.HIGH
       return level 
             
       

    
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
     difficulty_levels = {DifficultyLevel.LOW: BaseOracle(), DifficultyLevel.MEDIUM: SmartOracle(), DifficultyLevel.HIGH: SmartOracle()}
     
     if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
         #both players are computers
         player1 = Player("Ex-Machina", oracle=SmartOracle())
         player2 = Player("Wall-E", oracle=SmartOracle())
     else:
         #pc vs human
         player1 = Player("Robocop", oracle=difficulty_levels[self.difficulty_level])
         player1._oracle
         #We accept direct input for now
         player2 = HumanPlayer(name=input("Enter your name human: "))
      #We return and create the Match
     return Match(player1, player2)
    
       
    
      
       



