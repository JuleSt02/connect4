#Adding type_checking to avoid circular imports when trying to import BaseOracle into player and
#Oracle is importing Player, these type hints dont do anything on runtime

from __future__ import annotations
from typing import TYPE_CHECKING
from .oracle import ColumnClassification
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
    def __init__(self, name:str, char:str, oracle :"BaseOracle")->None:

        self._char = char
        self._name = name
        self._oracle = oracle

    def play(self,board):

        """
        Obtiene las mejores recomendaciones, selecciona la mejor de todas y juega en ella
        """

        #Get recommendations form Oracle
        recommendations = self._oracle.get_recommendation(board,self)
        #Selects the best move that will be chosen calling another method 
        best =self._choose(recommendations)    
        #Play on board using board method add, passing char of player and the index of the
       
        board.add(self._char, best)
        
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
    
    #We need to override play because the human won´t use the oracle
    def play(self,board):

        """
        Maybe also check how the board looks at the moment? Or maybe we do that in main?
        """    
        while True:
            choice = input("Choose a column")
            if is_valid(choice,board):
                board.add(self._char, choice)
                break
