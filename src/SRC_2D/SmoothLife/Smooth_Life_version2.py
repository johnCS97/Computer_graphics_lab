
import os

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import SRC_2D.SmoothLife.SLMathmatics as slm
import SRC_2D.SmoothLife.Rules as rs


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
            x = np.random.randint(self.outer, self.width - self.outer)
            y = np.random.randint(self.outer, self.height - self.outer)
            self.game_field[x-self.outer:x + self.outer,
                            y-self.outer:y + self.outer] = age

    def next(self):
        field = np.fft.fft2(self.game_field)
        M_buffer = field * self.SLmathmatics.M
        N_buffer = field * self.SLmathmatics.N
        M_buffer = np.real(np.fft.ifft2(M_buffer))
        N_buffer = np.real(np.fft.ifft2(N_buffer))
        s = self.rules.sigmaoid_s(N_buffer, M_buffer)

        self.game_field = np.clip(s, 0, 1)
        return self.game_field
