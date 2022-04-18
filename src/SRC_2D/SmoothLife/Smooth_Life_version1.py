
import pygame
import os
import SRC_2D.SmoothLife.SLMathmatics as slm
import SRC_2D.SmoothLife.Rules as rs
import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt
import sys
sys.path.insert(1, '/path/to/src/SRC_2D/Smoothlife')


class SmoothL:

    def __init__(self, width, height, inner_radius=2, outer_radius=6):
        self.width = width
        self.height = height
        self.rules = rs.Rules()
        self.inner = inner_radius
        self.outer = outer_radius
        self.game_field = np.zeros(shape=(self.width, self.height))
        self.SLmathmatics = slm.Multipliers((width, height))

    # Create_cells: creates cells depending on inner radius
    # [x:x+y,z:z+y] array thing, runs on all array indexes included in the range

    def create_cells(self, new_cells, age):
        for i in range(new_cells):
            x = np.random.randint(0, self.width - self.outer)
            y = np.random.randint(0, self.height - self.outer)
            self.game_field[x:x + self.outer, y:y + self.outer] = age

    def next(self):
        M = np.zeros(shape=(self.width, self.height))
        N = np.zeros(shape=(self.width, self.height))
        for x in range(self.width):
            for y in range(self.height):
                counterm = 0
                countern = 0
                for i in range(x-self.outer, x+self.outer):
                    if i >= 0 and i < self.width:
                        for j in range(y-self.outer, y+self.outer):
                            if j >= 0 and j < self.height:
                                dis = float(np.sqrt((j-y)**2.0+(i-x)**2.0))
                                if dis < self.inner:
                                    M[x][y] += self.game_field[i][j]
                                    N[x][y] += self.game_field[i][j]
                                    counterm += 1
                                    countern += 1
                                if dis > self.inner and dis < self.outer:
                                    N[x][y] += self.game_field[i][j]
                                    countern += 1
                if countern:
                    N[x][y] /= countern
                if counterm:
                    M[x][y] /= counterm

        self.game_field = self.rules.sigmaoid_s(N, M)
        return self.game_field

    def show(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                color = (self.game_field[i][j], 143, 124)
                pygame.draw.rect(screen, color, [i, j,
                                                 1, 1])
