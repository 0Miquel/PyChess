# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:36:59 2020

@author: miquel
"""
from queen import *
from constants import *

#PEON
class Pawn:
    
    def __init__(self, row, col, color):
         self.id = PAWN
         self.col = col
         self.row = row
         self.color = color
         self.start = True
         
    def get_valid_locations(self, board):
        valid_locations = []
        if self.color == WHITE:
            if board[self.row-1][self.col] == EMPTY:
                valid_locations.append((self.row-1,self.col))
                if self.start:
                    if board[self.row-2][self.col] == EMPTY:
                        valid_locations.append((self.row-2,self.col))
                    
            if self.col+1 < N_COLS:
                if board[self.row-1][self.col+1] != EMPTY:
                    if board[self.row-1][self.col+1].color == BLACK:
                        valid_locations.append((self.row-1,self.col+1))
            if self.col-1 > -1:
                if board[self.row-1][self.col-1] != EMPTY:
                    if board[self.row-1][self.col-1].color == BLACK:
                        valid_locations.append((self.row-1,self.col-1))
                
        else: #color == BLACK
            if board[self.row+1][self.col] == EMPTY:
                valid_locations.append((self.row+1,self.col))
                if self.start:
                    if board[self.row+2][self.col] == EMPTY:
                        valid_locations.append((self.row+2,self.col))
                    
            if self.col+1 < N_COLS:
                if board[self.row+1][self.col+1] != EMPTY:
                    if board[self.row+1][self.col+1].color == WHITE:
                        valid_locations.append((self.row+1,self.col+1))
            if self.col-1 > -1:
                if board[self.row+1][self.col-1] != EMPTY:
                    if board[self.row+1][self.col-1].color == WHITE:
                        valid_locations.append((self.row+1,self.col-1))
        
        self.valid_locations = valid_locations
        return self.valid_locations
    
    def draw_piece(self,screen):
        if self.color == WHITE:
            screen.blit(w_pawn, (self.col*DIM_SQUARE,self.row*DIM_SQUARE))
        else: #color == BLACK
            screen.blit(b_pawn, (self.col*DIM_SQUARE,self.row*DIM_SQUARE))
            
    def convert_queen(self, board):
        if self.color == WHITE:
            if self.row == 0:
                board[self.row][self.col] = Queen(self.row, self.col, WHITE)
        else: #self.color == BLACK
            if self.row == 7:
                board[self.row][self.col] = Queen(self.row, self.col, BLACK)
        
        
        
        