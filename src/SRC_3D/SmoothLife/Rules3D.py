import numpy as np
import math

class Rules3D:

    def __init__(self, b1=0.278, b2=0.365, d1=0.267, d2=0.445, m=0.028, n=0.147):
        self.b1 = b1
        self.b2 = b2
        self.d1 = d1
        self.d2 = d2
        self.n = n
        self.m = m

    def sigmaoid_1(self, x, a):
        return 1.0 / (1.0 + np.exp(-4.0 * (x - a) / self.m))

    def sigmaoid_2(self, x, a, b):
        return self.sigmaoid_1(x, a) * (1.0 - self.sigmaoid_1(x, b))

    def sigmaoid_m(self, x, y, m):
        return x * (1.0-self.sigmaoid_1(m, 0.5)) + y * self.sigmaoid_1(m, 0.5)

    def sigmaoid_s(self, n, m):
        return self.sigmaoid_2(n, self.sigmaoid_m(self.b1, self.d1, m), self.sigmaoid_m(self.b2, self.d2, m))

    def sigmaoid_new(self, n, m):
        return 2*self.sigmaoid_s(n, m)-1

def logistics(size, radius, ):
    z, y, x = size
    zz, yy, xx = np.mgrid[:y, :x, :z]
    radiuses = np.sqrt((xx - x / 2) ** 2 + (yy - y / 2) ** 2+(zz - z / 2) ** 2)

    logres = math.log(min(*size), 2)

    # with np.errstate(over="ignore"):
    logistic = 1 / (1 + np.exp(logres * (radiuses - radius)))

    logistic = np.roll(logistic, y // 2, axis=0)
    logistic = np.roll(logistic, x // 2, axis=1)
    logistic = np.roll(logistic, z // 2, axis=2)
    return logistic
