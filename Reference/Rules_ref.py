import math

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


class Rules:
    # Birth range
    B1 = 0.278
    B2 = 0.365
    # Survival range
    D1 = 0.267
    D2 = 0.445
    # Sigmoid widths
    N = 0.028
    M = 0.147

    # B1 = 0.257
    # B2 = 0.336
    # D1 = 0.365
    # D2 = 0.549
    # N = 0.028
    # M = 0.147

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)  # Set variables from constructor

    @staticmethod
    def sigma(x, a, alpha):
        """Logistic function on x Transition around a with steepness alpha"""
        return 1.0 / (1.0 + np.exp(-4.0 / alpha * (x - a)))

    def sigma2(self, x, a, b):
        """Logistic function on x between a and b"""
        return self.sigma(x, a, self.N) * (1.0 - self.sigma(x, b, self.N))

    @staticmethod
    def lerp(a, b, t):
        """Linear intererpolate t:[0,1] from a to b"""
        return (1.0 - t) * a + t * b

    def s(self, n, m):
        """State transition function"""
        alive = self.sigma(m, 0.5, self.M)
        return self.sigma2(n, self.lerp(self.B1, self.D1, alive), self.lerp(self.B2, self.D2, alive))

    def logistic2d (size, radius, roll=True, logres=None) :

        y, x = size
        # Get coordinate values of each point
        yy, xx = np.mgrid[:y, :x]
        # Distance between each point and the center
        radiuses = np.sqrt((xx - x/2)**2 + (yy - y/2)**2)
        # Scale factor for the transition width
        if logres is None:
            logres = math.log(min(*size), 2)
        with np.errstate(over="ignore"):
            # With big radiuses, the exp overflows,
            # but 1 / (1 + inf) == 0, so it's fine
            logistic = 1 / (1 + np.exp(logres * (radiuses - radius)))
        if roll:
            logistic = np.roll(logistic, y//2, axis=0)
            logistic = np.roll(logistic, x//2, axis=1)
        return logistic

