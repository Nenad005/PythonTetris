import pygame
import random
from settings import * 
from board import GET_COLOR

class Block:
    #TODO - POKAZIVANJE I DODAVANJE SLEDECEG ELEMENTA

    #TODO ----------------------------------------------------------
    #TODO ----------PROVERITI METODU ZA KRAJ IGRE(BUG)--------------
    #TODO ----------------------------------------------------------

    def __init__(self, WIN):
        self.body = Random_Shape()
        print(self.body)
        self.WIN = WIN
        self.keys_pressed = {'left': False, 'right': False, 'down': False, 'space' : False}
        self.pause = 0

    def draw(self):
        for i in range(len(self.body[1])):
            for j in range(len(self.body[1][i])):
                if (self.body[1][i][j]) != 0:
                    pygame.draw.rect(self.WIN, GET_COLOR(self.body[2]), ((j + self.body[0][1]) * BLOCK_SIZE-1, (i + self.body[0][0]) * BLOCK_SIZE-1, BLOCK_SIZE-2, BLOCK_SIZE-2))

    #TODO bolji sistem cekanja
    def move_dn(self):
        changed = False
        if self.pause == 3:
            changed = True
            self.pause = 0
        if not self.check_col_dn():
            self.body[0][0] += 1
            #print(self.body)
        elif changed == True:
            self.add_to_body()
            self.reset()
        else: self.pause +=1
        
    def check_col_dn(self):
        for i in range(len(self.body[1])):
            for j in range(len(self.body[1][i])):
                if self.body[1][i][j] != 0:
                    if BODY[i + self.body[0][0] + 1 + BLOCK_INDENT][j + self.body[0][1]] != 0:
                        return True 
        return False

    def check_col_right(self):
        for i in range(len(self.body[1])):
            for j in range(len(self.body[1][i])):
                if self.body[1][i][j] != 0:
                    try:
                        if BODY[i + self.body[0][0]+ BLOCK_INDENT][j + 1 + self.body[0][1]] != 0:
                            #self.add_to_body()
                            return True
                    except:
                        return True
        return False

    def check_col_left(self):
        for i in range(len(self.body[1])):
            for j in range(len(self.body[1][i])):
                if self.body[1][i][j] != 0:
                    if (self.body[0][1] + j) <= 0: return True
                    if BODY[i + self.body[0][0]+ BLOCK_INDENT][j - 1 + self.body[0][1]] != 0:
                        return True
        return False

    def add_to_body(self):
        print(f"added : {[i for i in self.body[1]]} at {self.body[0]}")

        for i in range(len(self.body[1])):
            for j in range(len(self.body[1][i])):
                if (self.body[1][i][j]) != 0:
                    x = i + self.body[0][0] + BLOCK_INDENT
                    y = j + self.body[0][1]
                    BODY[x][y] = self.body[2]

    #TODO POPRAVITI TIMEING
    def move(self, keys_pressed):
        if keys_pressed[pygame.K_a] and not self.keys_pressed['left']:
            if not self.check_col_left():
                self.body[0][1] -= 1
                self.keys_pressed['left'] = True
        if keys_pressed[pygame.K_d] and not self.keys_pressed['right']:
            if not self.check_col_right():
                self.body[0][1] += 1
                self.keys_pressed['right'] = True
        if keys_pressed[pygame.K_s] and not self.keys_pressed['down']:
            if not self.check_col_dn():
                self.body[0][0] += 1
                self.keys_pressed['down'] = True
            else: self.reset
        if keys_pressed[pygame.K_SPACE] and not self.keys_pressed['space']:
            while not self.check_col_dn():
                self.body[0][0] += 1
                self.pause = 3
            self.keys_pressed['space'] = True
        if not keys_pressed[pygame.K_SPACE]:
            self.keys_pressed['space'] = False

    def reset(self):
        self.body = Random_Shape()

    def rotate(self):
        body = list(zip(*self.body[1][::-1]))
        if self.check_rotate(body):
            self.body[1] = body

    #TODO HARD - napravi da uvek moze da se rotira ali da se pomera ako treba
    def check_rotate(self, body1):
        for i in range(len(body1)):
            for j in range(len(body1[i])):
                if body1[i][j] != 0:
                    try:
                        if (self.body[0][1] + j ) < 0 or BODY[self.body[0][0] + i + BLOCK_INDENT][self.body[0][1] + j] != 0:
                            return False
                    except:
                        #self.body[0][1] -= 1
                        #return True
                        return False
        return True

def Random_Shape():
    random.seed()
    shape = random.choice(['O', 'I', 'J', 'L', 'S', 'Z', 'T'])
    return Generate_Shape(shape)
    
def Generate_Shape(shape):
    body = [[-3, 4] , [], []]
    print(shape)

    if shape == 'O':
        body[1] = [
            [1, 1],
            [1, 1]
        ]
        body[2] = 1
    elif shape == 'I':
        body[0] = [-3, 3]
        body[1] = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 2, 2, 2],
            [0, 0, 0, 0]
        ]
        body[2] = 2
    elif shape == 'J':
        body[1] = [
            [0, 3, 0],
            [0, 3, 0],
            [3, 3, 0]
        ]
        body[2] = 3
    elif shape == 'L':
        body[1] = [
            [0, 4, 0],
            [0, 4, 0],
            [0, 4, 4]
        ]
        body[2] = 4
    elif shape == 'S':
        body[1] = [
            [5, 0, 0],
            [5, 5, 0],
            [0, 5, 0]
        ]
        body[2] = 5
    elif shape == 'Z':
        body[1] = [
            [0, 0, 6],
            [0, 6, 6],
            [0, 6, 0],
        ]
        body[2] = 6
    elif shape == 'T':
        body[1] = [
            [0, 0, 0],
            [7, 7, 7],
            [0, 7, 0],
        ]
        body[2] = 7
        
    return body