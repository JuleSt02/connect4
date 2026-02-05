#Aqui tambien se pueden hacer experimentos. Comprobar creando una seucnecia que si yo creo un board
#tiene realmente lo que yo quiero si juego en un lugar lo muestra bien (entra en la pos y columna correcta)


from .settings import BOARD_ROWS, BOARD_COLUMNS, VICTORY_STREAK
from .logic import inverted_board,  has_streak 
from .board import Board

# if __name__ == "__main__":
#     pass

# b2 = Board()

# # Columna 1
# b2.play("o", 1)
# b2.play("x", 1)
# # Columna 2
# b2.play("o", 2)
# b2.play("o", 2)
# b2.play("x", 2)
#  # Columna 3
# b2.play("o", 3)
# b2.play("o", 3)
# b2.play("o", 3)
# b2.play("x", 3)


# print(b2)

# print(b2.is_victory("o"))