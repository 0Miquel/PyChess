# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:27:06 2020

@author: miquel
"""

from king import *
from queen import *
from rook import *
from knight import *
from pawn import *
from bishop import *
from constants import *
import numpy as np
import copy
import math


class Board:
    
    def __init__(self):
        self.board = np.array([[Rook(0,0,BLACK),Knight(0,1,BLACK),Bishop(0,2,BLACK),King(0,3,BLACK),Queen(0,4,BLACK),Bishop(0,5,BLACK),Knight(0,6,BLACK),Rook(0,7,BLACK)],
                               [Pawn(1,0,BLACK),Pawn(1,1,BLACK),Pawn(1,2,BLACK),Pawn(1,3,BLACK),Pawn(1,4,BLACK),Pawn(1,5,BLACK),Pawn(1,6,BLACK),Pawn(1,7,BLACK)],
                               [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
                               [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
                               [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
                               [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
                               [Pawn(6,0,WHITE),Pawn(6,1,WHITE),Pawn(6,2,WHITE),Pawn(6,3,WHITE),Pawn(6,4,WHITE),Pawn(6,5,WHITE),Pawn(6,6,WHITE),Pawn(6,7,WHITE)],
                               [Rook(7,0,WHITE),Knight(7,1,WHITE),Bishop(7,2,WHITE),Queen(7,3,WHITE),King(7,4,WHITE),Bishop(7,5,WHITE),Knight(7,6,WHITE),Rook(7,7,WHITE)]])
        
        
    def draw_board(self, screen):
        screen.blit(background, (0,0))
        for i in range(N_COLS):
            for j in range(N_ROWS):
                piece = self.board[i][j]
                if piece != EMPTY:
                    piece.draw_piece(screen)
        
    def choose_piece(self, col, row, turn, screen):
        piece = self.board[row][col]
        can_choose = False
        
        if piece != EMPTY:
            if piece.color == turn:
                valid_locations = piece.get_valid_locations(self.board)
                valid_locations = self.check_valid_locations(piece)               
                print(valid_locations)
                if valid_locations != []:
                    self.draw_valid_locations(piece, screen)
                    can_choose = True
                    return can_choose, piece
        return can_choose, None

    def check_valid_locations(self, piece):
        valid_locations = piece.valid_locations
        
        for location in list(valid_locations):
            copy_piece = copy.deepcopy(piece)
            copy_piece.row = location[0]
            copy_piece.col = location[1]
            copy_board = copy.deepcopy(self)
            copy_board.board[piece.row][piece.col] = EMPTY
            copy_board.board[location[0]][location[1]] = copy_piece
            
            if copy_board.is_check(piece.color):
                valid_locations.remove(location)
        piece.valid_locations = valid_locations
        return valid_locations
    
    def draw_valid_locations(self, piece, screen):
        for location in piece.valid_locations:
            screen.blit(i_location, (location[1]*DIM_SQUARE, location[0]*DIM_SQUARE))

    def move_piece(self, piece, col, row, screen, turn):
        position = (row, col)
        can_move = False
        
        if position in piece.valid_locations: 
            can_move = True
            old_row = piece.row
            old_col = piece.col
            self.board[old_row][old_col] = EMPTY
            piece.row = row
            piece.col = col
            self.board[row][col] = piece
            #unable the 2 square movement once the pawn has been moved 
            if piece.id == PAWN:
                piece.start = False
                if piece.row == 7 or piece.row == 0:
                    piece.convert_queen(self.board)
                    piece = self.board[row][col]
        self.draw_board(screen)
 
        return can_move
    
    def is_check(self, turn):
        king = self.find_king(turn)
        king_position = (king.row, king.col)
        for i in range(N_ROWS):
            for j in range(N_COLS):
                piece = self.board[i][j]
                if piece != EMPTY:
                    if piece.color != turn:
                        if king_position in piece.get_valid_locations(self.board):
                            return True
        return False
 
    def is_checkmate(self, turn):
        checkmate = False
        if turn == BLACK:
            check = self.is_check(WHITE)
        else:
            check = self.is_check(BLACK)

        if check:
            checkmate = True
            for i in range(N_ROWS):
                for j in range(N_COLS):
                    piece = self.board[i][j]
                    if piece != EMPTY:
                        if piece.color != turn:
                            valid_locations = piece.get_valid_locations(self.board)
                            valid_locations = self.check_valid_locations(piece)
                            if valid_locations != []:
                                checkmate = False
                                return checkmate
        return checkmate
                            
                
    def find_king(self, turn):
        for i in range(N_ROWS):
            for j in range(N_COLS):
                piece = self.board[i][j]
                if piece != EMPTY:
                    if piece.id == KING and piece.color == turn:
                        return piece
    
    
    def is_draw(self, turn):
        for i in range(N_ROWS):
            for j in range(N_COLS):
                piece = self.board[i][j]
                if piece != EMPTY:
                    if piece.color == turn:
                        valid_locations = piece.get_valid_locations(self.board)
                        valid_locations = self.check_valid_locations(piece)
                        if valid_locations != []:
                            return False
        return True
    
    #SHOWS THE BOARD IN A NON-GRAPHICAL WAY
    def show_board(self):
        for i in range(N_COLS):
            print("")
            for j in range(N_ROWS):
                if self.board[i][j] == EMPTY:
                    print(self.board[i][j], end =" ")
                else:
                    print(self.board[i][j].id, end =" ")
        print("")
        
        
        
    def get_score(self, turn):
        score = 0
        for i in range(N_ROWS):
            for j in range(N_COLS):
                piece = self.board[i][j]
                if piece != EMPTY:
                    """
                    if piece.color == turn:
                        if piece.id == PAWN:
                            score += 2
                        elif piece.id == BISHOP or piece.id == ROOK or piece.id == KNIGHT:
                            score += 5
                        elif piece.id == QUEEN:
                            score += 10
                    else:
                    """
                    if piece.color != turn:
                        if piece.id == PAWN:
                            score -= 3
                        elif piece.id == BISHOP or piece.id == ROOK or piece.id == KNIGHT:
                            score -= 6
                        elif piece.id == QUEEN:
                            score -= 11
        print(score)
        return score
    
        
    def is_terminal_node(self):
        return self.is_checkmate(BLACK) or self.is_checkmate(WHITE) or self.is_draw(BLACK) or self.is_draw(WHITE)
        
    def minimax(self, depth, alpha, beta, maximizingPlayer):
        print(depth)
        is_terminal = self.is_terminal_node()
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.is_checkmate(BLACK):
                    return (100000000, None, None, None)
                elif self.is_checkmate(WHITE):
                    return (-100000000, None, None, None)
                else: # no valid moves, it is a draw
                    return (0, None, None, None)
            else: #depth == 0
                return (self.get_score(maximizingPlayer), None, None, None)
        if maximizingPlayer == BLACK: #AI PLAYER
            value = -math.inf
            row = 0
            col = 0
            best_piece = EMPTY
            for i in range(N_ROWS):
                for j in range(N_COLS):
                    piece = self.board[i][j]
                    if piece != EMPTY:
                        if piece.color == maximizingPlayer:
                            valid_locations = piece.get_valid_locations(self.board)
                            valid_locations = self.check_valid_locations(piece)
                            for location in valid_locations:
                                copy_piece = copy.deepcopy(piece)
                                copy_piece.row = location[0]
                                copy_piece.col = location[1]
                                copy_board = copy.deepcopy(self)
                                copy_board.board[piece.row][piece.col] = EMPTY
                                copy_board.board[location[0]][location[1]] = copy_piece
                                
                                new_score = copy_board.minimax(depth-1, alpha, beta, WHITE)[0]
                                if new_score > value:
                                    value = new_score
                                    row = location[0]
                                    col = location[1]
                                    best_piece = piece
                                alpha = max(alpha, value)
                                if alpha >= beta:
                                    print("cut")
                                    break
            #print(row, col, best_piece)
            return (value, row, col, best_piece)
            
        else: #minimzingPlayer OPP PLAYER
            value = math.inf
            row = 0
            col = 0
            best_piece = EMPTY
            for i in range(N_ROWS):
                for j in range(N_COLS):
                    piece = self.board[i][j]
                    if piece != EMPTY:
                        if piece.color == maximizingPlayer:
                            valid_locations = piece.get_valid_locations(self.board)
                            valid_locations = self.check_valid_locations(piece)
                            for location in valid_locations:
                                copy_piece = copy.deepcopy(piece)
                                copy_piece.row = location[0]
                                copy_piece.col = location[1]
                                copy_board = copy.deepcopy(self)
                                copy_board.board[piece.row][piece.col] = EMPTY
                                copy_board.board[location[0]][location[1]] = copy_piece
                                
                                new_score = copy_board.minimax(depth-1, alpha, beta, BLACK)[0]
                                if new_score < value:
                                    value = new_score
                                    row = location[0]
                                    col = location[1]
                                    best_piece = piece
                                beta = max(beta, value)
                                if alpha >= beta:
                                    print("cut")
                                    break
            #print(row, col, best_piece)
            return (value, row, col, best_piece)
    