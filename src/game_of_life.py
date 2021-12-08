import random

import numpy as np
import pygame


class Game:
    def __init__(self, scale, width, height, offset):
        self.scale = scale
        self.rows = int(width / scale) + 20
        self.columns = int(height / scale) + 20
        self.offset = offset
        self.game_array = np.ndarray(shape=(self.rows, self.columns))

    def array_init(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.game_array[x][y] = random.randint(0, 1)

    def next_gen(self):
        next_gen = np.ndarray(shape=(self.rows, self.columns))
        for x in range(self.rows):
            for y in range(self.columns):
                number_of_neighbours = self.get_neighbours(x, y)
                if self.game_array[x][y] == 1 and (number_of_neighbours == 2 or number_of_neighbours == 3):
                    next_gen[x][y] = 1
                elif self.game_array[x][y] == 0 and number_of_neighbours == 3:
                    next_gen[x][y] = 1
                else:
                    next_gen[x][y] = 0
        self.game_array = next_gen

    def conway_life(self, surface, off_color, on_color):

        for x in range(self.rows):
            for y in range(self.columns):
                if self.game_array[x][y] == 1:
                    pygame.draw.rect(surface, on_color,
                                     [x * self.scale - 10 * self.scale, y * self.scale - 10 * self.scale,
                                      self.scale - self.offset, self.scale - self.offset])
                else:
                    pygame.draw.rect(surface, off_color,
                                     [x * self.scale - 10 * self.scale, y * self.scale - 10 * self.scale,
                                      self.scale - self.offset, self.scale - self.offset])
        self.next_gen()

    def get_neighbours(self, x, y):
        total = 0
        if x:
            if y:
                total += self.game_array[x - 1][y - 1]
            if y != self.columns - 1:
                total += self.game_array[x - 1][y + 1]
            total += self.game_array[x - 1][y]
        if y:
            total += self.game_array[x][y - 1]
            if x != self.rows - 1:
                total += self.game_array[x + 1][y - 1]
        if y != self.columns - 1:
            total += self.game_array[x][y + 1]
        if y != self.columns - 1 and x != self.rows - 1:
            total += self.game_array[x + 1][y + 1]

        if x != self.rows - 1:
            total += self.game_array[x + 1][y]

        return total

