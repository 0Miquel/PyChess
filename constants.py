# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:29:26 2020

@author: miquel
"""


import numpy as np
import pygame
pygame.init()

background = pygame.image.load('./images/background.png')
b_bishop = pygame.image.load('./images/bb.png')
b_rook = pygame.image.load('./images/br.png')
b_pawn = pygame.image.load('./images/bp.png')
b_queen = pygame.image.load('./images/bq.png')
b_king = pygame.image.load('./images/bk.png')
b_knight = pygame.image.load('./images/bn.png')
w_bishop = pygame.image.load('./images/wb.png')
w_pawn = pygame.image.load('./images/wp.png')
w_rook = pygame.image.load('./images/wr.png')
w_queen = pygame.image.load('./images/wq.png')
w_king = pygame.image.load('./images/wk.png')
w_knight = pygame.image.load('./images/wn.png')
i_location = pygame.image.load('./images/location.png')


KING = 3
QUEEN = 4
ROOK = 5
KNIGHT = 6
PAWN = 7
BISHOP = 8

EMPTY = 0
WHITE = 1
BLACK = 2

N_ROWS = 8
N_COLS = 8
DIM_SQUARE = 109
SCREEN_X = N_COLS * DIM_SQUARE
SCREEN_Y = N_ROWS * DIM_SQUARE




