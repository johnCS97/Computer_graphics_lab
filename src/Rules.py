import numpy as np
import math


class Rules:

    def __init__(self, b1=0.278, b2=0.365, d1=0.267, d2=0.445, m=0.028, n=0.147):
        self.b1 = b1
        self.b2 = b2
        self.d1 = d1
        self.d2 = d2
        self.n = m
        self.m = n

    @staticmethod
    def sigmaoid_1(x, a, alpha):
        return 1.0 / (1.0 + np.exp(-4.0 * (x - a) / alpha))

    def sigmaoid_2(self, x, a, b):
        return self.sigmaoid_1(x, a, self.n) * (1.0 - self.sigmaoid_1(x, b, self.n))

    @staticmethod
    def sigmaoid_m(x, y, m):
        return x*(1.0-m)+y*m

    def sigmaoid_s(self, n, m):
        return self.sigmaoid_2(n, self.sigmaoid_m(self.b1, self.d1, m), self.sigmaoid_m(self.b2, self.d2, m))


def logistics(size, radius,roll=True, logres=None):
    y, x = size
    yy, xx = np.mgrid[:y, :x]
    radiuses = np.sqrt((xx - x / 2) ** 2 + (yy - y / 2) ** 2)
    if logres is None:
        logres = math.log(min(*size), 2)
    with np.errstate(over="ignore"):
        logistic = 1 / (1 + np.exp(logres * (radiuses - radius)))
    if roll:
        logistic = np.roll(logistic, y // 2, axis=0)
        logistic = np.roll(logistic, x // 2, axis=1)
    return logistic
