import bge
from blenderplayer import *
from blendergame import *

Player1 = randomplayer()
Player2 = randomplayer()
bge.TheGame = blendergame(Player1,Player2)

