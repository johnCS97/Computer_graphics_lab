from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import SLMathmatics as slm
import Rules as rs
import os
import pygame


class SmoothL:

    def __init__(self, width, height, inner_radius=2, outer_radius=6):
        self.width = width
        self.height = height
        self.rules = rs.Rules()
        self.inner = inner_radius
        self.outer = outer_radius
        self.game_field = np.zeros(shape=(self.width, self.height))
        self.SLmathmatics = slm.Multipliers((width, height))
        self.kernel = np.asarray([
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0]])
        self.kernel = self.kernel / np.sum(self.kernel)

    # Create_cells: creates cells depending on inner radius
    # [x:x+y,z:z+y] array thing, runs on all array indexes included in the range

    def create_cells(self, new_cells, age):
        for i in range(new_cells):
            x = np.random.randint(0, self.width - self.outer)
            y = np.random.randint(0, self.height - self.outer)
            self.game_field[x:x + self.outer, y:y + self.outer] = age

    def next(self):
        

    def show(self,screen):
        for i in range(self.width):
            for j in range(self.height):
                color = (self.game_field[i][j], 143, 124)
                pygame.draw.rect(screen, color, [i , j ,
                                      1, 1])
        


if __name__ == '__main__':
    sl = SmoothL(50, 50)
    sl.create_cells(10,1)
    fig = plt.figure()
    # Nice color maps: viridis, plasma, gray, binary, seismic, gnuplot
    im = plt.imshow(sl.game_field, animated=True,
                    cmap=plt.get_cmap("plasma"), aspect="equal")
    def animate(*args):
        im.set_array(sl.next())
        return (im, )

    ani = animation.FuncAnimation(fig, animate, interval=60, blit=True)
    plt.show()

