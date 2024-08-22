import pygame, sys
from block import Block
from board import Board
from settings import *

WIN = pygame.display.set_mode((W_WIDTH + 200, W_HEIGHT))
pygame.display.set_caption('TETRIS')

BOARD = Board(WIN)
BLOCK = Block(WIN)

MOVE_DN = pygame.USEREVENT
MOVE_DN_MS = 1000

MOVE = pygame.USEREVENT
MOVE_MS = 200

pygame.time.set_timer(MOVE_DN, MOVE_DN_MS)
pygame.time.set_timer(MOVE, MOVE_MS)

class Game_State: 

    def __init__(self):
        self.state = 'main' 

    def main(self):
        global BLOCK

        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                sys.exit()

            if event.type == MOVE_DN:
                BLOCK.move_dn()
                BOARD.check_rows()

            if event.type == MOVE:
                BLOCK.keys_pressed['left'] = False
                BLOCK.keys_pressed['right'] = False
                BLOCK.keys_pressed['down'] = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    BLOCK.rotate()                 

        BLOCK.move(keys_pressed)
        BOARD.check_death()
        BOARD.draw()
        BLOCK.draw()
        pygame.display.update()

    def State_Setter(self):
        if self.state == 'main': self.main()
        if self.state == 'other': pass

def main():
    gameloop = Game_State()
    clock = pygame.time.Clock()

    while True:
        gameloop.State_Setter()
        clock.tick(60)

if __name__ == '__main__':
    main()