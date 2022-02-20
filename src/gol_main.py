import os

import pygame

import game_of_life as gol

os.environ["SDL_VIDEO_CENTERED"] = '1'
width, height = 700, 700
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

fps =20
offset = 1
conway = gol.Game(scaler, width, height, offset)
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

