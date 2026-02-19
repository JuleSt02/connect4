from .board import Board
from .oracle import BaseOracle, ColumnRecommendation, ColumnClassification, are_same, SmartOracle
from .player import Player


#TEST BASE ORACLE 

def test_base_oracle():

    #Creamos un test board con el classmethod from_List para no modificar sin querer nuestro
    #board original
    board = Board.from_list([["x", None, None, None],
                                ["x","x","o","x"],
                                ["x","o","x","x" ],
                                ["x",None,None, None]])
    
    
    #Creamos una instancia del BaseOracle
    rappel = BaseOracle()
    
    #Resultados esperados por nuestro BaseOracle, dos columnas llenas las otras serian un Maybe
    expected = [ColumnRecommendation(0, ColumnClassification.MAYBE),
                ColumnRecommendation(1, ColumnClassification.FULL),
                ColumnRecommendation(2, ColumnClassification.FULL),
                ColumnRecommendation(3, ColumnClassification.MAYBE)]
    
    #Si el tablero tiene longitud n, tenemos que obtener una lista recomendaciones de n elementos
    assert len(rappel.get_recommendation(board, None))== len(expected)
    assert rappel.get_recommendation(board, None) == expected

# def test_equality():
    
#     cr = ColumnRecommendation(2, ColumnClassification.MAYBE)
    
#     #same same
#     assert cr == cr 

#     #same same but different. Equivalentes. Hay que ajustar esto con metodo __eq__ para
#     #que el programa pueda reconocer estas equivalencias entre objetos que tengan el mismo valor
#     #Otro objeto con mismos valores
#     assert cr == ColumnRecommendation(2, ColumnClassification.MAYBE) 
#     assert cr == ColumnRecommendation(3, ColumnClassification.MAYBE)
#     #no equivalntes
#     assert cr != ColumnRecommendation(1, ColumnClassification.FULL)
#     assert cr != ColumnRecommendation(2, ColumnClassification.FULL)


# def test_are_same():

#     list_recommendations1 = [ColumnRecommendation(0, ColumnClassification.MAYBE),
#                 ColumnRecommendation(1, ColumnClassification.FULL),
#                 ColumnRecommendation(2, ColumnClassification.FULL),
#                 ColumnRecommendation(3, ColumnClassification.MAYBE)]
#     list_recommendations2 = [ColumnRecommendation(0, ColumnClassification.MAYBE),
#                 ColumnRecommendation(1, ColumnClassification.MAYBE),
#                 ColumnRecommendation(2, ColumnClassification.MAYBE),
#                 ColumnRecommendation(0, ColumnClassification.MAYBE)]
    
#     assert are_same(list_recommendations1) == False
#     assert are_same(list_recommendations2)



#TEST SMART ORACLE

def test_smart_oracle():

    player_test = Player("Robocop", "x")
    player_test2 = Player("Vader", "o")
    player_test.opponent = player_test2
    
    board = Board.from_list([["x", None, None, None],
                            ["x","x",None, None],
                            ["o","o",None ,None ],
                            ["x",None,None, None]])
    
    rappel = SmartOracle()
    expected = [ColumnRecommendation(0, ColumnClassification.LOSE),
                ColumnRecommendation(1, ColumnClassification.WIN),
                ColumnRecommendation(2, ColumnClassification.WIN),
                ColumnRecommendation(3, ColumnClassification.LOSE)]
    
    assert rappel.get_recommendation(board, player_test) == expected
    
def test_is_wining_move():
    winner = Player("Robocop", "x")
    loser = Player("Vader" , "o")

    empty = Board.from_list([[None, None, None, None],
                            [None,None,None, None],
                            [None, None ,None ,None ],
                            [None,None,None, None]])
    
    almost = Board.from_list([["x", None, None, None],
                            ["x","x",None, None],
                            ["o","o",None ,None ],
                            ["x",None,None, None]])
    
    oracle = SmartOracle()
    
    assert oracle._is_winning_move(empty, 0, winner) == False
    assert oracle._is_winning_move(empty, 1, loser) == False
    assert oracle._is_winning_move(almost, 1, winner) == True
    assert oracle._is_winning_move(almost, 1, loser) == False
    assert oracle._is_winning_move(almost, 2, winner) == True


  
def test_is_losing_move():

    player1 = Player("Robocop", "x")
    player2 = Player("Vader", "o")

    player1.opponent = player2

    lost = Board.from_list([["o", "o", None, None],
                            ["x","x",None, None],
                            ["o",None,None ,None ],
                            ["x",None,None, None]])
        
    lost2 = Board.from_list([["x", None, None, None],
                            ["x","x",None, None],
                            ["o","o",None ,None ],
                            ["x",None,None, None]])
    
    oracle = SmartOracle()
    
    assert oracle._is_losing_move(lost, 0, player1) == False
    assert oracle._is_losing_move(lost, 1, player1) 
    assert oracle._is_losing_move(lost, 2, player1) 
    assert oracle._is_losing_move(lost, 3, player1) 

    assert oracle._is_losing_move(lost2, 0, player1) 
    assert oracle._is_losing_move(lost2, 1, player1)
    assert oracle._is_losing_move(lost2, 2, player1) == False
    assert oracle._is_losing_move(lost2, 3, player1) 



    
#     oracle = SmartOracle()

# def test_is_losing_move():

#     player1 = Player("Robocop", "x")
#     player2 = Player("Vader", "o")

#     lost = Board.from_list([["o", None, None, None],
#                             ["x","o",None, None],
#                             ["o",None,None ,None ],
#                             ["x",None,None, None]])
    
#     oracle = SmartOracle()

#     assert oracle._is_losing_move(lost, 0, player1, player2)
#     assert oracle._is_losing_move(lost, 2, player1, player2)
#     assert oracle._is_losing_move(lost, 1, player1, player2) == False
#     assert oracle._is_losing_move(lost, 3, player1, player2) == False



