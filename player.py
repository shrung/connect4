# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:31:45 2016

@author: Roy
"""
import random

import fileinput

class player():
    def __init__(self):
        self._color = 0
        self._numwins = 0
        self._numlosses = 0
        self._name = 'default player'
        
    def GetName(self):
        return self._name

    def SetColor(self,color): # report space as blue (-1), red (+1), or 
                         # empty (0) 
        self._color = color
    
    def GetColor(self):
        return self._color

    def CountWin(self):
        self._numwins += 1
        
    def CountLoss(self):
        self._numlosses += 1

    def GetWin(self):
        return self._numwins
        
    def GetLoss(self):
        return self._numlosses
        
    def TakeTurn(self,board):
        pass
    
class randomplayer(player):
    
    def __init__(self):
        super().__init__() #call player.__init__
        self._name = 'Rando CalRizzen'
    
    def TakeTurn(self,board):
        #print (board[0])
        available_columns = []
        column_counter = 0
        for column in board[0]:
            if column == -1: #check if the column is empty
                available_columns.append(column_counter)
            column_counter += 1
        #print (available_columns)
        choose_column = random.randint(0,len(available_columns)-1) #choose
#random from list of available columns
        
        return available_columns[choose_column]
                
class strat1player(player):
	def __init__(self):
		super().__init__() # call player.__init__
		self.name = 'BoJangles'
	
	def TakeTurn(self,board):
		column_counter = 0
		for column in board[0]: #play first available slot
			if column == -1:
				break
			column_counter += 1
		choose_column = column_counter
		return choose_column
		
class humanplayer(player):
    
    def __init__(self):
        super().__init__() #call player.__init__
        self._name = 'A Real Person'
    
    def TakeTurn(self,board):
        #print (board[0])
        available_columns = []
        column_counter = 0
        for column in board[0]:
            if column == -1: #check if the column is empty
                available_columns.append(column_counter)
            column_counter += 1
        valid = False
        while(not valid):
            print ("These are available: ",available_columns)
            column_choice = input("Choose one: ")
            column_choice = int(column_choice)
            print (column_choice)
            if column_choice in available_columns:
                valid = True
                #print ("That was a valid choice")
        #print("returning from TakeTurn")
        return column_choice
    
