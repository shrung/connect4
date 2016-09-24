import bge
import copy
from blenderplayer import *
from blendergame import *

Player1 = copy.deepcopy(bge.playerlist[bge.player1])
Player2 = copy.deepcopy(bge.playerlist[bge.player2])
bge.state = 1
bge.play = 0
bge.win = -1
bge.finished = False
bge.TheGame = blendergame(Player1,Player2)

