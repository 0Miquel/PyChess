# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:35:44 2020

@author: miquel
"""

from constants import *

#TORRE
class Rook:
    
    def __init__(self, row, col, color):
         self.id = ROOK
         self.col = col
         self.row = row
         self.color = color
        
    def get_valid_locations(self, board):
        valid_locations = []
        
        row = board[self.row,:]
        col = board[:,self.col]
        
        #treating col
        for i in range(self.row+1, len(col)):
            if board[i][self.col] == EMPTY:
                valid_locations.append((i,self.col))
            elif board[i][self.col].color != self.color:
                valid_locations.append((i,self.col))
                break
            else:
                break
        
        for i in range(self.row-1, -1, -1):
            if board[i][self.col] == EMPTY:
                valid_locations.append((i,self.col))
            elif board[i][self.col].color != self.color:
                valid_locations.append((i,self.col))
                break
            else:
                break
        
        for i in range(self.col+1, len(row)):
            if board[self.row][i] == EMPTY:
                valid_locations.append((self.row,i))
            elif board[self.row][i].color != self.color:
                valid_locations.append((self.row,i))
                break
            else:
                break
        
        for i in range(self.col-1, -1, -1):
            if board[self.row][i] == EMPTY:
                valid_locations.append((self.row,i))
            elif board[self.row][i].color != self.color:
                valid_locations.append((self.row,i))
                break
            else:
                break
            
        self.valid_locations = valid_locations
        return self.valid_locations
    
    def draw_piece(self,screen):
        if self.color == WHITE:
            screen.blit(w_rook, (self.col*DIM_SQUARE,self.row*DIM_SQUARE))
        else: #color == BLACK
            screen.blit(b_rook, (self.col*DIM_SQUARE,self.row*DIM_SQUARE))