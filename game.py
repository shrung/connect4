class game():
	def __init__(self, player1, player2):
		self._boarddimx = 8
		self._boarddimy = 8
		self._currentturn = 0
		self._board = [[0]*self._boarddimy]*self._boarddimx
		print(self._board)
		self._lastplay = -1
		self._player1 = player1
		self._player2 = player2
		player1.SetColor(1)
		player2.SetColor(-1)
	def ShowBoard():
	def GetTurnNumber():
	def GetLastPlay():
	def GetBoardDimX():
	def GetBoardDimY():
	
	
	
	
	
