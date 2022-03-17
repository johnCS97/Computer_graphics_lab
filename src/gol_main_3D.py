import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import game_of_life_3D as gol_3D
import time


if __name__ == '__main__':
    conway=gol_3D.Game(10,10,10,500)
    ax = plt.figure().add_subplot(projection='3d')
    
    ax.axis('off')
    ax.voxels(conway.game_array,facecolor="#4d4d4d",edgecolors='black')
    def animate(*args):
        plt.cla()
        
        ax.axis('off')
        ax.voxels(conway.next_gen(),facecolor="#4d4d4d",edgecolors='black')
        return ax,
    ani = animation.FuncAnimation(ax.figure, animate, interval=300, blit=True)
    plt.show()