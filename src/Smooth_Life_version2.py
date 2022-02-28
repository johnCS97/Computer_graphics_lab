from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import SLMathmatics as slm
import Rules as rs
import os
import pygame


class SmoothL:

    def __init__(self, width, height, inner_radius=10, outer_radius=30):
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
        field = np.fft.fft2(self.game_field)
        M_buffer = field * self.SLmathmatics.M
        N_buffer = field * self.SLmathmatics.N
        M_buffer = np.real(np.fft.ifft2(M_buffer))
        N_buffer = np.real(np.fft.ifft2(N_buffer))
        s = self.rules.sigmaoid_s(N_buffer, M_buffer)
        
        self.game_field = np.clip(s, 0, 1)
        return self.game_field
        
if __name__ == '__main__':
    sl = SmoothL(400, 400)
    sl.create_cells(100,1)
    fig = plt.figure()
    im = plt.imshow(sl.game_field, animated=True,
                    cmap=plt.get_cmap("winter"), aspect="equal")
    def animate(*args):
        im.set_array(sl.next())
        return (im, )
    ani = animation.FuncAnimation(fig, animate, interval=100, blit=True)
    
    plt.show()

