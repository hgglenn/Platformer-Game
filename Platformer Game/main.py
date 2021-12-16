import pygame
import sys
from settings import *
from sprites import *
import os
from tilemap import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_icon(ICON)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = os.path.dirname(__file__)
        self.map = Map(os.path.join(game_folder, "map.txt"))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        BackGround(self)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Block(self, col, row, "1")
                if tile == "2":
                    Block(self, col, row, "2")
                if tile == "3":
                    Block(self, col, row, "3")
                if tile == "P":
                    self.player = Player(self, col, row)
                if tile == "D":
                    Mob(self, col, row)                    
        self.camera = Camera(self.map.width, self.map.height)
                

    def run(self):
        # Game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing == True:
            self.timeStep = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # The update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self, state):
        if state == True:
            for x in range(0, WIDTH, TILESIZE):
                pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT, TILESIZE):
                pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        #pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BGCOLOR)
        self.draw_grid(GRID)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()            

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
while True:
    g.show_start_screen()
    g.new()
    g.run()
    g.show_go_screen()