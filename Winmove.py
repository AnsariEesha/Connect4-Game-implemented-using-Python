import numpy as np
import random
import pygame
import sys
import math
from Board import Board
class Winmove(Board):

        def winning_move(self,board, piece):
                # Check horizontal locations for win
                for c in range(Board.COLUMN_COUNT-3):
                        for r in range(Board.ROW_COUNT):
                                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                                        return True

                # Check vertical locations for win
                for c in range(Board.COLUMN_COUNT):
                        for r in range(Board.ROW_COUNT-3):
                                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                                        return True

                # Check positively sloped diaganols
                for c in range(Board.COLUMN_COUNT-3):
                        for r in range(Board.ROW_COUNT-3):
                                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                                        return True

                # Check negatively sloped diaganols
                for c in range(Board.COLUMN_COUNT-3):
                        for r in range(3, Board.ROW_COUNT):
                                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                                        return True
