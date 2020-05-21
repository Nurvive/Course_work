import pygame
import sys
from time import sleep
import random

trys = 7
TEXT_COLOR = (90, 100, 252)

fin = open("misc/word_rus.txt", encoding="utf-8")
data = fin.readlines()
for i in range(len(data)):
    data[i] = data[i][:-1]

pygame.init()
alphabet = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
# words = 'море'.split()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Виселица')

clock = pygame.time.Clock()

background_image = pygame.image.load('images/back.jpg')
scale_back = pygame.image.load('images/1.jpg')

pygame.font.init()

font = pygame.font.Font('misc/font.otf', 40)
line_size = font.get_linesize()
screen.blit(background_image, (0, 0))
size = font.size('Выход')
width, height = size
missed_letters = ''
already_crossing_letters = []
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


def again():
    alert("Хочешь сыграть ещё раз?(д/н)")
    button = Button()
    while 1:
        for i in pygame.event.get():
            if button.exit_button(i, x_position=SCREEN_WIDTH // 2 + SCREEN_WIDTH // 3.5 - width // 2,
                                  y_position=SCREEN_HEIGHT // 1.5 + line_size * 2):
                replay()
                main_menu()
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.KEYDOWN:
                if i.key == 108:
                    replay()
                    pygame.display.update()
                    game()
                    return 0
                elif i.key == 121:
                    replay()
                    main_menu()
            clock.tick(240)


def replay():
    global secretword
    global correct_letters
    global missed_letters
    global already_crossing_letters
    secretword = get_random_word(data)
    correct_letters = ''
    missed_letters = ''
    already_crossing_letters.clear()


def get_random_word(wordlist):
    return random.choice(wordlist)


secretword = get_random_word(data)


class Button:

    def __init__(self):
        self.playButton_presence = False
        self.exitButton_presence = False

    def play_button(self, event):
        x_position = SCREEN_WIDTH // 2 - width // 2
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

    def exit_button(self, event, x_position=SCREEN_WIDTH // 2 - width // 2, y_position=200 + line_size * 2):
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


def drawing_alphabet():
    k = SCREEN_WIDTH // 1.6
    e = SCREEN_HEIGHT // 6
    global letter_position
    letter_position = []
    for i in range(len(alphabet)):
        text = font.render(alphabet[i], True, TEXT_COLOR)
        screen.blit(text, (k, e))
        letter_position.append((k, e))
        k += 50
        if i % 8 == 0 and i != 0:
            k = SCREEN_WIDTH // 1.6
            e += 65
    return letter_position


def check_letter(letter):
    global correct_letters
    global missed_letters
    if letter in secretword:
        correct_letters = correct_letters + letter
        foundallletters = True
        crossing_letter(letter)
        for i in range(len(secretword)):
            if secretword[i] not in correct_letters:
                foundallletters = False
                break

        if foundallletters:
            display_secret_word()
            alert('ты угадал - ' + secretword)
            sleep(1.5)
            painting_alert()
            return True

    else:
        missed_letters = missed_letters + letter
        draw_hangman()
        crossing_letter(letter)
        if len(missed_letters) == (trys - 1):
            display_secret_word()
            alert('не угадал, слово было - ' + secretword)
            sleep(1.5)
            painting_alert()
            return True


def crossing_letter(letter):
    for i in (missed_letters + correct_letters):
        if i not in already_crossing_letters:
            x2 = letter_position[alphabet.index(i)][0] + font.size(letter)[0] + 1
            y2 = letter_position[alphabet.index(i)][1]
            slash = font.render('/', True, (255, 0, 0))
            screen.blit(slash, (x2 - 19, y2 + 6))
            pygame.display.update()
            already_crossing_letters.append(letter)


def display_secret_word():
    blanks = '_' * len(secretword)
    for i in range(len(secretword)):
        if secretword[i] in correct_letters:
            blanks = blanks[:i] + secretword[i] + blanks[i + 1:]
    k = SCREEN_WIDTH // 2.5
    for letter in blanks:
        blank = font.render(letter, 1, TEXT_COLOR)
        screen.blit(blank, (k, 20))
        k += 30
        pygame.display.update()


def draw_hangman():
    base = False

    if not base:
        pygame.draw.rect(screen, (0, 0, 255), (100, SCREEN_HEIGHT // 1.5 + line_size * 2, 150, 8))
        pygame.draw.rect(screen, (0, 0, 255), (171, SCREEN_HEIGHT // 1.5 + line_size * 2, 8, -450))
        pygame.draw.rect(screen, (0, 0, 255), (171, SCREEN_HEIGHT // 1.5 + line_size * 2 - 455, 80, 8))
        pygame.draw.rect(screen, (0, 0, 255), (251, SCREEN_HEIGHT // 1.5 + line_size * 2 - 455, 8, 50))

        base = True

    if len(missed_letters) == 1:
        pygame.draw.circle(screen, (0, 0, 255), (255, 210), 30, 5)

    if len(missed_letters) == 2:
        pygame.draw.rect(screen, (0, 0, 255), (253, 235, 5, 100))

    if len(missed_letters) == 3:
        pygame.draw.line(screen, (0, 0, 255), (253, 335), (233, 375), 5)

    if len(missed_letters) == 4:
        pygame.draw.line(screen, (0, 0, 255), (258, 335), (273, 375), 5)

    if len(missed_letters) == 5:
        pygame.draw.line(screen, (0, 0, 255), (253, 255), (233, 295), 5)

    if len(missed_letters) == 6:
        pygame.draw.line(screen, (0, 0, 255), (258, 255), (273, 295), 5)
        base = False


def game():
    game = True
    screen.blit(background_image, (0, 0))

    drawing_alphabet()
    display_secret_word()
    pygame.display.update()
    button = Button()
    while game:
        clock.tick(240)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if button.exit_button(event, x_position=SCREEN_WIDTH // 2 + SCREEN_WIDTH // 3.5 - width // 2,
                                  y_position=SCREEN_HEIGHT // 1.5 + line_size * 2):
                replay()
                main_menu()

            draw_hangman()

            if event.type == pygame.KEYDOWN:
                painting_alert()
                if event.key in key_buttons.keys() or event.key == 27:
                    guess = get_guess(missed_letters + correct_letters, event)
                    if isinstance(guess, str):
                        if check_letter(guess):
                            again()
                    display_secret_word()

        pygame.display.update()


def alert(text):
    txt = font.render(text, True, TEXT_COLOR)
    screen.blit(txt, (450 // 2, 500))

    pygame.display.update()
    # sleep(1)
    # screen.blit(scale_back, (400 // 2, 470))
    # pygame.display.update()

def painting_alert():
    screen.blit(scale_back, (400 // 2, 470))
    pygame.display.update()

def get_guess(alreadyguessed, event):
    while True:
        for i in key_buttons.keys():
            if i == event.key:
                if key_buttons[i] in alreadyguessed:
                    alert("Эта буква уже была")
                    return -1
                else:
                    return key_buttons[i]
            elif event.key == 27:
                main_menu()
        clock.tick(240)


def main_menu():
    while True:
        for event in pygame.event.get():
            button = Button()
            screen.blit(background_image, (0, 0))

            if event.type == pygame.QUIT:
                sys.exit()

            if button.play_button(event):
                game()

            if button.exit_button(event):
                sys.exit()

            pygame.display.update()
            clock.tick(240)


if __name__ == '__main__':
    main_menu()
