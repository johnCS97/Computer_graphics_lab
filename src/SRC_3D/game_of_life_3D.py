import random

import numpy as np

import scipy.signal as ss


class Game:
    def __init__(self, width, height, depth, num):
        self.rows = int(width)
        self.columns = int(height)
        self.slices = int(depth)
        self.game_array = np.zeros(
            shape=(self.rows, self.columns, self.slices))
        self.array_init(num)
        self.angle=0.0

    def get_angle(self):
        return self.angle
    def array_init(self, cells):
        for i in range(cells):
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.columns-1)
            z = random.randint(0, self.slices-1)
            self.game_array[x][y][z] = random.randint(0, 1)
        # self.game_array[(int)(self.rows/2)][(int)(self.columns/2)][(int)(self.slices/2)]=1
        # self.game_array[(int)(self.rows/2)][(int)(self.columns/2)][(int)(self.slices/2)+1]=1
        # self.game_array[(int)(self.rows/2)][(int)(self.columns/2)][(int)(self.slices/2)-1]=1
        # # self.game_array[(int)(self.rows/2)][(int)(self.columns/2)+1][(int)(self.slices/2)]=1
        # # self.game_array[(int)(self.rows/2)][(int)(self.columns/2)-1][(int)(self.slices/2)]=1
        # self.game_array[(int)(self.rows/2)+1][(int)(self.columns/2)][(int)(self.slices/2)]=1
        # self.game_array[(int)(self.rows/2)-1][(int)(self.columns/2)][(int)(self.slices/2)]=1

    def next_gen(self):
        self.angle+=1
        nextg = np.zeros(shape=(self.rows, self.columns, self.slices))
        for x in range(self.rows):
            for y in range(self.columns):
                for z in range(self.slices):
                    num = self.get_neighbours(x, y, z)
                    nextg[x][y][z] = self.game_array[x][y][z]
                    if self.game_array[x][y][z] == 1 and (num == 5):
                        nextg[x][y][z] = 1
                    elif self.game_array[x][y][z] == 0 and (num == 4 or num == 5):
                        nextg[x][y][z] = 1
                    else:
                        nextg[x][y][z] = 0
                    # if self.game_array[x][y][z] == 1 and (num >= 4 and num <= 5):
                    #     nextg[x][y][z] = 0
                    # if self.game_array[x][y][z] == 0 and num == 5:
                    #     nextg[x][y][z] = 1
        self.game_array = nextg
        return self.game_array

    def get_neighbours(self, x, y, z):
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    a = x+i
                    b = y+j
                    c = z+k
                    if a >= 0 and b >= 0 and c >= 0:
                        if a < self.rows and b < self.columns and c < self.slices:
                            if (a != x or b != y or c != z):
                                sum += (self.game_array[a][b][c])
        return sum
