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
  #Esta clase no es especialmemnte inteleginte, podriamos usar una tupla pero queremos practicar clases
    def __init__(self, index:int, classification: ColumnClassification):
        self.index = index
        self.classification = classification

        #Va a recibir a self y a other, el otro objeto con el que va a comparar
    def __eq__(self,other):
       
       #si son de clases distantas, pues distintos
       #Estas instancias son de la misma clase?
       if not isinstance(other, self.__class__):
          return False
       #si son de la misma clase, pues compara las propiedades de unoy y otro
       else:
          return (self.index, self.classification) == (other.index, other.classification)
       

#Oraculos, de mas tonto a mas lostp
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
       Medodo privado, que determina si una columna esta llena, en cuyo caso la clasifica
       como Full. Para todo lo demas, Maybe.
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
       Afina las recomendaciones. Las que hayan salido como Maybe intento ver si hay algo mas 
       preciso, en concreto una victoria para player.
       """
       #pido la clasificacion basica 
       recommendation =  super()._get_columns_recommendation(board, index, player)
       #Afino los Maybe: juego como player en esa columna y compruebo si eso me da una victoria
       if recommendation == ColumnClassification.MAYBE:
          #creo un tablero temporal a partir de board
          #juego en un index
          # le pregunto a tablero temporal si is_victory(player)
          #si es asi, reclasifico a WIN
          #Importantisimo hacer una copia de board (DEEPCOPY) para no alterar el board (datos compuestos,
          #same same as listas. Apuntan al mismo sitio)
        if board.is_victory(self._play_on_temp_board(board,index,player)):
           recommendation = ColumnRecommendation(index, ColumnClassification.WIN)
        return recommendation
    def _play_on_temp_board(self, original:Board,index:int, player):
       
       """
       Crea una DEEPCOPY del board original juega en nombre de player en la columna que nos
       ha dicho y devuelve el board resultante.
       """
       temp_board = copy.deepcopy(original)
       return (temp_board.add(player,index))
       


    
    # def winning_moves(self, board:Board, index:int, player:Player):

        # """
        # Recibe una copia del board actual, y comprueba todas las columnas en busca de una victoria inminent
        # """
        #  #Unsure que resultado debe devolver si no es win
        # result = ColumnRecommendation
        # #Itera sobre todo el board y por cada columna le pasamos el player y llamamos al metodo is_victory
        # for i in range(board):
        #     if board.is_victory(board.play(player, i)):
        #      result = ColumnRecommendation(index, ColumnClassification.WIN)
        #      return result

