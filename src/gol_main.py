import os

import pygame

import game_of_life as gol
from matplotlib import pyplot as plt
from matplotlib import animation
width, height = 100, 100

conway = gol.Game(width, height)
run = True
if __name__ == '__main__':
    fig = plt.figure()
    img = plt.imshow(conway.game_array, animated=True,
                    cmap=plt.get_cmap("binary"), aspect="equal")
    def animate(*args):
        img.set_array(conway.next_gen())
        return img,
    ani = animation.FuncAnimation(fig, animate, interval=75, blit=True)
    plt.show()