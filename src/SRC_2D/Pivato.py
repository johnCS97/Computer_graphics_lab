import random
from matplotlib import pyplot as plt
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
        self.kernel[int(self.r/2)][int(self.r/2)] = 0
        self.kernel_sum = self.kernel.sum()
        # self.kernel/=self.kernel_sum
        # self.kek=np.zeros(shape=(self.rows, self.columns))
        # self.middle=(int)(width/2)
        # for i in range(self.middle-r,self.middle+r):
        #     for j in range(self.middle-r,self.middle+r):
        #         self.kek[i][j]=1
        # self.kek[self.middle][self.middle] = 0
        # self.kf=np.fft.fft2(self.kek)
        # self.kf/=np.sum(self.kf)
        self.array_init()

    def array_init(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.game_array[x][y] = random.randint(0, 1)

    def next_gen(self):
        next_gen = ss.convolve2d(
            self.game_array, self.kernel, mode='same', boundary='symm')/(self.r*self.r)
        # next_gen=np.fft.ifft2(np.fft.fft2(self.game_array)*self.kf)
        self.game_array = np.clip(self.game_array+(0 + ((next_gen >= 0.34) & (
            next_gen <= 0.46)) - ((next_gen < 0.30) | (next_gen > 0.59))), 0, 1)
        return self.game_array
