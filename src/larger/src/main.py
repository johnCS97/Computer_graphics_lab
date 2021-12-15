import os

import pygame

import larger_than_life as ltl

os.environ["SDL_VIDEO_CENTERED"] = '1'
width, height = 1280, 720
pygame.init()
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Larger than life")

clock = pygame.time.Clock()


black = (0, 0, 0)
off_color = (255, 255, 255)
on_color = (0, 40, 150)
scaler = 5


fps =500
offset = 1
r=4
game = ltl.Game(scaler, width, height, offset, r)
game.array_init()
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    game.conway_life(screen, off_color, on_color)
    pygame.display.update()