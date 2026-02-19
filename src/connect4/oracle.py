#CHECK AND MODIFY

#Clases de columnas, hay varios estados pero siempre puede haber solo uno, por lo tanto ENUM
from enum import Enum, auto
from .board import Board
from .settings import BOARD_COLUMNS 
import copy
from beautifultable import BeautifulTable

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
    Class that represents a recommendation for a column
    It is composed of the index and a classification for that column
    """
  # simple class, could have also been done with a tuple
    def __init__(self, index:int, classification: ColumnClassification):
        self.index = index
        self.classification = classification

        # this method will receive self and other to compare
    def __eq__(self,other):
       
      
       # if they are different classes, False
       if not isinstance(other, self.__class__):
          return False
       #If same class, we check the attribute classification , index attribute  is not relevant for this 
       # if attribute is the same, they are equivalent.
       else:
          return (self.classification) == (other.classification)
       
      

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
    
    def display_recommendations(self,board, player):      
      
      recommendations = self.get_recommendation(board, player)
      bt = BeautifulTable()
      bt.columns.header = [str(i) for i in range(BOARD_COLUMNS)]
    #Extract classifications into a list
      row = [recom.classification.name for recom in recommendations]
    #Append as row
      bt.rows.append(row)
      print(bt)



        
    
class SmartOracle(BaseOracle):
  
    """
      The  evolution of Base Oracle, it not only detects Maybes and Full Boards but 
      winning and losing move.

   """

    def _get_columns_recommendation(self, 
                                    board: Board, 
                                    index: int,
                                      player)->ColumnRecommendation:
       
       """
        Checks recommendation classified as MAYBE for a possible WIN for player.
       """
       #Get  basic recommendation from BaseOracle
       recommendation =  super()._get_columns_recommendation(board, index, player)
       
       #if the classification of that recommendation is maybe:
       if recommendation.classification == ColumnClassification.MAYBE:
          
          #Check if is_winning_move is True and reclassify 
          if self._is_winning_move(board,index, player):
            #recommendation gets changed from MAYBE to WIN
           recommendation = ColumnRecommendation(index, ColumnClassification.WIN)
         #if there is no win check for a losing_move:
          elif self._is_losing_move(board, index, player):
            recommendation = ColumnRecommendation(index, ColumnClassification.LOSE)
          
       return recommendation
    

       
    def _play_on_temp_board(self, original:Board,index:int, player_char):
       
       """
      Creates a DEEPCOPY as to not change our "actual" board, plays on it and returns the altered 
      board to be checked for possible victory
       """
       temp_board = copy.deepcopy(original)
       temp_board_play = temp_board.add(player_char,index)
       return temp_board_play
    
    def _is_winning_move(self, original:Board, index:int, player):
       
       """
       Method that checks if making a move in a given column leads to a win
       """

       #Variable that points to a temporal board with a "new move"
       temp_board_with_play = self._play_on_temp_board(original,index,player.char)
       
       #Use board method is_victory on temp_board_with_play and return its evaluation
       return temp_board_with_play.is_victory(player.char) 
    
    def _is_losing_move(self,original:Board, index:int, player):  
       
       """
       Checks if there is a potential losing move in the index(Column) it receives
       """
       losing_move = False
       # make a move on temporal board 
       temp_board_with_play = self._play_on_temp_board(original, index, player.char)

       # check if after that play, there is an obvious win on the board "left" for our opponent
       for i in range(BOARD_COLUMNS):
        if self._is_winning_move(temp_board_with_play,i,player.opponent):
          
          #if so, losing_move returns True
          losing_move = True
          break
       return losing_move


#NEED to check better placement - issues with imports
#COURSE : Change __eq__ only compare class not index - change testing euality - are_same checks only normal lists
def are_same(list_elements:list[ColumnRecommendation])->bool:
   
   """
   Checks if all elements of a list are the same
   """
   result = True
   comparing_element = list_elements[0].classification

   for el in list_elements:
      if el.classification != comparing_element:

         result = False
         break
   return result 
