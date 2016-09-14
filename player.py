# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:31:45 2016

@author: Roy
"""
class player():
	def __init__(self):
		self._color = 0
		self._numwins = 0
		self._numlosses = 0

	def SetColor(self,color): # report space as blue (-1), red (+1), or 
						 # empty (0) 
		self._color = color
		return self._color
	
	def CountWin(self):
		self._numwins += 1
		
	def CountLoss(self):
		self._numlosses += 1
	