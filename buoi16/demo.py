import pygame
import sys
from pygame.locals import *

# khởi tạo game
pygame.init()

# gán Width, Height khung cửa sổ game
DISPLAYSURF = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Hello")

x = 0
y = 0
x2 = 0
# xử lý item
rectSurface = pygame.Surface((150, 10))
rectSurface.fill((128, 128, 0))

rectSurface2 = pygame.Surface((350, 150))
rectSurface2.fill((255, 0, 0))

# khởi tạo 2 biến xử lý va chạm
rect = rectSurface.get_rect(topleft=(0, 30))
rect2 = rectSurface2.get_rect(topleft=(0, 150))

# vòng lặp game
while True:
    # xử lý sự kiện trong pygame
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    DISPLAYSURF.fill((255, 255, 255))  # gắn màu nền cho cửa sổ

    DISPLAYSURF.blit(rectSurface, rect)
    DISPLAYSURF.blit(rectSurface2, rect2)

    rect.x += 1
    rect.y += 1
    rect2.x -= 10

    if rect2.x < -350:
        rect2.x = 800

    # kiểm tra va chạm
    if rect.colliderect(rect2):
        rectSurface2.fill((255, 0, 255))
    else:
        rectSurface2.fill((255, 0, 0))

    pygame.display.update()  # cập nhật lại các trạng thái của pygame
    pygame.time.Clock().tick(60)  # FPS
