import bge

cont = bge.logic.getCurrentController()
action1 = cont.actuators["TextEdit1"]
action2 = cont.actuators["TextEdit2"]

go = False
for sens in cont.sensors:
    if sens.positive:
        go = True
        if sens.name == "left":
            bge.player1 +=1
        elif sens.name == "right":
            bge.player1 -= 1 
        elif sens.name == "up":
            bge.player2 +=1
        elif sens.name == "down":
            bge.player2 -=1
if go ==True:
    bge.player1 = bge.player1%len(bge.playerlist)
    bge.player2 = bge.player2%len(bge.playerlist)
    print(bge.player1,bge.player2)
    print(bge.playernames[bge.player1])

    action1.value = '''"'''+bge.playernames[bge.player1]+'''"'''
    action2.value = '''"'''+bge.playernames[bge.player2]+'''"'''
    
    cont.activate(action1)
    cont.activate(action2)
