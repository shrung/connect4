from player import*

class game():
    def __init__(self, player1, player2, boardx=7, boardy=6):
        self._boarddimx = boardx
        self._boarddimy = boardy
        # board is in row column format (0,0 is the top left), -1 is empty space
        self._board = []
        for i in range(0,boardy):
            self._board.append([])
            for j in range(0,boardx):
                self._board[i].append(-1)
        self._lastplay = -1
        self._players = [player1,player2]
        self._players[0].SetColor(0)
        self._players[1].SetColor(1)
        self._currentplayer = 0    
        self._turnnumber = 1
        self._gamewon = -1
        self._boardfull = False
    def ShowBoard(self):
        for i in range(self._boarddimx):
            if i == self._lastplay:
                print("v",end = " ")
            else:
                print(" ", end = " ")
        print("")
        for row in self._board:
            for space in row:
                if space == 0:
                    print("0", end = " ")
                elif space == 1:
                    print("1",end = " ")
                else:
                    print(".",end = " ")
            print("")
        print("")
    def GetTurnNumber(self): return self._turnnumber
    def GetLastPlay(self): return self._lastplay
    def GetBoardDimX(self): return self._boarddimx
    def GetBoardDimY(self): return self._boarddimy
    def _Reset(self): 
        for row in self._board:
            for space in row:
                space = -1
        self._lastplay = -1
        self._currentplayer = 0    
        self._turnnumber = 1
        self._gamewon = -1
        self._boardfull = 0
    def GetGameState(self): return self._gamewon

    def _CheckGameWin(self):
        full = True
        wins = [False,False]
        for space in self._board[0]:
            if space == -1:
                full = False
        self._boardfull = full
        for column in range(self._boarddimx):
            #print("Checking column "+str(column))
            for row in range(self._boarddimy):
                # looping over entire board, checking for a filled in space to start from
                if self._board[row][column] != -1:
                    color = self._board[row][column]
                    #Checking for a horizontal win going right from this space
                    for i in range(1,4):
                        if(column+i<self._boarddimy):
                            if self._board[row][column+i] != color:
                                break
                            if i==3:
                                wins[color] = True
                        else:
                            break
                    if(wins[0] or wins[1]):
                        break
                    #Checking for a vertical win going down from this space
                    for i in range(1,4):
                        if(row+i<self._boarddimy):
                            if self._board[row+i][column] != color:
                                break
                            if i==3:
                                wins[color] = True
                        else:
                            break
                    if(wins[0] or wins[1]):
                        break
                    #Checking for a diagonal win going down-right
                    for i in range(1,4):
                        if(column+i<self._boarddimx) and (row+i<self._boarddimy):
                            if self._board[row+i][column+i] != color:
                                break
                            if i==3:
                                wins[color] = True
                        else:
                            break
                    if(wins[0] or wins[1]):
                        break
                    #Checking for a diagonal win going down-left
                    for i in range(1,4):
                        if(column-i>-1) and (row+i<self._boarddimy):
                            if self._board[row+i][column-i] != color:
                                break
                            if i==3:
                                wins[color] = True
                        else:
                            break
                    if(wins[0] or wins[1]):
                        break
            if (wins[0] or wins[1]):
                break
        if wins[0]:
            self._gamewon = 0
            self._players[0].CountWin()
            self._players[1].CountLoss()
            return True
        if wins[1]:
            self._gamewon = 1
            self._players[1].CountWin()
            self._players[0].CountLoss()
            return True
        
        if full:
            return True
        
        return False
        
    def Play(self):
        self._Reset()
        #counter = 0 
        while True:
            PlayColumn = self._players[self._currentplayer].TakeTurn(list(list(row) for row in self._board))
            if (PlayColumn<0 or PlayColumn>=self._boarddimx):
                print("That was out of the board.  I give up!") 
                return
            elif self._board[0][PlayColumn]!=-1:
                print("That was an illegal play.  I give up!") 
                return
            else:
                for i in range(0,self._boarddimy):
                    if self._board[self._boarddimy-(i+1)][PlayColumn] == -1:
                        self._board[self._boarddimy-(i+1)][PlayColumn] = self._currentplayer
                        break
                if (self._currentplayer==0):
                    self._currentplayer = 1
                else:
                    self._currentplayer = 0
                self._turnnumber = self._turnnumber + 1
                self._lastplay = PlayColumn
                #counter = counter + 1
            self.ShowBoard()
            if (self._CheckGameWin()):
                if (self._gamewon==-1):                
                    print("It was a draw!")
                    return
                else: 
                    print("Player ",self._gamewon," has won!")
                    return
            








    
