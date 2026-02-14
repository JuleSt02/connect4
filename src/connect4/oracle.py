#CHECK AND MODIFY

#Clases de columnas, hay varios estados pero siempre puede haber solo uno, por lo tanto ENUM
from enum import Enum, auto
from .board import Board
from .settings import BOARD_COLUMNS 
import copy


class ColumnClassification(Enum):

    FULL = -1 #imposible
    LOSE = 1 #derrota inminente si juegas ahi generas un tablero tal que el otro aunque sea
                  #idiota pierdes, hagas lo que hagas               
    BAD = 5 #muy indeseable
    MAYBE = 10 #indeseable
    WIN = 100 #victoria inmediata

    #Buena estructura de datos hace que el codigo sea mas eficiiente y mas sencillo

class ColumnRecommendation:
    """
    Clase que representa la recomendacion del oraculo para una columna.
    Se compone del indice de dicha columna en el ttablero y un valor de ColumnClassification.
    """
  #Esta clase no es especialmemnte inteleginte, podriamos usar una tupla 
    def __init__(self, index:int, classification: ColumnClassification):
        self.index = index
        self.classification = classification

        #Va a recibir a self y a other, el otro objeto con el que va a comparar
    def __eq__(self,other):
       
       #si son de clases distantas, pues distintos
       #Estas instancias son de la misma clase?
       if not isinstance(other, self.__class__):
          return False
       #If same class, we check the attribute classification , index attribute  is not relevant for this 
       else:
          return (self.classification) == (other.classification)
       

#Oraculos, de mas tonto a mas listo
#los oraculos, deben  de realizar un trabajo complejo: clasificar columnas
#en el caso mas complejo, teniendo en cuenta errores del pasado.
#usamos dividi y venceras, y cada oraculo del mas tonto al mas listo 
# se encargara de una parte

class BaseOracle:

    """
    La clase base y el oraculo mas tonto: clasifica las columnas en llenas y no llenas.
    """
    #No necesita init porque no consstruye nada, se comportara como una funcion, le preguntamos
    #algo y nos devolvera algo.

    def get_recommendation(self, board:Board, player)->list[ColumnRecommendation]:
      recommendations = []

      for index in range(BOARD_COLUMNS):
         recommendations.append(self._get_columns_recommendation(board, index, player))
      return recommendations
    
    def _get_columns_recommendation(self, board, index:int, player)->ColumnRecommendation:
        """
       Private method that determines if a column is full and in that case classification becomes FULL,
       everything else is classified as MAYBE
        """
        result = ColumnRecommendation(index, ColumnClassification.MAYBE)
        #Checking if we are incorrect, if is_full is True we change the classification
        #We adapted the method so it doesn´t access board._columns the attribute of our class board
        #directly but only "sends" the index int of the column to the method is_full of board
        # cleaner , uncoupling the structure of Oracle and board.
        if board.is_full(index):
            result = ColumnRecommendation(index, ColumnClassification.FULL)
        return result

 
        
    
class SmartOracle(BaseOracle):
  
    """
       Refina la recomendacion del oracula base, intenta afinar la clasificacion a algo mas preciso.
       En concreto a WIN: va a determinar que jugadas nos llevar a ganar de inmediate
       si llamamos a un metodo primero se busca aqui tdentro de la clase luego a subiendo a las clases padres
   """

    def _get_columns_recommendation(self, 
                                    board: Board, 
                                    index: int,
                                      player)->ColumnRecommendation:
       
       """
        Checks recommendation classified as MAYBE for a possible WIN for player.
       """
       #Get  basic recommendation
       recommendation =  super()._get_columns_recommendation(board, index, player)
       
       #if the classification of that recommendation is maybe:
       if recommendation.classification == ColumnClassification.MAYBE:
          
          #Variable that points to a temporal board with a "new move"
          temp_board_with_play = self._play_on_temp_board(board,index,player.char)
          
          #if on that temp board with the added move is_victory == True
          if temp_board_with_play.is_victory(player.char):
           
           #recommendation gets changed from MAYBE to WIN
           recommendation = ColumnRecommendation(index, ColumnClassification.WIN)
       
       return recommendation
    def _play_on_temp_board(self, original:Board,index:int, player_char):
       
       """
      Creates a DEEPCOPY as to not change our "actual" board, plays on it and returns the altered 
      board to be checked for possible victory
       """
       temp_board = copy.deepcopy(original)
       temp_board_play = temp_board.add(player_char,index)
       return temp_board_play
       




#NEED to check better placement - issues with imports
#COURSE : Change __eq__ only compare class not index - change testing euality - are_same checks only normal lists
def are_same(list_elements:list[ColumnRecommendation])->bool:
   
   """
   Checks if all elements of a list are the same
   """
   result = True
   comparing_element = list_elements[0].classification
   print(comparing_element)

   for el in list_elements:
      if el.classification != comparing_element:
         print(el.classification)
         result = False
         break
   return result 
