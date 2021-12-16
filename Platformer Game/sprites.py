import pygame
from settings import *
from math import *
from random import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.image.load(PLAYER_IDLE)
        self.rect = self.image.get_rect()
        self.image.set_colorkey("#00ff00")
        self.velocityX, self.velocityY = 0, 0
        self.accelerationX, self.accelerationY = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.jumping = False
        self.sprint = False
        self.playerFrame = 0

    def jump(self):
        # jump only if standing on a block
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        self.rect.y -= 1
        if hits and self.jumping == False:
            self.velocityY = PLAYER_JUMP
            self.jumping = True
            
    def graphics(self):
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        self.rect.y -= 1
        self.rect.x += 1
        sideHits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        self.rect.x -= 1
        if not(hits):
            if self.velocityX > 0:
                self.image = pygame.image.load(PLAYER_JUMP_RIGHT)
                self.image.set_colorkey("#00ff00")
            elif self.velocityX < 0:
                self.image = pygame.image.load(PLAYER_JUMP_LEFT)
                self.image.set_colorkey("#00ff00")
        elif self.velocityX > 0 and hits and not(sideHits):
            self.image = pygame.image.load(PLAYER_MOVE_RIGHT[self.playerFrame])            
            self.image.set_colorkey("#00ff00")
            self.playerFrame += 1
            if self.playerFrame == 20:
                self.playerFrame = 0
        elif self.velocityX < 0 and hits:
            self.image = pygame.image.load(PLAYER_MOVE_LEFT[self.playerFrame])            
            self.image.set_colorkey("#00ff00")
            self.playerFrame += 1
            if self.playerFrame == 20:
                self.playerFrame = 0       
        else:
            self.image = pygame.image.load(PLAYER_IDLE)
            self.image.set_colorkey("#00ff00")

    def playerSprint(self):
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        self.rect.y -= 1        
        if hits:
            self.sprint = True
    
    def get_keys(self):
        # Reset 
        self.accelerationX, self.accelerationY = 0, 0
        self.accelerationY = PLAYER_GRAVITY
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            self.sprint = True
        if keys[pygame.K_a]:
            self.accelerationX = -PLAYER_ACCELERATION
            if self.sprint == True:
                self.accelerationX = -PLAYER_SPRINT_ACCLELRATION
                self.sprint = False
        if keys[pygame.K_d]:
            self.accelerationX = PLAYER_ACCELERATION
            if self.sprint == True:
                self.accelerationX = PLAYER_SPRINT_ACCLELRATION
                self.sprint = False
        if keys[pygame.K_SPACE]:
            self.jump()
        elif not(keys[pygame.K_SPACE]):
            self.jumping = False
            if self.velocityY < 0:
                self.velocityY /= 1.1
        
        # apply friction
        self.accelerationX += self.velocityX * PLAYER_FRICTION
        # equations of motion
        self.velocityX += self.accelerationX
        self.velocityY += self.accelerationY
        
        if self.velocityX < 0.5 and self.velocityX > -0.5:
            self.velocityX = 0
        
    def collide_with_blocks(self, dir):
        if dir == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.velocityX > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.velocityX < 0:
                    self.x = hits[0].rect.right
                self.velocityX = 0
                self.rect.x = self.x
            if self.rect.left <= 0:
                self.x = 2
                self.velocityX = 0
                self.rect.x = self.x                
        if dir == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.velocityY > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.velocityY < 0:
                    self.y = hits[0].rect.bottom
                self.velocityY = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.velocityX
        self.y += self.velocityY
        self.rect.x = (self.x // 2) * 2
        self.collide_with_blocks("x")
        self.rect.y = (self.y // 2) * 2    
        self.collide_with_blocks("y")
        self.graphics()

class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(ENEMY_0)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.positionX = x * TILESIZE
        self.positionY = y * TILESIZE
        self.rect.x = self.positionX
        self.rect.y = self.positionY
        
    def update(self):
        self.hyp = abs(sqrt((self.game.player.x - self.rect.x)**2 + (self.game.player.y - self.rect.y)**2))
        self.opp = self.rect.y - self.game.player.y
        self.adj = self.rect.x - self.game.player.x
        self.angle = asin(self.opp / self.hyp)
        #self.hyp = 1
        print(self.angle)
        if self.hyp < 10:
            self.rect.x = self.game.player.x
            self.rect.y = self.game.player.y
            self.game.playing = False
        elif self.hyp < (10 * TILESIZE):
            self.rect.x -= cos(acos(self.adj / self.hyp)) * 2
            self.rect.y -= sin(asin(self.opp / self.hyp)) * 2

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, type):
        self.game = game
        self.groups = game.all_sprites, game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        if type == "0":
            self.image = pygame.image.load(BLOCK_0)        
        elif type == "1":
            self.image = pygame.image.load(BLOCK_1)
        elif type == "2":
            self.image = pygame.image.load(BLOCK_2)
        elif type == "3":
            self.image = pygame.image.load(BLOCK_3)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class BackGround(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(BACKGROUND)
        self.rect = self.image.get_rect()
        #self.image.set_colorkey(WHITE)
        self.x = 0
        self.y = 0
        self.rect.x = 0 * TILESIZE
        self.rect.y = 0 * TILESIZE    