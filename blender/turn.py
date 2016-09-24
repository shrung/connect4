import bge
import bpy
from blendergame import *

def turn():
    cont = bge.logic.getCurrentController()
    for sens in cont.sensors:
            if not sens.positive:
                return
    sources = cont.actuators
    for i in sources:
        i.object = "Piece.001"
        
    play = bge.TheGame.TakeTurn()
    print(play," ",bge.TheGame._turnnumber)
    cont.activate(sources[play])
turn()