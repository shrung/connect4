from player import*
from game import*

Roy = humanplayer()
Rob = strat1player()
game1 = game(Roy, Rob)
for i in range(1):
    game1.Play()
game1.PrintStats()
