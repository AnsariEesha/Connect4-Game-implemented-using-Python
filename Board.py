import numpy as np
import random
import pygame
import sys
import math
class Board:
        ROW_COUNT = 6
        COLUMN_COUNT = 7

        
        def create_board(self):
                board = np.zeros((Board.ROW_COUNT,Board.COLUMN_COUNT))
                return board

        def drop_piece(self,board, row, col, piece):
                board[row][col] = piece

        def is_valid_location(self,board, col):
                return board[Board.ROW_COUNT-1][col] == 0

        def get_valid_locations(self,board):
                valid_locations = []
                for col in range(Board.COLUMN_COUNT):
                        if self.is_valid_location(board, col):
                                valid_locations.append(col)
                return valid_locations

        def get_next_open_row(self,board, col):
                for r in range(Board.ROW_COUNT):
                        if board[r][col] == 0:
                                return r

        def print_board(self,board):
                print(np.flip(board, 0))
