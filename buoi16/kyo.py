import pygame
import sys
from pygame.locals import *

# khởi tạo game
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 500))
DISPLAYSURF.fill((255, 255, 255))

pygame.display.set_caption("Hello")

surface = pygame.Surface((150, 105), pygame.SRCALPHA)

x = 50
y = 250


def animate(option, url):
    if option == 0:
        surface.blit(pygame.image.load(url), (0, 0), (0, 0, 150, 105))
    if option == 1:
        surface.blit(pygame.image.load(url), (0, 0), (150, 0, 150, 105))
    if option == 2:
        surface.blit(pygame.image.load(url), (0, 0), (290, 0, 150, 105))
    if option == 3:
        surface.blit(pygame.image.load(url), (0, 0), (430, 0, 150, 105))
    if option == 4:
        surface.blit(pygame.image.load(url), (0, 0), (570, 0, 150, 105))
    if option == 5:
        surface.blit(pygame.image.load(url), (0, 0), (720, 0, 150, 105))


url = './img/kyo.png'
left = False
right = False
timeCount = 0
SPEED = 5
option = 0

high = 20
jump = False

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                jump = True
            # if event.key == K_DOWN:
            #     y += 100
            if event.key == K_LEFT:
                left = True
            if event.key == K_RIGHT:
                right = True

        if event.type == KEYUP:
            if event.key == K_LEFT:
                left = False
            if event.key == K_RIGHT:
                right = False
        

    if left:
        x -= 5
        timeCount += 1
        url = './img/kyo_r.png'

    if right:
        x += 5
        timeCount += 1
        url = './img/kyo.png'

    if jump:
        if high >= -20:
            y -= high
            high -= 1
        else:
            jump=False
            high =20

    DISPLAYSURF.fill((255, 255, 255))

    surface.fill((0, 0, 0, 0))

    if timeCount <= SPEED:  # 0 - 5
        option = 5
    elif timeCount <= SPEED*2:  # 6 - 10
        option = 4
    elif timeCount <= SPEED*3:  # 11 - 15
        option = 3
    elif timeCount <= SPEED*4:  # 16 - 20
        option = 2
    elif timeCount <= SPEED*5:  # 21 - 25
        option = 1
    elif timeCount <= SPEED*6:  # 26 - 30
        option = 0

    elif timeCount > SPEED*6:
        timeCount = 0

    animate(option, url)

    DISPLAYSURF.blit(surface, (x, y))

    pygame.display.update()  # cập nhật lại các trạng thái của pygame
    pygame.time.Clock().tick(60)  # FPS
