import bge
cont = bge.logic.getCurrentController()

if bge.finished == True:
    cont.activate(cont.actuators["end"])
    if bge.win == -1:
        cont.activate(cont.actuators["draw"])
    if bge.win == 0:
        cont.activate(cont.actuators["player1"])
    if bge.win == 1:
        cont.activate(cont.actuators["player2"])
        