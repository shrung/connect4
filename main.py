from player import*
from game import*

Roy = randomplayer()
Rob = randomplayer()
game1 = game(Roy, Rob)
for i in range(100000):
    game1.Play()
game1.PrintStats()
