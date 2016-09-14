from player import*

class game():
	def __init__(self, player1, player2):
		self._boarddimx = 7
		self._boarddimy = 6
		self._board = [[-1]*self._boarddimy]*self._boarddimx
		#print(self._board)
		self._lastplay = -1
		self._players = [player1,player2]
		player1.SetColor(1)
		player2.SetColor(-1)
		self._currentplayer = 0	
		self._turnnumber = 1
		self._gamewon = -1
		self._boardfull = 0
	def ShowBoard(): print(self._board)
	def GetTurnNumber(): return self._turnnumber
	def GetLastPlay(): return self._lastplay
	def GetBoardDimX(): return self._boarddimx
	def GetBoardDimY(): return self._boarddimy

	def _CheckGameWin(self):

	def _Reset(): 
		self._board = [[-1]*self._boarddimy]*self._boarddimx
		self._lastplay = -1
		self._currentplayer = 0	
		self._turnnumber = 1
		self._gamewon = -1
		self._boardfull = 0

	def _CheckBoardFull(self):
	
	def Play():
		_Reset()
		counter = 0 
		while (not(self._gamewon!=-1 or self._boardfull) and counter <10):
			PlayColumn = self._players[self._currentplayer].TakeTurn(self._board)
			if (PlayColumn<0 or PlayColumn>=self._boarddimx or self._board[PlayColumn[self._boarddimy]]!=0):
				print("That was an illegal play.  I give up!") 
				return
			else:
				i = 0
				while (self._board[PlayColumn[0]!=0):
					i=i+1
				self._board[PlayColumn[i]]=self._currentplayer
				if (self._currentplayer==0):
					self._currentplayer = 1
				else:
					self._currentplayer = 0
				self._turnnumber = self._turnnumber + 1
				self._lastplay = PlayColumn
				counter = counter + 1
			if (_CheckGameWin(self)):
				if (self._gamewon==-1):				
					print("It was a draw!")
					return
				else: 
					print("Player",self._currentplayer,"has won!")
					return
			








	
