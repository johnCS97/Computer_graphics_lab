from matplotlib import pyplot as ptl
from matplotlib import animation
import numpy as np
import SLMathmatics as slm
import Rules as rs

class SmoothL:
    def __init__(self, width, height, inner_radius, outer_radius):
        self.width = width
        self.height = height
        self.game_field=np.ndarray(shape=(self.width, self.height))
        self.innerR = inner_radius
        self.outerR = outer_radius

# Create_cells: creates cells depending on inner radius
# [x:x+y,z:z+y] array thing, runs on all array indexes included in the range

    def create_cells(self, new_cells, age):
        for i in range(new_cells):
            radius = int(self.innerR)
            x = np.random.randint(0, self.width-radius)
            y = np.random.randint(0, self.height-radius)
            self.game_field[x:x+radius, y:y+radius] = age

    def reset_game(self):
        self.game_field=np.zeros(shape=(self.width, self.height))




