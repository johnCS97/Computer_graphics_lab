import math

import Rules_ref
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

class Multipliers:
    INNER_RADIUS = 7.0
    OUTER_RADIUS = INNER_RADIUS * 3.0

    def __init__(self, size, inner_radius=INNER_RADIUS, outer_radius=OUTER_RADIUS):
        inner = Rules.logistic2d(size, inner_radius)
        outer = Rules.logistic2d(size, outer_radius)
        annulus = outer - inner

        # Scale each kernel so the sum is 1
        inner /= np.sum(inner)
        annulus /= np.sum(annulus)

        # Precompute the FFT's
        self.M = np.fft.fft2(inner)
        self.N = np.fft.fft2(annulus)

