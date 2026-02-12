from .settings import BOARD_ROWS, BOARD_COLUMNS, VICTORY_STREAK
from .logic import inverted_board,  has_streak, reverted_matrix, displace_matrix
from copy import deepcopy
type MatrixColumn = list[list[str|None]]

class Board:
    """
    Represents a board with the dimensions defined in settings
    Detects a victory
    The board is a “matrix” of player characters, and None represents an empty position
    Each list is a column, and the bottom is the starting point
    """  
    @classmethod
    def from_list(cls, columns):

        """

        """ 
        #Classmethos that creates an empty board
        board = cls()
        #Creamos una deepcopy
        board._columns = deepcopy(columns)
        return board
    
    @property
    def columns(self):
        """
        Exposes this attribute so others have access to it but only a copy
        of the original object so that the original object can´t and its internal state 
        can´t be modified
        """
        return deepcopy(self._columns)
    
    def __init__(self)-> None:
        """
        Creates a board
        """
        #A matrix will represent our Board
        self._columns = self.create_board()
    
    
    def __eq__(self,value:object)->bool:

        """
        It executes doing a == b
        A is self, b is the value
        """
         # refers to the board; we are inside the Board class.
         # First, we need to check whether value is of the same type as this object
         # For that, we use Python’s built-in function isinstance().

        #This is like a contract
        result = True
        if not isinstance(value, self.__class__):
            result = False
        else:
            ##if they are the same class i will compare their values
            result = (self._columns == value._columns)
        return result
   
    def __hash__(self)-> int:
       
       # If we were comparing users, for example, we would compare their names.
       # @dataclass is a decorator that tells Python to generate `__eq__` and `__hash__`
       # automatically based on the __init__ attributes.
        return hash(self._columns)

    
    # def __repr__(self)->str:
    #     """
    #     Repr lets us print the state of our object
       
    #     """
    #    # inverted = inverted_board(self._columns)
    #     return f"Board({(self._columns)}"
    
    def __len__(self):
        """
        Magical method we can use to get the length of every object, also classes
        """
        return len(self._columns)

    
    # def __str__(self)->str:

    #     inverted = inverted_board(self._columns)
    #     reverted = reverted_matrix(inverted)
    #     #Convert into str to apply /n
    #     text = ""
    #     for row in reversed(inverted):
    #       text += str(row) + "\n"
    #     #Cleans last /n
    #     return text.rstrip("\n")
    
    def create_board(self):    
        return [[None] * BOARD_ROWS for _ in range(BOARD_COLUMNS)]
    

    def is_full(self,index)->bool:
        """
      Receives an index and checks within its own attribute self._columns if that column(index)´s
      last element is != None in which case is_full is True.
    
        """
        return self._columns[index][-1] != None
      
    def all_full(self)->bool:
        result = False
        counter = 0
        for i in range(len(self._columns)):
            if self.is_full(i):
                counter += 1
        if counter == len(self._columns):
         result = True
        return result

    def add(self,player_char, col_number:int):
    # Pecadora : impure because it changes the matrix

        """
      Impure method: it only produces side effects (it changes the board).
      If col_number is not valid, it must raise an exception.
     Raise ValueError if the column is full or if the index refers to a non-existent column.
        """
        # You choose a column, and we have to look for the first `None`; that’s where we drop the piece.
        # Any code that could raise an error should go inside a try block, even if another part will catch it
        try:

            chosen_column = (self._columns[col_number])
            found_slot = False
            for index, item in enumerate(chosen_column):
                if item == None:
                    found_slot = True
                    chosen_column[index] = player_char
                    break
                
        except IndexError:
         raise ValueError(f"This column does not exist: {col_number}")
            
        if not found_slot:
            # hasn´t found a slot, has to go over the whole list
            raise ValueError(f"This slot is full")
        return self._columns
        
 
    def is_victory(self, player_char: str)-> bool:
        """
        Determina si hay una victoria para jugador
        representado por un caracter 
        """
        
        #METERLE AQUI el if has vertical vitory : (print) y asi con todas para que
        #Siempre e vea el resultado
        #Comprueba si se cumple alguna de las posibles victorias verticales/horizontales o diagonales.

        # if self._has_vertical_victory(player_char, self._columns):
        #     print("VERTICAL VICTORY")
        # elif self._has_horizontal_victory(player_char, self._columns):
        #     print("HORIZONTAL VICTORY")
        # elif self._has_ascending_victory(player_char, self._columns):
        #     print("ASCENDING VICTORY")
        # elif self._has_descending_victory(player_char, self._columns):
        #     print("DESCENDING VICTORY")

        return (self._has_vertical_victory(player_char, self._columns) or
                 self._has_horizontal_victory(player_char, self._columns) or
                 self._has_ascending_victory(player_char, self._columns) or 
                 self._has_descending_victory(player_char, self._columns))
    
      #Interfaz privada
      #Paco
    def _has_vertical_victory(self,player_char:str, matrix)->bool:
        """
       Determines whether there is a vertical win.      
        """
        #Loop over cols of board
        result = False
        for column in matrix:
            result = has_streak(column, player_char)
            if result:
                break
        return result
         
    def _has_horizontal_victory(self,player_char:str, matrix)->bool:    
        """
        Determines whether there is a horizontal win
   
        """
        inverted = inverted_board(matrix)
        return self._has_vertical_victory(player_char, inverted)    
    
    def _has_descending_victory(self, player_char:str, matrix)->bool:     
        """
       Determines whether there is an ascending (diagonal) win.
        """     
        # invert the board 
        # add padding
        transformed = displace_matrix(matrix,None)
        return self._has_horizontal_victory(player_char, transformed)
       
        
    def _has_ascending_victory(self, player_char:str, matrix)->bool:      
        """
        Determines whether there is an descending (diagonal) win.
    
        """
        desc_transformed = reverted_matrix(matrix)
        return self._has_descending_victory(player_char,desc_transformed)
    
    
