import numpy as np
import random
import pygame
import sys
import math
from Board import Board
from Winmove import Winmove
from Window import Window
class MINIMAX(Window,Winmove,Board):
        
        def minimax(self,board, depth, alpha, beta, maximizingPlayer):
                valid_locations = Board.get_valid_locations(self,board)
                is_terminal = Window.is_terminal_node(self,board)
                if depth == 0 or is_terminal:
                        if is_terminal:
                                if Winmove.winning_move(self,board, Window.AI_PIECE):
                                        return (None, 100000000000000)
                                elif Winmove.winning_move(self,board, Window.PLAYER_PIECE):
                                        return (None, -10000000000000)
                                else: # Game is over, no more valid moves
                                        return (None, 0)
                        else: # Depth is zero
                                return (None, Window.score_position(self,board, Window.AI_PIECE))
                if maximizingPlayer:
                        value = -math.inf
                        column = random.choice(valid_locations)
                        for col in valid_locations:
                                row = Board.get_next_open_row(self,board, col)
                                b_copy = board.copy()
                                Board.drop_piece(self,b_copy, row, col, Window.AI_PIECE)
                                new_score = MINIMAX.minimax(self,b_copy, depth-1, alpha, beta, False)[1]
                                if new_score > value:
                                        value = new_score
                                        column = col
                                alpha = max(alpha, value)
                                if alpha >= beta:
                                        break
                        return column, value

                else: # Minimizing player
                        value = math.inf
                        column = random.choice(valid_locations)
                        for col in valid_locations:
                                row = Board.get_next_open_row(self,board, col)
                                b_copy = board.copy()
                                Board.drop_piece(self,b_copy, row, col, Window.PLAYER_PIECE)
                                new_score = MINIMAX.minimax(self,b_copy, depth-1, alpha, beta, True)[1]
                                if new_score < value:
                                        value = new_score
                                        column = col
                                beta = min(beta, value)
                                if alpha >= beta:
                                        break
                        return column, value


        def pick_best_move(self,board, piece):

                valid_locations = Board.get_valid_locations(self,board)
                best_score = -10000
                best_col = random.choice(valid_locations)
                for col in valid_locations:
                        row = Board.get_next_open_row(self,board, col)
                        temp_board = board.copy()
                        Board.drop_piece(self,temp_board, row, col, piece)
                        score = Window.score_position(self,temp_board, piece)
                        if score > best_score:
                                best_score = score
                                best_col = col

                return best_col
