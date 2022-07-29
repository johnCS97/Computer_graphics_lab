
from pickle import NONE
import numpy as np
from scipy.fft import fftn, ifftn
import SRC_3D.SmoothLife.SLMathmatics3D as slm
import SRC_3D.SmoothLife.Rules3D as rs

class SmoothL:
    
    def __init__(self, width, height, depth, inner_radius, outer_radius):
        self.rows = width
        self.cols = height
        self.slices = depth
        self.angle=0
        self.rules = rs.Rules3D()
        self.inner = inner_radius
        self.outer = outer_radius
        self.game_field = np.zeros(shape=(self.rows, self.cols, self.slices))
        self.SLmathmatics = slm.Multipliers((width, height, depth),inner_radius,outer_radius)

    def create_cells(self, new_cells, age):
        
        for i in range(new_cells):
            x = np.random.randint(self.outer, self.rows - self.outer)
            y = np.random.randint(self.outer, self.cols - self.outer)
            z = np.random.randint(self.outer, self.slices - self.outer)
            for i in range(-self.outer,self.outer):
                for j in range(-self.outer,self.outer):
                    for k in range(-self.outer,self.outer):
                        if i+x>=self.rows or i+x<0:
                            continue
                        if j+y>=self.cols or j+y<0:
                            continue
                        if k+z>=self.slices or k+z<0:
                            continue
                        if np.sqrt((i / 2) ** 2 + (j / 2) ** 2+(k / 2) ** 2)<self.inner:
                            self.game_field[i+x][j+y][k+z]=1

    def next(self):
        self.angle+=0.5
        field = np.fft.fftn(self.game_field)
        M_buffer = field * self.SLmathmatics.M
        N_buffer = field * self.SLmathmatics.N
        M_buffer = np.real(np.fft.ifftn(M_buffer))
        N_buffer = np.real(np.fft.ifftn(N_buffer))
        s = self.rules.sigmaoid_new(N_buffer, M_buffer)
        dt=0.0999
        self.game_field=self.game_field+dt*(s)
        self.game_field = np.clip(self.game_field, 0, 1)
        self.game_field[0][0][0]=1
        return self.game_field

