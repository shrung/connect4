from player import*

class game():
	def __init__(self, player1, player2, boardx=7, boardy=6):
		self._boarddimx = boardx
		self._boarddimy = boardy
        # board is in row column format (0,0 is the top left), -1 is empty space
		self._board = [[-1]*self._boarddimy]*self._boarddimx
		#print(self._board)
		self._lastplay = -1
		self._players = [player1,player2]
		self._players[0].SetColor(0)
		self._players[1].SetColor(1)
		self._currentplayer = 0	
		self._turnnumber = 0
		self._gamewon = -1
		self._boardfull = False
	def ShowBoard(): print(self._board)
	def GetTurnNumber(): return self._turnnumber
	def GetLastPlay(): return self._lastplay
	def GetBoardDimX(): return self._boarddimx
	def GetBoardDimY(): return self._boarddimy

	def GetGameState(): return self._gamewon

	def _CheckGameWin(self):
        full = True
        wins = [False,False]
        for space in self._board[0]:
            if space == -1
                full = False
        self._boardfull = full
        for column in range(self._boarddimx):
            for row in range(self._boarddimy):
                # looping over entire board, checking for a filled in space to start from
                if (self._board[row][column] != -1:
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
                        if(row+i<self._boarddimx):
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
                        if(column+i<self._boarddimy) and (row+i<self._boarddimx):
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
                        if(column-i<-1) and (row+i<self._boarddimx):
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
        
        retrun False
        
        
	def _Reset:

	def _
	
	def Play():
		while (!self._gamewon):
			PlayColumn = self._players[self._currentplayer].TakeTurn(self._board)
			if (PlayColumn<0 or PlayColumn>=self._boarddimx or self._board[PlayColumn[self._boarddimy]]!=0):
				print("That was an illegal play.  I give up!") 
				return
			else:
				i = 0
				while (self._board[PlayColumn[0]!=0):
					i=i+1
				self._board[PlayColumn[i]]=currentplayer
			if 
	
	
	
	
