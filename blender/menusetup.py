import bge
from blenderplayer import *

bge.playerlist = []
bge.playerlist.append(humanplayer())
bge.playerlist.append(randomplayer())
bge.playernames = []
for player in bge.playerlist:
    bge.playernames.append(player.GetName())
bge.player1 = 0
bge.player2 = 0