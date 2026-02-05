from .board import Board
from .oracle import BaseOracle, ColumnRecommendation, ColumnClassification

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

def test_equality():
    
    cr = ColumnRecommendation(2, ColumnClassification.MAYBE)
    
    #same same
    assert cr == cr 

    #same same but different. Equivalentes. Hay que ajustar esto con metodo __eq__ para
    #que el programa pueda reconocer estas equivalencias entre objetos que tengan el mismo valor
    #Otro objeto con mismos valores
    assert cr == ColumnRecommendation(2, ColumnClassification.MAYBE) 
    #no equivalntes
    assert cr != ColumnRecommendation(1, ColumnClassification.MAYBE)
    assert cr != ColumnRecommendation(2, ColumnClassification.FULL)


