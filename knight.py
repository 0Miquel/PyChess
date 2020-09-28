# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:36:05 2020

@author: miquel
"""

from constants import *

#CABALLO
class Knight:
    
    def __init__(self, row, col, color):
         self.id = KNIGHT
         self.col = col
         self.row = row
         self.color = color
         
    def get_valid_locations(self, board):
        valid_locations = []
        
        if self.row+2 < N_ROWS and self.col+1 < N_COLS:
            if board[self.row+2][self.col+1] == EMPTY or board[self.row+2][self.col+1].color != self.color:
                valid_locations.append((self.row+2,self.col+1))
        
        if self.row+2 < N_ROWS and self.col-1 > -1:
            if board[self.row+2][self.col-1] == EMPTY or board[self.row+2][self.col-1].color != self.color:
                valid_locations.append((self.row+2,self.col-1))
        
        if self.row-2 > -1 and self.col+1 < N_COLS:
            if board[self.row-2][self.col+1] == EMPTY or board[self.row-2][self.col+1].color != self.color:
                valid_locations.append((self.row-2,self.col+1))
          
        if self.row-2 > -1 and self.col-1 > -1:
            if board[self.row-2][self.col-1] == EMPTY or board[self.row-2][self.col-1].color != self.color:
                valid_locations.append((self.row-2,self.col-1))
        
        if self.row+1 < N_ROWS and self.col+2 < N_COLS:
            if board[self.row+1][self.col+2] == EMPTY or board[self.row+1][self.col+2].color != self.color:
                valid_locations.append((self.row+1,self.col+2))
        
        if self.row-1 > -1 and self.col+2 < N_COLS:
            if board[self.row-1][self.col+2] == EMPTY or board[self.row-1][self.col+2].color != self.color:
                valid_locations.append((self.row-1,self.col+2))
            
        if self.row+1 < N_ROWS and self.col-2 > -1:
            if board[self.row+1][self.col-2] == EMPTY or board[self.row+1][self.col-2].color != self.color:
                valid_locations.append((self.row+1,self.col-2))
        
        if self.row-1 > -1 and self.col-2 > -1:
            if board[self.row-1][self.col-2] == EMPTY or board[self.row-1][self.col-2].color != self.color:
                valid_locations.append((self.row-1,self.col-2))
        
        self.valid_locations = valid_locations
        return self.valid_locations
    
    def draw_piece(self,screen):
        if self.color == WHITE:
            screen.blit(w_knight, (self.col*DIM_SQUARE,self.row*DIM_SQUARE))
        else: #color == BLACK
            screen.blit(b_knight, (self.col*DIM_SQUARE,self.row*DIM_SQUARE))