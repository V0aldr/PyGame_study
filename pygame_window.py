"""
pygame демо 0 – только окно
"""

import pygame

import sys

import random

from pygame.locals import *

from pathlib import Path

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
# 5 – Инициализируем переменные
ball_X = random.randrange(MAX_WIDTH)
ball_Y = random.randrange(MAX_HEIGHT)
ball_rect = pygame.Rect(ball_X, ball_Y, MAX_WIDTH, MAX_HEIGHT)
target_rect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)
# 6 – Бесконечный цикл

while True:
    # 7 – Проверяем наличие событий и обрабатываем их
    for event in pygame.event.get():
        # Нажата кнопка "закрыть"? Выходим из pygame и завершаем
        # программу
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # определяем, нажал ли пользователь клавишу
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_X -= N_PIXELS_TO_MOVE
            if event.key == pygame.K_RIGHT:
                ball_X += N_PIXELS_TO_MOVE
            if event.key == pygame.K_UP:
                ball_Y -= N_PIXELS_TO_MOVE
            if event.key == pygame.K_DOWN:
                ball_Y += N_PIXELS_TO_MOVE

        # определяем, щелкнул ли пользователь
        if event.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos
            # Могли бы это сделать принеобходимости
            # проверяем, был ли щелчок в пределах прямоугольника мяча
            # Если это так, выбираем случайным образом новое
            # местоположение
            if ball_rect.collidepoint(event.pos):
                ball_X = random.randrange(MAX_WIDTH)
                ball_Y = random.randrange(MAX_HEIGHT)
                ball_rect = pygame.Rect(ball_X, ball_Y,
                                        BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # 8 – Выполняем действия "в рамках фрейма"
    # Проверяем нажатия клавиш пользователем
    keyPressedTuple = pygame.key.get_pressed()


    # определяем, перекрывает ли мяч целевое изображение
    ball_rect = pygame.Rect(ball_X, ball_Y, BALL_WIDTH_HEIGHT,
                            BALL_WIDTH_HEIGHT)
    if ball_rect.colliderect(target_rect):
        print('Ball is touching the target')
    # 9 – Очищаем окно
    window.fill(BLACK)
    # 10 – Рисуем все элементы окна.
    window.blit(target_image, (TARGET_X, TARGET_Y))
    # рисуем мяч на позиции 100 вдоль (х) и 200 вниз по (у)
    window.blit(ball_image, (ball_X, ball_Y))

    # 11 – Обновляем окно
    pygame.display.update()

    # 12 – Делаем паузу
    clock.tick(FRAMES_PER_SECOND)
