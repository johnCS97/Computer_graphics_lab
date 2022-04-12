import os
import pygame
import Pivato as Pv
from matplotlib import pyplot as plt
from matplotlib import animation

width, height = 100, 100
r = 5
game = Pv.Game (width, height, r)

if __name__ == '__main__':
    fig = plt.figure()
    img = plt.imshow(game.game_array, animated=True,
                    cmap=plt.get_cmap("plasma"), aspect="equal")
    def animate(*args):
        img.set_array(game.next_gen())
        return img,
    ani = animation.FuncAnimation(fig, animate, interval=75, blit=True)
    plt.show()
