import pygame
import sys
from pygame.locals import *


lstMap = [{
    'key': 1,
    'X': 15,
    'Y': 15,
    'nei': [2, 6]
},
    {
    'key': 2,
    'X': 130,
    'Y': 15,
    'nei': [1, 7]
},
    {
    'key': 3,
    'X': 245,
    'Y': 15,
    'nei': [4, 8]
},
    {
    'key': 4,
    'X': 360,
    'Y': 15,
    'nei': [3, 5]
},
    {
    'key': 5,
    'X': 495,
    'Y': 15,
    'nei': [4]
},

    {
    'key': 6,
    'X': 15,
    'Y': 130,
    'nei': [1, 11]
},
    {
    'key': 7,
    'X': 130,
    'Y': 130,
    'nei': [2, 8]
},
    {
    'key': 8,
    'X': 245,
    'Y': 130,
    'nei': [3, 7, 9]
},
    {
    'key': 9,
    'X': 360,
    'Y': 130,
    'nei': [8, 10, 14]
},
    {
    'key': 10,
    'X': 495,
    'Y': 130,
    'nei': [9, 15]
},
    {
    'key': 11,
    'X': 15,
    'Y': 245,
    'nei': [6, 12, 16]
},
    {
    'key': 12,
    'X': 130,
    'Y': 245,
    'nei': [11, 13]
},
    {
    'key': 13,
    'X': 245,
    'Y': 245,
    'nei': [12, 18]
},
    {
    'key': 14,
    'X': 360,
    'Y': 245,
    'nei': [9, 19]
},
    {
    'key': 15,
    'X': 495,
    'Y': 245,
    'nei': [10]
},
    {
    'key': 16,
    'X': 15,
    'Y': 360,
    'nei': [11, 17]
},
    {
    'key': 17,
    'X': 130,
    'Y': 360,
    'nei': [16, 22]
},
    {
    'key': 18,
    'X': 245,
    'Y': 360,
    'nei': [13, 23]
},
    {
    'key': 19,
    'X': 360,
    'Y': 360,
    'nei': [14, 20]
},
    {
    'key': 20,
    'X': 495,
    'Y': 360,
    'nei': [19, 25]
},
    {
    'key': 21,
    'X': 15,
    'Y': 495,
    'nei': [22]
},
    {
    'key': 22,
    'X': 130,
    'Y': 495,
    'nei': [17, 21]
},
    {
    'key': 23,
    'X': 245,
    'Y': 495,
    'nei': [18]
},
    {
    'key': 24,
    'X': 360,
    'Y': 495,
    'nei': [25]
},
    {
    'key': 25,
    'X': 495,
    'Y': 495,
    'nei': [20, 24]
},
]


class Vertex:
    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y


class Graqh:
    def __init__(self):
        self.lstVertex = {}
        self.lstEdge = {}

    def addVertex(self, key, x, y):
        vertex = Vertex(key, x, y)

        self.lstVertex[key] = vertex

        if key not in self.lstEdge:
            self.lstEdge[key] = []

    def addEdge(self, vertex, nei):
        self.lstEdge[vertex] = nei

    def dfs(self, startKey, endKey, visited=None, path=None, result=None):

        if visited is None:
            visited = set()

        if path is None:
            path = []
        if result is None:
            result = []
        visited.add(startKey)
        path.append(self.lstVertex[startKey])

        if startKey == endKey:
            for node in path:
                result.append({'key': node.key, 'X': node.x,
                              'Y': node.y})  # [{key,X,Y}]
        else:
            for neighbour in self.lstEdge[startKey]:
                if neighbour not in visited:
                    self.dfs(neighbour, endKey, visited, path, result)

        path.pop()
        visited.remove(startKey)

        return result


graqh = Graqh()
for item in lstMap:
    graqh.addVertex(item["key"], item["X"], item["Y"])
    graqh.addEdge(item["key"], item["nei"])


pygame.init()
DISPLAYSUF = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Maze dot")


class Dot():
    def __init__(self):
        self.x = 245
        self.y = 15
        self.surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.surface.blit(pygame.transform.scale(
            pygame.image.load("./img/dot.png"), (100, 100)
        ), (0, 0))
        self.lstNode = graqh.dfs(3, 23)  # [3,8,7,2,1,..]
        print(self.lstNode )
        self.find = self.lstNode[0]

    def run(self):

        # logic xử lý animation
        if self.x != self.find['X']:
            # qua trái phải
            if self.x > self.find['X']:  # qua trái
                self.x -= 5
            else:
                self.x += 5

        elif self.y != self.find['Y']:
            # lên xuống
            if self.y > self.find['Y']:  # xuống
                self.y -= 5
            else:
                self.y += 5

        elif len(self.lstNode) > 0:
            self.find = self.lstNode.pop(0)

    def draw(self):
        DISPLAYSUF.blit(self.surface, (self.x, self.y))


isStart = False
dot = Dot()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                isStart = True

    DISPLAYSUF.fill((255, 255, 255))

    DISPLAYSUF.blit(pygame.image.load("./img/maze_map.png"), (0, 0))
    dot.draw()

    if isStart:
        dot.run()

    pygame.display.update()
    pygame.time.Clock().tick(60)
