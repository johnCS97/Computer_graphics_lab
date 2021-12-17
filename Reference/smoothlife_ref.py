import math
import pygame

import Rules_ref as R
import Multipliers_ref as M

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


# # Necessary for writing video
# from skvideo.io import FFmpegWriter
# from matplotlib import cm


class SmoothLife:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.multipliers = M.Multipliers((height, width))
        self.rules = R.Rules()
        self.clear()
        # self.esses = [None] * 3
        # self.esses_count = 0

    def clear(self):
        """Zero out the field"""
        self.field = np.zeros((self.height, self.width))
        # self.esses_count = 0

    def step(self):
        """Do timestep and return field"""

        # To sum up neighbors, do kernel convolutions
        # by multiplying in the frequency domain
        # and converting back to spacial domain
        field_ = np.fft.fft2(self.field)
        M_buffer_ = field_ * self.multipliers.M
        N_buffer_ = field_ * self.multipliers.N
        M_buffer = np.real(np.fft.ifft2(M_buffer_))
        N_buffer = np.real(np.fft.ifft2(N_buffer_))

        # Apply transition rules
        s = self.rules.s(N_buffer, M_buffer)
        nextfield = s

        # Trying some things with smooth time stepping....
        # Not yet working well....
        # s0 = s - M_buffer
        # s1, s2, s3 = self.esses

        # if self.esses_count == 0:
        #     delta = s0
        # elif self.esses_count == 1:
        #     delta = (3 * s0 - s1) / 2
        # elif self.esses_count == 2:
        #     delta = (23 * s0 - 16 * s1 + 5 * s2) / 12
        # else:  # self.esses_count == 3:
        #     delta = (55 * s0 - 59 * s1 + 37 * s2 - 9 * s3) / 24

        # self.esses = [s0] + self.esses[:-1]
        # if self.esses_count < 3:
        #     self.esses_count += 1
        # dt = 0.1
        # nextfield = self.field + dt * delta

        # mode = 0  # timestep mode (0 for discrete)
        # dt = 0.9  # timestep
        # # Apply timestep
        # nextfield = self._step(mode, self.field, s, M_buffer, dt)

        self.field = np.clip(nextfield, 0, 1)
        return self.field

    def _step(self, mode, f, s, m, dt):
        """State transition options
        SmoothLifeAll/SmoothLifeSDL/shaders/snm2D.frag
        """
        if mode == 0:  # Discrete time step
            return s

        # Or use a solution to the differential equation
        elif mode == 1:
            return f + dt*(2*s - 1)
        elif mode == 2:
            return f + dt*(s - f)
        elif mode == 3:
            return m + dt*(2*s - 1)
        elif mode == 4:
            return m + dt*(s - m)

    def add_speckles(self, count=None, intensity=1):
        """Populate field with random living squares
        If count unspecified, do a moderately dense fill
        I suggest using a smaller count when using continuous time
        updating instead of discrete because continuous tends to converge.
        """
        if count is None:
            # count = 200 worked well for a 128x128 grid and INNER_RADIUS 7
            # scale according to area and INNER_RADIUS
            count = 200 * (self.width * self.height) / (128 * 128)
            count *= (7.0 / self.multipliers.INNER_RADIUS) ** 2
            count = int(count)
        for i in range(count):
            radius = int(self.multipliers.INNER_RADIUS)
            r = np.random.randint(0, self.height - radius)
            c = np.random.randint(0, self.width - radius)
            self.field[r:r+radius, c:c+radius] = intensity
        # self.esses_count = 0



def show_animation():
        w = 1 << 9
        h = 1 << 9
        # w = 1920
        # h = 1080
        sl = SmoothLife(h, w)
        sl.add_speckles()
        sl.step()

        fig = plt.figure()
        # Nice color maps: viridis, plasma, gray, binary, seismic, gnuplot
        im = plt.imshow(sl.field, animated=True,
                    cmap=plt.get_cmap("viridis"), aspect="equal")

        def animate(*args):
            im.set_array(sl.step())
            return (im)

        ani = animation.FuncAnimation(fig, animate, interval=60, blit=True)
        plt.show()

if __name__ == '__main__':
    show_animation()
    # save_animation()