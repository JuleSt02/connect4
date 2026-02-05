from .settings import BOARD_ROWS, BOARD_COLUMNS, VICTORY_STREAK
from .logic import inverted_board,  has_streak, reverted_matrix, displace_matrix
from copy import deepcopy
type MatrixColumn = list[list[str|None]]

class Board:
    """
    Respresenta un tablero con las dimensiones de settings
    Detecta una victoria
    EL tablero es una "matriz" de caracteres del jugador  y None representa 
    una posicion vacia
    Cada lista es una columna y el fondo es el principio

    """  
    @classmethod
    def from_list(cls, columns):

        """

        """ 
        #Este classmethod ejecuta un init que crea un tablero vacio 
        board = cls()
        #Creamos una deepcopy
        board._columns = deepcopy(columns)
        return board
    
    def __init__(self)-> None:
        """
        Crea un tablero con las dimensiones adecuadas
        """
        #Podemos crear una lista llamada columnas que sera la especie de matriz, cada elemento de esa
        #lista sera un monton de Nones. 
        self._columns = self.create_board()
    
    
    def __eq__(self,value:object)->bool:

        """
        Se ejecuta cuando haces a == b
        siendo a self y b value
        """
        #Self sabemos que es board, somos nosotros estamos en la clase board. 
        #primero hay que comprobar si value, es del mismo tipo que yo
        #para eso se utiliza esta funcion propia de P isinstance()

        #Esto es un contrato
        result = True
        if not isinstance(value, self.__class__):
            result = False
        else:
            #son de la misma clase: comparo sus propiedades
            # en este caso, _columns
            result = (self._columns == value._columns)
        return result
   
    def __hash__(self)-> int:

        # Si estuvieramos comparando usuarios por ejemplpo comparariamos los nombres
        #dataclass es un decorador para decirle a Python : el eq y el hash lo generas tu en 
        #base al init-. 
        return hash(self._columns)

    
    def __repr__(self)->str:
        """
        Repr permite printear el estado del nuestro objeto
        Sintaxis !r para sobreescribir __str__ si lo añadimos 
        """
       # inverted = inverted_board(self._columns)
        return f"Board({(self._columns)}"
    
    def __len__(self):
        """
        Magical method we can use to get the length of every object, also classes
        """
        return len(self._columns)

    
    def __str__(self)->str:

        inverted = inverted_board(self._columns)
        #Convertimos en str para dar saltos de linea
        text = ""
        for row in inverted:
          text += str(row) + "\n"
        #Elimina el ultimo salto de linea, lo deja limpio
        return text.rstrip("\n")
    
    def create_board(self):    
        #Version compacta de for loop en range BOARD_COLUMNS que en cada loop crea una nueva row con None
        return [[None] * BOARD_ROWS for _ in range(BOARD_COLUMNS)]
    

    def is_full(self,index)->bool:
        """
      Receives an index and checks within its own attribute self._columns if that column(index)´s
      last element is != None in which case is_full is True.
    
        """
        return self._columns[index][-1] != None
        # result = False
        # if col[-1] != None:
        #     result = True
        # return result
        
    def add(self,player_char, col_number:int):
    #Pecadora, impura ya que cambia la matriz

        """
        Metodo impuro solo lleva a cabo efecto secundarios (cambia el tablero)
        SI col_number no es valido, debe lanzar excepcion
        ValueError si la columna esta llena o si el indice es de una columna inexsitente
        """
        #Eliges una columna y tenemos que ir buscando dodne esta el primer  None y ahi metemos
        #la ficha 
        #Cada codigo que pueda tener un error debe ir en try, aunque ya lo cogera otro.
        try:

            chosen_column = (self._columns[col_number])
            found_slot = False
            for index, item in enumerate(chosen_column):
                if item == None:
                    found_slot = True
                    chosen_column[index] = player_char
                    break
    
                
        except IndexError:
         raise ValueError(f"No exise {col_number}")
            
        if not found_slot:
            #no he encontrado ningun slot vacio, (hay que recorrer la lista entera hasta elfinal)
            raise ValueError(f"Ya hay una ficha aqui")
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
        Determina si hay una victoria vertical.           
        """
        #Loop sobre las columnas del Board
        result = False
        for column in matrix:
            result = has_streak(column, player_char)
            if result:
                break
        return result
         
    def _has_horizontal_victory(self,player_char:str, matrix)->bool:    
        """
        Determina si hay una victoria horizontal
   
        """
        inverted = inverted_board(matrix)
        return self._has_vertical_victory(player_char, inverted)    
    
    def _has_descending_victory(self, player_char:str, matrix)->bool:     
        """
        Determina si hay una victoria ascendiete
        """     
        #Primero hay que invertir el board para que las filas sean columnas
        #Despues hay que que añadir un padding de un lado y otro para desplazar 

        transformed = displace_matrix(matrix,None)
        return self._has_horizontal_victory(player_char, transformed)
       
        
    def _has_ascending_victory(self, player_char:str, matrix)->bool:      
        """
        Determina si hay una victoria descendiente
                diagonal = get_diagonal_asc(matrix)
        pass
        """
        desc_transformed = reverted_matrix(matrix)
        return self._has_descending_victory(player_char,desc_transformed)
    
    
