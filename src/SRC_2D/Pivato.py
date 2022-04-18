import random

import numpy as np
import pygame
import scipy.signal as ss
from scipy.ndimage import convolve


class Game:
    def __init__(self, width, height, r):
        self.rows = width
        self.columns = height
        self.r = 2*r+1
        self.game_array = np.ndarray(shape=(self.rows, self.columns))
        self.kernel = np.ones(shape=(self.r, self.r))
        self.kernel_sum = self.kernel.sum()
        self.kernel = self.kernel/self.kernel_sum
        self.array_init()

    def array_init(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.game_array[x][y] = random.randint(0, 1)

    def next_gen(self):
        next_gen = ss.convolve2d(
            self.game_array, self.kernel, mode='same', boundary='wrap')
        self.game_array = np.clip(self.game_array+(0 + ((next_gen >= 0.34) & (
            next_gen <= 0.45)) - ((next_gen < 0.34) | (next_gen > 0.58))), 0, 1)
        return self.game_array
