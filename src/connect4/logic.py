
from .settings import BOARD_ROWS, BOARD_COLUMNS,VICTORY_STREAK
from typing import Any

def inverted_board(matrix):
  """"
  Devuelve el board invertido, transformando las filas en columnas
  """
  inverted = []
  #Creamos un loop y en cada loop llamamos a la funcion new_list que nos devolvera los elementos i de cada lista
  for i in range(len(matrix)):
      inverted.append(get_first_element(matrix,i))
  return inverted
    

def get_first_element(matrix,index:int)->list[int]:
  
  """
  Devuelve el primer elemento de las rows de Board
  """
  first_element = []
  for sub_list in matrix:
     first_element.append(sub_list[index])
      
  return first_element

    
def has_streak(col, player_char)->bool:

    """
    Recibe una columna y el player_char y determina si hay un streak de 3.
    """ 
    #Counter comienza en 0 y result inicia en False
    counter = 0
    result = False
    #Loop sobre la columna
    for item in col:
        
        #Si el item es igual al player_char counter aumenta
        if item  == player_char:
            counter += 1
        #Si item no es igual al player_char reseteamos counter     
        else:
            counter = 0
        #Si el counter es igual a 3, has_streak es True. Break y devolvemos
        if counter == VICTORY_STREAK:
            result = True
            break
    return result 


def add_filler(filler,number)->list:
  
  """
  Devuelve filler 
  """
  return [filler] * number

def displace_matrix(matrix, filler):
 
  """
Devuelve una matriz "desplazada" con filler
  """
#Longitud, numero de columnas (listas) de la matriz
  len_m = len(matrix) 
  new_m = []
 
 #Recorremos la matriz
  for index,sub_list in enumerate(matrix):

    #El prefix que hay que añadirle es el indice, columna 0 recibe 0 prefix
    prefix = add_filler(filler, index)

    #El suffix es la longitud de la matriz menos uno menos el indice. 
    #La primera columna que no recibe prefix (no se mueve) se le añade 3x unidades de suffix
    suffix = add_filler(filler, (len_m - 1 - index))
    new_m.append(prefix + sub_list + suffix)
  return new_m


def reverted_list(l):
   #Invertimos una lista usando reversed que tiene que ser transformado a lsita ya que devuelve
   #un reverse iterator
   return list(reversed(l))

def reverted_matrix(m):

   reverted_m = []
   for col in m:
      reverted_m.append(reverted_list(col))
   return reverted_m


#CHECK HUMAN INPUT

def is_int(iput):
    try: 
        transf = int(iput)
        return type(transf) == int
    except:
       return False

def is_col_range(input):
    return int(input) in range(0,4)


def is_valid(input, board):
    #Validate the input
    #It needs to be an int
    #Between 0-4
    #Column needs to be not full
  
    return (is_int(input)) and (is_col_range(int(input))) and not column_full(int(input), board) 
    

def column_full(input, board):

   return board.is_full(input)      
        


# def add_prefix(number:int, filler:Any)->list:
   
#    """
#   Recibe una lista y devuelve una nueva lista con number rellenos al principio
#    (un prefijo)
#    add_prefix([1,2], 2 , None)->[None,None ,1, 2]
#    """
#    #Podriamos utilizar insert pero es destructivo
#    #Otra opcion seria multiplicar EJ None * 3 + lista
#    return ([filler] * number) 

# def add_suffix(number:int, filler:Any)-> list:
   
#    """
#    Rebie una lsita y devuelve una nueva liS
#    add_suffic([1,2], 2 , None)->[1,2 None,None]
#    """
#    return ([filler] * number)

# def displace_list(elements:list, distance:int, total_size:int, filler:Any)->list:
#    """
#     Crea una nueva lista de tamaño total_size con la original, desplazada hacia 
#     el final distance posiciones.
#     Los espacios nuevos se rellenan con filler
#     displacae_list([1,2,3] 1, 7, None) -> devolvera una nueva lista de longitud 7 
#     -> [None, 1, 2, 3, None, None, None]
#     """
#    el_suffix = total_size - distance - len(elements)
#    return add_prefix(distance, filler) + elements + add_suffix(el_suffix, filler)


# def displace_lol(matrix:list[list], total_size:int=7, filler:Any=None)->list[list]:
#    extended = []
#    for index,sub_list in enumerate(matrix):
#       extended.append(displace_list(sub_list, index, total_size, filler))
#    return extended
                                                      

 



