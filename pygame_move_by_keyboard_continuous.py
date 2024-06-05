"""
pygame демо 3 – одно изображение, непрерывный режим, перемещать,
пока зажата клавиша
"""

import pygame

import sys

from pygame.locals import *

# 2 – Определяем константы
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

# 3 – Инициализируем окружение pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 – Загружаем элементы: изображения, звуки и т. д.
ball_image = pygame.image.load("images/ball.png")
target_image = pygame.image.load("images/target.jpg")


# 7 – Проверяем наличие событий и обрабатываем их
