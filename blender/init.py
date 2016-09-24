import bge
from blenderplayer import *
from blendergame import *

Player1 = blenderhuman()
Player2 = randomplayer()
bge.state = 1
bge.play = 0
bge.win = -1
bge.finished = False
bge.TheGame = blendergame(Player1,Player2)

