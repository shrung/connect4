from game import*
from player import* 
import random
import math

class tournament():
    def __init__(self,Player_list):
        self._playerlist = Player_list
        self._numplayers = len(self._playerlist)
        self._numrounds = math.log(self._numplayers,2)
        self._currentround = 1
        self._seedtracker = -1
        self._seeds = [0]*self._numplayers
        


    def RunTournament(self):
        self._AssignSeeds()
        champion = self._Thing()
        print("Our tournament winner is ", champion.GetName())        

    def _AssignSeeds(self):
        availableseeds = [0]*self._numplayers
        playersremaining = self._playerlist
        for i in range(0,self._numplayers-1):
            numremain = self._numplayers-1-i
            pick = random.randint(0,numremain)
            self._seeds[i] = playersremaining[pick]
            del playersremaining[pick]

    def _PlayMatch(self,player1,player2):
        Players = [player1,player2]
        Match = game(player1,player2)
        winner = Players[Match.GetGameState()]
        return winner

    def _Thing(self):
        if (self._currentround!= self._numrounds):
            self._seedtracker += 2
            return self._PlayMatch(self._seeds[self._seedtracker],self._seeds[self._seedtracker])
        else:
            return self._PlayMatch(self._Thing(),self._Thing())


            
