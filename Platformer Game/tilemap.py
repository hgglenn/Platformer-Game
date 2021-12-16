import pygame
from settings import *

class Map:
    def __init__(self, filename):
        game_folder = os.path.dirname(__file__)
        self.data = []
        with open(os.path.join(game_folder, "map2.txt"), "rt") as map:
            for line in map:
                self.data.append(line.rstrip())
                
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE
        
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = 0
        x = min(0, x)
        x = max(-(self.width - WIDTH), x)        
        self.camera = pygame.Rect(x, y, self.width, self.height)
        
    