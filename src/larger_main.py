import os

import pygame

import larger_than_life as ltl
from matplotlib import pyplot as plt
from matplotlib import animation

width, height = 200, 200
r = 5
game = ltl.Game (width, height, r)

if __name__ == '__main__':
    fig = plt.figure()
    img = plt.imshow(game.game_array, animated=True,
                    cmap=plt.get_cmap("gray"), aspect="equal")
    def animate(*args):
        img.set_array(game.next_gen())
        return img,
    ani = animation.FuncAnimation(fig, animate, interval=75, blit=True)
    plt.show()
