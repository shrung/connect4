from player import *
import bge

class blenderhuman(humanplayer):
    def __init__(self):
        super().__init__() #call humanplayer.__init__
    def TakeTurn(self,board):
        column_choice = bge.play
        print("returning ",column_choice)
        bge.play = -1
        return column_choice
    
