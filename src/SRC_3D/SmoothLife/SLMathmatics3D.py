import SRC_3D.SmoothLife.Rules3D as Rs
import numpy as np

class Multipliers:

    def __init__(self, size, inner_radius, outer_radius):
        self.inner = Rs.logistics(size, inner_radius)
        self.outer = Rs.logistics(size, outer_radius)
        self.annulus = self.outer - self.inner

        self.inner /= np.sum(self.inner)
        self.annulus /= np.sum(self.annulus)

        self.M = np.fft.fftn(self.inner)
        self.N = np.fft.fftn(self.annulus)
