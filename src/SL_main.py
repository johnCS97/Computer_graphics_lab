import Smooth_Life_version1
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import SLMathmatics as slm
import Rules as rs
import os
import pygame
if __name__ == '__main__':
    sl = Smooth_Life_version1.SmoothL(100, 100,3,9)
    sl.create_cells(50,1)
    fig = plt.figure()
    # Nice color maps: viridis, plasma, gray, binary, seismic, gnuplot
    im = plt.imshow(sl.game_field, animated=True,
                    cmap=plt.get_cmap("plasma"), aspect="equal")
    def animate(*args):
        im.set_array(sl.next())
        return (im, )

    ani = animation.FuncAnimation(fig, animate, interval=60, blit=True)
    plt.show()
