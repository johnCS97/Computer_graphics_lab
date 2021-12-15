import os

import pygame

import Larger than Life as LTL

os.environ["SDL_VIDEO_CENTERED"] = '1'
width, height = 1280, 720
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
scaler = 15


fps =500
offset = 1
conway = LTL.Game(scaler, width, height, offset, 4)
conway.array_init()
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    conway.conway_life(screen, off_color, on_color)
    pygame.display.update()