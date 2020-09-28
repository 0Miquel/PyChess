# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:37:19 2020

@author: miquel
"""

from constants import *

#ALFIL
class Bishop:
    
    def __init__(self, row, col, color):
         self.id = BISHOP
         self.col = col
         self.row = row
         self.color = color
         
    def get_valid_locations(self, board):
        valid_locations = []
                
        for i,j in zip(range(self.row+1, N_ROWS), range(self.col+1, N_COLS)):
            if board[i][j] == EMPTY:
                valid_locations.append((i,j))
            elif board[i][j].color != self.color:
                valid_locations.append((i,j))
                break
            else:
                break
        
        for i,j in zip(range(self.row-1, -1, -1), range(self.col-1, -1, -1)):
            if board[i][j] == EMPTY:
                valid_locations.append((i,j))
            elif board[i][j].color != self.color:
                valid_locations.append((i,j))
                break
            else:
                break
            
        for i,j in zip(range(self.row+1, N_ROWS), range(self.col-1, -1, -1)):
            if board[i][j] == EMPTY:
                valid_locations.append((i,j))
            elif board[i][j].color != self.color:
                valid_locations.append((i,j))
                break
            else:
                break
            
        for i,j in zip(range(self.row-1, -1, -1), range(self.col+1, N_COLS)):
            if board[i][j] == EMPTY:
                valid_locations.append((i,j))
            elif board[i][j].color != self.color:
                valid_locations.append((i,j))
                break
            else:
                break
        
        self.valid_locations = valid_locations
        return self.valid_locations
    
    def draw_piece(self,screen):
        if self.color == WHITE:
            screen.blit(w_bishop, (self.col*DIM_SQUARE,self.row*DIM_SQUARE))
        else: #color == BLACK
            screen.blit(b_bishop, (self.col*DIM_SQUARE,self.row*DIM_SQUARE))