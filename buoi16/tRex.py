import pygame
import sys
from pygame.locals import *

# khởi tạo game
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 500))
DISPLAYSURF.fill((255, 255, 255))

pygame.display.set_caption("T-Rex")


class Ground():
    def __init__(self):
        self.x = 0
        self.y = 400
        self.surface = pygame.Surface((1200, 12), pygame.SRCALPHA)
        self.surface.blit(pygame.image.load(
            "./img/ground.png"), (0, 0, 1200, 12))

    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, self.y))

class Cactus():
    def __init__(self):
        self.x = 300
        self.y = 360
        self.surface = pygame.Surface((73, 46), pygame.SRCALPHA)
        self.surface.blit(pygame.image.load(
            "./img/cactus.png"), (0, 0, 73, 46))
        self.rect= self.surface.get_rect(topleft=(self.x,self.y))

    def draw(self):
        self.x -= 5
        self.rect.topleft = (self.x,self.y)
        if self.x < 0:
            self.x=810
        DISPLAYSURF.blit(self.surface, (self.x, self.y))



class TRex():
    def __init__(self):
        self.x = 0
        self.y = 360

        self.surface = pygame.Surface((55, 43),pygame.SRCALPHA)
        self.surface.blit(pygame.image.load(
            "./img/tRex.png"), (0, 0), (0, 0, 40, 43))

        self.option = 0
        self.timeCount = 0
        self.SPEED = 5

        self.high = 20
        self.jump = False

        self.rect= self.surface.get_rect(topleft=(self.x,self.y))

    def updateRect(self):
        self.rect.topleft = (self.x,self.y)

    def update(self, up, down, left, right):
        self.surface.fill((0, 0, 0, 0))

        if up:
            self.jump = True

        if self.jump:
            if self.high >= -20:
                self.y -= self.high
                self.high -= 1
            else:
                self.jump=False
                self.high =20

        if down:
            if self.timeCount <= self.SPEED:  # 0 - 5
                self.option = 4
            elif self.timeCount <= self.SPEED*2:
                self.option = 5
        else:
            if self.timeCount <= self.SPEED:  # 0 - 5
                self.option = 0
            elif self.timeCount <= self.SPEED*2:  # 6 - 10
                self.option = 1
            elif self.timeCount <= self.SPEED*3:  # 11 - 15
                self.option = 2
        
        if self.timeCount > self.SPEED*3:
                self.timeCount = 0

        if left:
            self.x -= 2
            self.timeCount += 1

        if right:
            self.x += 2
            self.timeCount += 1
        self.animate()

    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, self.y))

    def animate(self):
        if self.option == 0:
            self.surface.blit(pygame.image.load(
                "./img/tRex.png"), (0, 0), (0, 0, 40, 43))
        if self.option == 1:
            self.surface.blit(pygame.image.load(
                "./img/tRex.png"), (0, 0),  (40, 0, 40, 43))
        if self.option == 2:
            self.surface.blit(pygame.image.load(
                "./img/tRex.png"), (0, 0), (80, 0, 40, 43))
        if self.option == 3:
            self.surface.blit(pygame.image.load(
                "./img/tRex.png"), (0, 0),  (120, 0, 40, 43))
        if self.option == 4:
            self.surface.blit(pygame.image.load(
                "./img/tRex.png"), (0, 0), (160, 0, 55, 43))
        if self.option == 5:
            self.surface.blit(pygame.image.load(
                "./img/tRex.png"), (0, 0), (215, 0, 55, 43))


ground = Ground()
tRex = TRex()
cactus = Cactus()

up, down, left, right = False, False, False, False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                up = True
            if event.key == K_DOWN:
                down = True
            if event.key == K_LEFT:
                left = True
            if event.key == K_RIGHT:
                right = True

        if event.type == KEYUP:
            if event.key == K_UP:
                up = False
            if event.key == K_DOWN:
                down = False
            if event.key == K_LEFT:
                left = False
            if event.key == K_RIGHT:
                right = False

    DISPLAYSURF.fill((255, 255, 255))

    ground.draw()
    tRex.draw()
    tRex.update(up, down, left, right)
    cactus.draw()

    tRex.updateRect()

    if tRex.rect.colliderect(cactus.rect):
        print("đã đụng")
       

    pygame.display.update()  # cập nhật lại các trạng thái của pygame
    pygame.time.Clock().tick(60)  # FPS
