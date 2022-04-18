import random

import numpy as np

import scipy.signal as ss


class Game:
    def __init__(self, width, height):
        self.rows = int(width)
        self.columns = int(height)
        self.game_array = np.ndarray(shape=(self.rows, self.columns))
        self.kernel = np.asarray([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        self.array_init()

    def array_init(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.game_array[x][y] = random.randint(0, 1)

    def next_gen(self):
        next_gen = ss.convolve2d(
            self.game_array, self.kernel, mode='same', boundary='wrap')
        for x in range(self.rows):
            for y in range(self.columns):
                number_of_neighbours = next_gen[x][y]
                if self.game_array[x][y] == 1 and (number_of_neighbours == 2 or number_of_neighbours == 3):
                    self.game_array[x][y] = 1
                elif self.game_array[x][y] == 0 and number_of_neighbours == 3:
                    self.game_array[x][y] = 1
                else:
                    self.game_array[x][y] = 0
        self.game_array = np.clip(self.game_array, 0, 1)
        return self.game_array
