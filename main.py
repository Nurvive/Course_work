import pygame
import sys

TEXT_COLOR = (41, 55, 247)

pygame.init()
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Виселица')
clock = pygame.time.Clock()
background_image = pygame.image.load('images/background.png')
pygame.font.init()
font = pygame.font.Font('misc/font.otf', 40)


while True:
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
