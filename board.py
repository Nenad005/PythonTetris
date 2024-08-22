import pygame, sys
from settings import *


class Board():
    def __init__(self, WIN):
        self.body = BODY
        self.block_size = W_WIDTH / 10
        self.WIN = WIN
    
    def draw(self):
        for i in range(BLOCK_INDENT, len(self.body)):
            for j in range(len(self.body[i])):
                pygame.draw.rect(self.WIN, GET_COLOR(self.body[i][j]), (j * BLOCK_SIZE-1, (i - BLOCK_INDENT) * BLOCK_SIZE-1, BLOCK_SIZE-2, BLOCK_SIZE-2))

    def check_rows(self):#all good
        rows_full = []
        for i in range(3, len(BODY) - 1):
            row_full = True
            for j in range(len(BODY[i])):
                if BODY[i][j] == 0: row_full = False; break
            if row_full == True: rows_full.append(i)
        if len(rows_full) != 0 : 
            self.delete_rows(rows_full)

    def delete_rows(self, rows):#all good
        #print(rows, end = ', ')
        for row in rows:
            BODY[row] = BODY[row-1][:]
            if row == 0:
                BODY[row] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            if row > 1:
                self.delete_rows([row-1])

    def restart_body(self):#all good
        for i in range(len(BODY) - 1):
            BODY[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def check_death(self):#all good
        for i in range(3):
            for j in range(10):
                if BODY[i][j] != 0:
                    self.restart_body()
                    pygame.quit()
                    sys.exit()
                    break
        
def GET_COLOR(n):
    if n == 0: return GRAY
    elif n == 1: return YELLOW
    elif n == 2: return CYAN
    elif n == 3: return BLUE
    elif n == 4: return ORANGE
    elif n == 5: return GREEN
    elif n == 6: return RED
    elif n == 7: return PURPLE
    elif n == 8: return BLACK