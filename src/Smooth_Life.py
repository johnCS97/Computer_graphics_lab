from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import SLMathmatics as slm
import Rules as rs
import os
import pygame


class SmoothL:

    def __init__(self, width, height, inner_radius, outer_radius):
        self.width = width
        self.height = height
        self.game_field = np.ndarray(shape=(self.width, self.height))
        self.innerR = inner_radius
        self.outerR = outer_radius
        self.rules = rs.Rules()
        self.reset_game()
        self.SLmathmatics=slm.Multipliers((width, height))

    # Create_cells: creates cells depending on inner radius
    # [x:x+y,z:z+y] array thing, runs on all array indexes included in the range

    def create_cells(self, new_cells, age):
        for i in range(new_cells):
            radius = int(self.innerR)
            x = np.random.randint(0, self.width - radius)
            y = np.random.randint(0, self.height - radius)
            self.game_field[x:x + radius, y:y + radius] = age

    def reset_game(self):
        self.game_field = np.zeros(shape=(self.width, self.height))

    def next(self):
        field_ = np.fft.fft2(self.game_field)
        m_buffer_ = field_ * self.SLmathmatics.M
        n_buffer_ = field_ * self.SLmathmatics.N
        m_buffer = np.real(np.fft.ifft2(m_buffer_))
        n_buffer = np.real(np.fft.ifft2(n_buffer_))
        s = self.rules.sigmaoid_s(n_buffer, m_buffer)
        nextfield = s
        self.game_field = np.clip(nextfield, 0, 1)
        return self.game_field

    def show(self, surface):
        for i in range(self.width):
            for j in range(self.height):
                if self.rules.b1 < self.game_field[i][j] < self.rules.b2:
                    pygame.draw.rect(surface, (255, 0, 0), [i+50, j+50, i+50, j+50])
                else:
                    pygame.draw.rect(surface, (255, 255, 255), [i + 50, j + 50, i + 50, j + 50])

os.environ["SDL_VIDEO_CENTERED"] = '1'
width, height = 500, 500
pygame.init()
size = (width, height)
screen = pygame.display.set_mode(size)
# icon = pygame.image.load("\Users\lilia\OneDrive\שולחן העבודה\Computer_graphics_lab\icons\gol_icon.png")
# pygame.display.set_icon(icon)
pygame.display.set_caption("Conway's life")

clock = pygame.time.Clock()


black = (0, 0, 0)
off_color = (255, 255, 255)
on_color = (0, 40, 150)
scaler = 10

fps =120
offset = 1

run = True
w = 500
h = 500


def show_animation():
    w = 1 << 9
    h = 1 << 9
    sl = SmoothL(h, w,1,7)
    sl.create_cells(200,1)

    while True:
        sl.next()
        fig = plt.figure()
        im = plt.imshow(sl.game_field, animated=True,
                    cmap=plt.get_cmap("viridis"), aspect="equal")
        plt.show()


if __name__ == '__main__':
    while True:
        show_animation()
    # save_animation()