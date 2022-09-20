import numpy as np
import random
import pygame
import sys
import math
from Board import Board
from Winmove import Winmove
class Window(Winmove,Board):
        PLAYER_PIECE = 1
        AI_PIECE = 2
        EMPTY = 0
        WINDOW_LENGTH = 4

        
        def evaluate_window(self,window, piece):
                score = 0
                opp_piece = Window.PLAYER_PIECE
                if piece == Window.PLAYER_PIECE:
                        opp_piece =Window.AI_PIECE

                if window.count(piece) == 4:
                        score += 100
                elif window.count(piece) == 3 and window.count(Window.EMPTY) == 1:
                        score += 5
                elif window.count(piece) == 2 and window.count(Window.EMPTY) == 2:
                        score += 2

                if window.count(opp_piece) == 3 and window.count(Window.EMPTY) == 1:
                        score -= 4

                return score

        def score_position(self,board, piece):
                score = 0

                ## Score center column
                center_array = [int(i) for i in list(board[:, Board.COLUMN_COUNT//2])]
                center_count = center_array.count(piece)
                score += center_count * 3

                ## Score Horizontal
                for r in range(Board.ROW_COUNT):
                        row_array = [int(i) for i in list(board[r,:])]
                        for c in range(Board.COLUMN_COUNT-3):
                                window = row_array[c:c+Window.WINDOW_LENGTH]
                                score += self.evaluate_window(window, piece)

                ## Score Vertical
                for c in range(Board.COLUMN_COUNT):
                        col_array = [int(i) for i in list(board[:,c])]
                        for r in range(Board.ROW_COUNT-3):
                                window = col_array[r:r+Window.WINDOW_LENGTH]
                                score += self.evaluate_window(window, piece)

                ## Score posiive sloped diagonal
                for r in range(Board.ROW_COUNT-3):
                        for c in range(Board.COLUMN_COUNT-3):
                                window = [board[r+i][c+i] for i in range(Window.WINDOW_LENGTH)]
                                score += self.evaluate_window(window, piece)

                for r in range(Board.ROW_COUNT-3):
                        for c in range(Board.COLUMN_COUNT-3):
                                window = [board[r+3-i][c+i] for i in range(Window.WINDOW_LENGTH)]
                                score += self.evaluate_window(window, piece)

                return score

        def is_terminal_node(self,board):
                return Winmove.winning_move(self,board, Window.PLAYER_PIECE) or Winmove.winning_move(self,board, Window.AI_PIECE) or len(Board.get_valid_locations(self,board)) == 0

