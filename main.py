# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:26:21 2020

@author: miquel
"""

import pygame 
import numpy as np
from constants import *
from board import *
import math
pygame.init()

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption('Ajedrez')

board = Board()
board.draw_board(screen)
running = True
gameover = False
turn = WHITE

phase = 1
#PHASE = 1, CHOOSE A PIECE
#PHASE = 2, MOVE THAT PIECE OR UNDO THE CHOICE 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and not gameover and turn == WHITE:
            x,y = pygame.mouse.get_pos()
            col = int(x/DIM_SQUARE)
            row = int(y/DIM_SQUARE)
            if col < 8:
                if phase == 1:
                    can_choose, piece = board.choose_piece(col, row, turn, screen)
                    if can_choose:
                        phase = 2
                else: #phase == 2
                    phase = 1
                    if board.move_piece(piece, col, row, screen, turn):
                        if board.is_checkmate(turn):
                            gameover = True
                            print("Player", turn, "wins")
                        else:
                            if turn == WHITE:
                                turn = BLACK
                            else:
                                turn = WHITE
                            if board.is_draw(turn):
                                gameover = True
                                print("DRAW")

        elif turn == BLACK:
            score, row, col, piece = board.minimax(3, -math.inf, math.inf, BLACK)
            if board.move_piece(piece, col, row, screen, turn):
                if board.is_checkmate(turn):
                    gameover = True
                    print("Player", turn, "wins")
                else:
                    if turn == WHITE:
                        turn = BLACK
                    else:
                        turn = WHITE
                    if board.is_draw(turn):
                        gameover = True
                        print("DRAW")

                
                

            #board.show_board()
    pygame.display.update()

pygame.quit() 
