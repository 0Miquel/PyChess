# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:34:59 2020

@author: miquel
"""

from constants import *

#REINA
class Queen:
    
    def __init__(self, row, col, color):
         self.id = QUEEN
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
            
        #diagonals
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
            screen.blit(w_queen, (self.col*DIM_SQUARE,self.row*DIM_SQUARE))
        else: #color == BLACK
            screen.blit(b_queen, (self.col*DIM_SQUARE,self.row*DIM_SQUARE))