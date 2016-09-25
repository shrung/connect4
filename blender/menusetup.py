import bge
from blenderplayer import *

#HERE IS WHERE NEW PLAYER TYPES CAN BE ADDED TO THE SELECTION
bge.playerlist = []
bge.playerlist.append(blenderhuman())
bge.playerlist.append(randomplayer())
bge.playerlist.append(strat1player())



bge.playernames = []
for player in bge.playerlist:
    bge.playernames.append(player.GetName())
bge.player1 = 0
bge.player2 = 0