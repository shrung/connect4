import bge
import bpy
from blendergame import *

def turn(play):
    cont = bge.logic.getCurrentController()
    sources = cont.actuators

    for i in sources:
        if bge.state ==0:
            i.object = "Piece.000"
        else:
            i.object = "Piece.001"
    bge.play = play
    play = bge.TheGame.TakeTurn()
    #print(play," ",bge.TheGame._turnnumber)
    name = "Piece"+str(play+1)
    cont.activate(sources[name])
    if bge.state == 0:
        bge.state = 1
    else:
        bge.state = 0

        
cont = bge.logic.getCurrentController()
play = -2
for sens in cont.sensors:
        if sens.positive:
            if sens.name == "1":
                play = 0
            elif sens.name == "2":
                play = 1
            elif sens.name == "3":
                play = 2
            elif sens.name == "4":
                play = 3
            elif sens.name == "5":
                play = 4
            elif sens.name == "6":
                play = 5
            elif sens. name == "7":
                play = 6                  
            elif sens.name == "AI":
                play = -1
if play != -2:
    if not bge.finished:
        if (bge.TheGame._players[bge.TheGame._currentplayer].GetName() != "A Real Person" and play ==-1 )or bge.TheGame.IsValid(play):
            turn(play)