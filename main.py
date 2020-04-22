import pygame
import sys
from time import sleep
import random

TEXT_COLOR = (90, 100, 252)

pygame.init()
alphabet = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
words = 'муха кошка пиво лампа шершень лимон хорёк вымпел гроза курица чукча таблица царство мощь носки ножницы арбуз пингвин'.split()
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
size = font.size('Выход')
width, height = size
missed_letters = ''
correct_letters = ''
key_buttons = {
    97: 'ф',
    98: 'и',
    99: 'с',
    113: 'й',
    119: 'ц',
    103: 'п',
    101: 'у',
    104: 'р',
    114: 'к',
    106: 'о',
    116: 'е',
    107: 'л',
    121: 'н',
    108: 'д',
    117: 'г',
    122: 'я',
    105: 'ш',
    120: 'ч',
    111: 'щ',
    118: 'м',
    112: 'з',
    110: 'т',
    115: 'ы',
    109: 'ь',
    100: 'в',
    59: 'ж',
    102: 'а',
    44: 'б',
    46: 'ю',
    91: 'х',
    93: 'ъ',
    39: 'э',
    96: 'ё'
}


class Button:

    def __init__(self):
        self.playButton_presence = False
        self.exitButton_presence = False

    def playButton(self, event):
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

    def exitButton(self, event, x_position=400 - width / 2, y_position=200 + line_size * 2):
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
    game = True
    secretword = getRandomWord(words)
    screen.blit(background_image, (0, 0))
    k = 450
    e = 70
    letter_position = []

    for i in range(len(alphabet)):
        text = font.render(alphabet[i], True, TEXT_COLOR)
        screen.blit(text, (k, e))
        letter_position.append((k, e))
        k += 50
        if i % 9 == 0 and i != 0:
            k = 450
            e += 65

    text = font.render(secretword, True, TEXT_COLOR)
    screen.blit(text, (700 // 2, 30))
    pygame.display.update()

    while game:

        clock.tick(60)
        for event in pygame.event.get():
            button = Button()
            if event.type == pygame.QUIT:
                exit()
            if button.exitButton(event, x_position=650 - width / 2, y_position=350 + line_size * 2):
                main_menu()
            if event.type == pygame.KEYDOWN:
                guess = getGuess(missed_letters + correct_letters, event)

        pygame.display.update()
    # TODO: написать Виселицу. В левой части окна отрисовка картинки виселицы,
    #  в правой - массив кнопок букв. Сверху слово


def getRandomWord(wordlist):
    wordindex = random.randint(0, len(wordlist) - 1)
    return wordlist[wordindex]


def alert(text):
    pygame.draw.rect(screen, (169, 169, 169), (width // 2, height // 2, 150, 120))
    txt = font.render(text, True, TEXT_COLOR)
    screen.blit(txt, (width // 2 + 50, height // 2 + 30))
    pygame.display.update()
    sleep(1)


def getGuess(alreadyguessed, event):
    while True:
        for i in key_buttons.keys():
            if i == event.key:
                if key_buttons[i] in alreadyguessed:
                    alert("Эта буква уже была")
                else:
                    return key_buttons[i]
            else:
                main_menu()
        clock.tick(60)


def main_menu():
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


if __name__ == '__main__':
    secretword = getRandomWord(words)
    main_menu()
