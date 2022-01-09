import Rules as Rs
import numpy as np


class Multipliers:
    INNER_RADIUS = 7.0
    OUTER_RADIUS = INNER_RADIUS * 3.0

    def __init__(self, size, inner_radius=INNER_RADIUS, outer_radius=OUTER_RADIUS):
        self.inner = Rs.logistics(size, inner_radius)
        self.outer = Rs.logistics(size, outer_radius)
        self.annulus = self.outer - self.inner
        # Scale each kernel so the sum is 1
        self.inner /= np.sum(self.inner)
        self.annulus /= np.sum(self.annulus)

        # Precompute the FFT's
        self.M = np.fft.fft2(self.inner)
        self.N = np.fft.fft2(self.annulus)

