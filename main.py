import pygame
import sys


TEXT_COLOR = (90, 100, 252)

pygame.init()
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Виселица')
clock = pygame.time.Clock()
background_image = pygame.image.load('images/background.png')
pygame.font.init()
font = pygame.font.Font('misc/font.otf', 40)
line_size = font.get_linesize()
screen.blit(background_image, (0, 0))


class Button:

    def __init__(self):
        self.playButton_presence = False
        self.exitButton_presence = False

    def playButton(self, event):
        size = font.size('Играть')
        width, height = size
        x_position = 400 - width / 2
        y_position = 200
        position = (x_position, y_position)
        if not self.playButton_presence:
            text = font.render('Играть', True, TEXT_COLOR)
            screen.blit(text, position)
            self.playButton_presence = True
        x, y = pygame.mouse.get_pos()
        if (x_position <= x <= x_position + width) and (
                y_position <= y <= y_position + height) and event.type == pygame.MOUSEBUTTONDOWN:
            return True

    def exitButton(self, event):
        size = font.size('Выход')
        width, height = size
        x_position = 400 - width / 2
        y_position = 200 + line_size * 2
        position = (x_position, y_position)
        if not self.exitButton_presence:
            text = font.render('Выход', True, TEXT_COLOR)
            screen.blit(text, position)
            self.exitButton_presence = True
        x, y = pygame.mouse.get_pos()
        if (x_position <= x <= x_position + width) and (
                y_position <= y <= y_position + height) and event.type == pygame.MOUSEBUTTONDOWN:
            return True

        # TODO: реализовать обведение/подчеркивание кнопок при наведении курсора


def pressed(btn: Button):
    pass
# TODO: нажатие клавиши = MOUSEBUTTONDOWN + MOUSEBUTTONUP


def game():
    game_over = False

    if not game_over:
        screen.blit(background_image, (0, 0))
        text = font.render('Игра началась', True, TEXT_COLOR)
        screen.blit(text, (0, 0))
        pygame.display.update()

    # TODO: написать Виселицу. В левой части окна отрисовка картинки виселицы,
    #  в правой - массив кнопок букв. Сверху слово


while True:
    for event in pygame.event.get():
        button = Button()
        screen.blit(background_image, (0, 0))

        if event.type == pygame.QUIT:
            sys.exit()

        if button.playButton(event):
            game()

        if button.exitButton(event):
            sys.exit()

        pygame.display.update()
        clock.tick(60)