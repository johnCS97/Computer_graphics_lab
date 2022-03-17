from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import SLMathmatics as slm
import mpl_toolkits.mplot3d.axes3d as p3
import Rules3D as rs
import os
import pygame


class SmoothL:

    def __init__(self, width, height,depth, inner_radius=10, outer_radius=30):
        self.rows = width
        self.cols = height
        self.slices=depth
        self.rules = rs.Rules3D()
        self.inner = inner_radius
        self.outer = outer_radius
        self.game_field = np.zeros(shape=(self.rows, self.cols,self.slices))
        self.SLmathmatics = slm.Multipliers((width, height,depth))
        

    # Create_cells: creates cells depending on inner radius
    # [x:x+y,z:z+y] array thing, runs on all array indexes included in the range

    def create_cells(self, new_cells, age):
        for i in range(new_cells):
            x = np.random.randint(self.outer, self.rows - self.outer)
            y = np.random.randint(self.outer, self.cols - self.outer)
            z = np.random.randint(self.outer, self.slices - self.outer)
            
            self.game_field[x-self.outer:x + self.outer, y-self.outer:y + self.outer,z-self.outer:z + self.outer] = age

    def next(self):
        field = np.fft.fftn(self.game_field)
        M_buffer = field * self.SLmathmatics.M
        N_buffer = field * self.SLmathmatics.N
        M_buffer = np.real(np.fft.ifftn(M_buffer))
        N_buffer = np.real(np.fft.ifftn(N_buffer))
        s = self.rules.sigmaoid_s(N_buffer, M_buffer)
        
        self.game_field = np.clip(s, 0, 1)
        return self.game_field
        
if __name__ == '__main__':
    sm=SmoothL(20, 20, 20,1,3)
    sm.create_cells(4,0.32)
    ax = plt.figure().add_subplot(projection='3d')
    ax.axis('off')
    ax.voxels(sm.game_field,facecolor="#4d4d4d",edgecolors='black')
    def animate(*args):
        plt.cla()
        ax.axis('off')
        ax.voxels(sm.next(),facecolor="#4d4d4d",edgecolors='black',shade=True)
        return ax,
    ani = animation.FuncAnimation(ax.figure, animate, interval=20, blit=True)
    plt.show()
