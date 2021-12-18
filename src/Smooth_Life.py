from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import SLMathmatics as slm
import Rules as rs
import os
import pygame


class SmoothL:

    def __init__(self, width, height, inner_radius=30, outer_radius=90):
        self.width = width
        self.height = height
        self.rules = rs.Rules()
        self.game_field = np.zeros((self.width, self.height))
        self.SLmathmatics = slm.Multipliers((width, height))

    # Create_cells: creates cells depending on inner radius
    # [x:x+y,z:z+y] array thing, runs on all array indexes included in the range

    def create_cells(self, new_cells, age):
        for i in range(new_cells):
            radius = int(self.SLmathmatics.INNER_RADIUS)
            x = np.random.randint(0, self.width - radius)
            y = np.random.randint(0, self.height - radius)
            self.game_field[x:x + radius, y:y + radius] = age


    def next(self):
        # To sum up neighbors, do kernel convolutions
        # by multiplying in the frequency domain
        # and converting back to spacial domain
        field_ = np.fft.fft2(self.game_field)
        M_buffer_ = field_ * self.SLmathmatics.M
        N_buffer_ = field_ * self.SLmathmatics.N
        M_buffer = np.real(np.fft.ifft2(M_buffer_))
        N_buffer = np.real(np.fft.ifft2(N_buffer_))
        # Apply transition rules
        s = self.rules.sigmaoid_s(N_buffer, M_buffer)
        nextfield = s
        self.game_filed = np.clip(nextfield, 0, 1)
        return self.game_field

def show_animation():
    w = 1 << 9
    h = 1 << 9
    # w = 1920
    # h = 1080
    sl = SmoothL(h, w)
    sl.create_cells(200, 1)
    sl.next()
    fig = plt.figure()
    # Nice color maps: viridis, plasma, gray, binary, seismic, gnuplot
    im = plt.imshow(sl.game_field, animated=True,
                    cmap=plt.get_cmap("viridis"), aspect="equal")

    def animate(*args):
          im.set_array(sl.next())
          return (im, )

    ani = animation.FuncAnimation(fig, animate, interval=60, blit=True)
    plt.show()


def save_animation():
    w = 1 << 8
    h = 1 << 8
    # w = 1920
    # h = 1080
    sl = SmoothL(h, w)
    sl.create_cells(200, 1)

    # Matplotlib shoves a horrible border on animation saves.
    # We'll do it manually. Ugh

  #  from skvideo.io import FFmpegWriter
   # from matplotlib import cm

    fps = 10
    frames = 100
  #  w = FFmpegWriter("smoothlife.mp4", inputdict={"-r": str(fps)})
    for i in range(frames):
        frame = cm.viridis(sl.field)
        frame *= 255
        frame = frame.astype("uint8")
        w.writeFrame(frame)
        sl.step()
    w.close()

    # Also, webm output isn't working for me,
    # so I have to manually convert. Ugh
    # ffmpeg -i smoothlife.mp4 -c:v libvpx -b:v 2M smoothlife.webm


if __name__ == '__main__':
    show_animation()
    # save_animation()