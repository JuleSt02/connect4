#Adding type_checking to avoid circular imports when trying to import BaseOracle into player and
#Oracle is importing Player, these type hints dont do anything on runtime

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from .oracle import ColumnClassification, ColumnRecommendation
from .logic import is_valid

if TYPE_CHECKING:
    from .oracle import BaseOracle


class Player:

    """
    Representa un jugador, con un nombre y un caracter (con el que juega)
    """
#Aqui si necesitamos crear un init ya que tenemos que decirle tu te llamas "Manolo" y juagas con "X"
#This typehint BaseOracle does NOT create a BaseOracle it is just info for us humans.
# Simple documentation
#When creating a Player, BaseOracle() needs to be passed to be propperly created. 
    def __init__(self, name:str, char:str, oracle: "BaseOracle")->None:

        self._char = char
        self._name = name
        self._oracle = oracle

    def play(self,board):

        """
        Obtiene las mejores recomendaciones, selecciona la mejor de todas y juega en ella
        """ 
        #Get recommendations form Oracle
        #tuple to create like a "class" when a method or a function returns several values
        (best, recommendations) = self._ask_oracle(board)
        #Plays on best position
        self._play_on(board, best)

    #Plays in one position, calls method add from board to add char
    def _play_on(self, board, pos):
        board.add(self._char, pos)
    
    def _ask_oracle(self, board):

        """
        Asks oracle and gets the best option
        """
        #Receive all the recommendations from oracle(list of Enums and Index)
        recommendations = self._oracle.get_recommendation(board,self)
        
        #Get the best option out of that list of recommendations
        best = self._choose(recommendations) 
        
        #Return recomms and best
        return (best, recommendations)


    def _choose(self,recommendations):
        #selecciona la mejor opcion de la lista de las recomendaciones
        valid = list(filter(lambda x: x.classification != ColumnClassification.FULL, recommendations))
         #if an object has named attributes, acccess it with .attribute NOT [index]
        return valid[0].index
        # sorted_recoms = list(sorted(recommendations, key=lambda x: x[1].value, reverse=True))
        # return sorted_recoms[0]
        

class HumanPlayer(Player):

    """
    Doesnt need an Oracle. Receives input from a human player
    """

    def __init__(self, name:str, char:str)->None:

        self._char = char
        self._name = name

    def _ask_oracle(self, board):
        """
        We override the method of our superclass and ask the human which is the oracle in this case
        """
        while True:
            #Get input
            raw = input("Choose a column")
            #Validate
            if is_valid(raw,board):
                pos = int(raw)
                self._play_on(board, pos)
                break
    #We need to override play because the human won´t use the oracle
    def play(self,board, pos):
        """
        Maybe also check how the board looks at the moment? Or maybe we do that in main?
        """       
        board.add(self._char, pos)
              

# #Option Course:
# def _ask_oracle(self,board):
#  while True:
#      raw = input("Select columns : ")
#      if is_valid(raw,board):
#          pos = int(raw)
#          #returns tuple same as method from oracle
#          return (ColumnRecommendation(pos, None), None)