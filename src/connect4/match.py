from .player import Player
from .board import Board

class Match():
    """
     Class that receives two players and updated their attribute char to assign them 
     a char for the  match
    """

    def __init__(self, player1: Player, player2: Player):
        
        #The instances of the object Player gets"stored - points to that player instance"
        #Now players are an attribute of match and can be accessed directly through match 
        self.player1 = player1
        self.player2 = player2
        player1._char = "x"
        player2._char = "o"

        #This method will tell us both depending on which player is asking
        player1._opponent = player2
        
        #We create the data structure to store our players
        self._players = {"x" : player1, "o": player2}

        #Since there are only two players  we will create a list and invert it to call one player
        #or the others
        self._round_robbin = [player1, player2]

    @property
    #Decrotaror that helps access methods as if they were attributes
    def next_player(self):
        #Access the first element of the list (player 1)
        next = self._round_robbin[0]
        #Reverses the list
        self._round_robbin.reverse()
        return next
    
    def get_player(self, char):
        #Returns the name of the player( value of dict)
        return self._players[char]

