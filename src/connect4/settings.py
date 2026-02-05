"""
Aqui van las constantantes que vamos a utilizar para el tablero
"""

BOARD_COLUMNS = 4
BOARD_ROWS = 4
VICTORY_STREAK = 3




# #def _has_horizontal_victory(self,player_char:str, matrix: MatrixColumn)->bool:   
# Determina si hay una victoria vertical
#     result = False
# #invertimos el board
# inverted = inverted_board(self._columns)   
# #Loop sobre las columnas del Board
# for column in inverted:
#     #Llamamos el metodo has_streak para checar si existe streak en esa columna
#     if has_streak(column, player_char):
#         result = True
#         break
# return result 


# def get_diagonal(matrix)->list[int]:

#   """"
#   Devuelve una lista de los elementos descendientes 
#   """
#   diagonal = []

#   for index,sub_list in enumerate(matrix):
#      diagonal.append(sub_list[index])

#   return diagonal

# def get_diagonal_asc(matrix):

#   """"
#   Devuelve una lista de los elementos diagonales ascendientes
#   """
#   #Invertimos las filas del tablero para poder utilizar get_diagonal
#   return get_diagonal(reversed(matrix))
    # def _has_ascending_victory(self, player_char:str, matrix: MatrixColumn)->bool:     
    #     """
    #     Determina si hay una victoria descendiente
    #     """     
    #     #Obtenemos una lista de los elementos descendientes
    #     diagonal = get_diagonal(matrix)
    #     result = False
    #     #Le pasamos esta lista  has_streak
    #     if has_streak(diagonal, player_char):
    #         result = True
    #     return result