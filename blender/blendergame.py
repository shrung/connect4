from game import *
import bge


class blendergame(game):
    def __init__(self,player1,player2, boardx = 7,boardy = 6):
        super().__init__(player1,player2,boardx,boardy)
    def IsValid(self, play):
        if play < 0 or play >= self._boarddimx:
            return False
        if self._board[0][play] == -1:
            return True
    def TakeTurn(self):
        print("taking turn ",str(bge.play))
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
            if (self._CheckGameWin()):
                bge.finished = True
                bge.win = self._gamewon
            return PlayColumn
