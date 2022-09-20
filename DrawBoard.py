import numpy as np
import random
import pygame
import sys
import math
from Minimax import MINIMAX
from Window import Window
from Winmove import Winmove
from Board import Board
class DrawB(MINIMAX,Window,Winmove,Board):
        PLAYER = 0
        AI = 1
        BLUE = (0,0,255)
        BLACK = (0,0,0)
        RED = (255,0,0)
        YELLOW = (255,255,0)
        SQUARESIZE = 100
        RADIUS = int(SQUARESIZE/2 - 5)
        width = Board.COLUMN_COUNT * SQUARESIZE
        height = (Board.ROW_COUNT+1) * SQUARESIZE
        size = (width,height)
        screen = pygame.display.set_mode(size)

        def draw_board(self,board):
                for c in range(Board.COLUMN_COUNT):
                        for r in range(Board.ROW_COUNT):
                                pygame.draw.rect(DrawB.screen, DrawB.BLUE, (c*DrawB.SQUARESIZE, r*DrawB.SQUARESIZE+DrawB.SQUARESIZE, DrawB.SQUARESIZE, DrawB.SQUARESIZE))
                                pygame.draw.circle(DrawB.screen, DrawB.BLACK, (int(c*DrawB.SQUARESIZE+DrawB.SQUARESIZE/2), int(r*DrawB.SQUARESIZE+DrawB.SQUARESIZE+DrawB.SQUARESIZE/2)), DrawB.RADIUS)
	
                for c in range(Board.COLUMN_COUNT):
                        for r in range(Board.ROW_COUNT):		
                                if board[r][c] == Window.PLAYER_PIECE:
                                        pygame.draw.circle(DrawB.screen, DrawB.RED, (int(c*DrawB.SQUARESIZE+DrawB.SQUARESIZE/2), DrawB.height-int(r*DrawB.SQUARESIZE+DrawB.SQUARESIZE/2)), DrawB.RADIUS)
                                elif board[r][c] == Window.AI_PIECE: 
                                        pygame.draw.circle(DrawB.screen, DrawB.YELLOW, (int(c*DrawB.SQUARESIZE+DrawB.SQUARESIZE/2), DrawB.height-int(r*DrawB.SQUARESIZE+DrawB.SQUARESIZE/2)), DrawB.RADIUS)
                pygame.display.update()
        
        def __init__(self):

                self.board = Board.create_board(self)
                Board.print_board(self,self.board)
                game_over = False

                pygame.init()

                self.draw_board(self.board)
                pygame.display.update()

                myfont = pygame.font.SysFont("monospace", 75)

                turn = random.randint(DrawB.PLAYER, DrawB.AI)

                while not game_over:

                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                         sys.exit()

                                if event.type == pygame.MOUSEMOTION:
                                        pygame.draw.rect(DrawB.screen, DrawB.BLACK, (0,0, DrawB.width, DrawB.SQUARESIZE))
                                        posx = event.pos[0]
                                        if turn == DrawB.PLAYER:
                                                pygame.draw.circle(DrawB.screen, DrawB.RED, (posx, int(DrawB.SQUARESIZE/2)), DrawB.RADIUS)

                                pygame.display.update()

                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        pygame.draw.rect(DrawB.screen, DrawB.BLACK, (0,0, DrawB.width, DrawB.SQUARESIZE))
                                        
                                        # Ask for Player Input
                                        if turn == DrawB.PLAYER:
                                                posx = event.pos[0]
                                                col = int(math.floor(posx/DrawB.SQUARESIZE))

                                                if Board.is_valid_location(self,self.board, col):
                                                        row = Board.get_next_open_row(self,self.board, col)
                                                        Board.drop_piece(self,self.board, row, col, Window.PLAYER_PIECE)

                                                        if Winmove.winning_move(self,self.board, Window.PLAYER_PIECE):
                                                                label = myfont.render("Player wins!", 1, DrawB.RED)
                                                                screen.blit(label, (40,10))
                                                                game_over = True

                                                        turn += 1
                                                        turn = turn % 2

                                                        Board.print_board(self,self.board)
                                                        self.draw_board(self.board)


                        # # Ask for Computer Input
                        if turn == DrawB.AI and not game_over:				

                                
                                col, minimax_score = MINIMAX.minimax(self,self.board, 5, -math.inf, math.inf, True)

                                if Board.is_valid_location(self,self.board, col):
                                        #pygame.time.wait(500)
                                        row = Board.get_next_open_row(self,self.board, col)
                                        Board.drop_piece(self,self.board, row, col, Window.AI_PIECE)

                                        if Winmove.winning_move(self,self.board, Window.AI_PIECE):
                                                label = myfont.render("Computer wins!", 1, DrawB.YELLOW)
                                                DrawB.screen.blit(label, (40,10))
                                                game_over = True
        
                                        Board.print_board(self,self.board)
                                        self.draw_board(self.board)

                                        turn += 1
                                        turn = turn % 2

                        if game_over:
                                pygame.time.wait(3000)  

