from dijstra_google import Graph
import json

import pygame
import sys
from pygame.locals import *

with open('./data.json', 'r') as file:
    dataMap = json.load(file)

grap = Graph()
grap.load_from_json(dataMap)


def check_key_in_data(key, data):
    for item in data:
        if item['key'] == key:
            return item
    return None


pygame.init()
DISPLAYSURF = pygame.display.set_mode((1720, 980))
pygame.display.set_caption("Google map !")

font = pygame.font.Font(None, 24)  # sử dụng font mặc định của Pygame

color = []

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if len(color) >= 2:
                color = []

            for item in dataMap:
                locat = pygame.Surface((30, 30))
                locat_pos = (item['X'], item['Y'])
                rect = locat.get_rect(topleft=locat_pos)

                if rect.collidepoint(mouse_pos):
                    if item not in color:
                        color.append(item)

    surfaceMap = pygame.transform.scale(
        pygame.image.load("./img/map.png"), (1720, 980))

    DISPLAYSURF.blit(surfaceMap, (0, 0))

    if len(color) == 2:
        path = grap.dijkstra(color[0]["key"], color[1]["key"])

        index = 0
              # 1,4,3,6,8,10,11
        for item in path:
            if index+1 < len(path):
                startKey = check_key_in_data(item, dataMap)
                nextKey = check_key_in_data(path[index+1], dataMap)

                pygame.draw.line(DISPLAYSURF, (0, 255, 0),
                                         (startKey['X']+15, startKey['Y']+15), (nextKey['X']+15, nextKey['Y']+15), 10)

            index += 1

    for item in dataMap:
        locat = pygame.Surface((30, 30))
        text_surface = font.render(str(item['key']), True, (0, 0, 0))

        if check_key_in_data(item['key'], color):
            locat.fill((255, 255, 0))
        else:
            locat.fill((255, 0, 0))
        locat.blit(text_surface, (10, 10))
        DISPLAYSURF.blit(locat, (item['X'], item['Y']))

    pygame.display.update()
    pygame.time.Clock().tick(60)
