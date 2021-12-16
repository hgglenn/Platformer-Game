import os
import pygame

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (78, 121, 237)

# game settings
WIDTH = 640  # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 480  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Platformer Game"
GRID = False


BGCOLOR = LIGHTBLUE

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Icon picture
game_folder = os.path.dirname(__file__)
sprites_folder = os.path.join(game_folder, "sprites")
ICON = pygame.image.load(os.path.join(sprites_folder, "icon.png"))

# Player textures
PLAYER_IDLE = os.path.join(sprites_folder, "Player.png")
PLAYER_IDLE_LEFT = os.path.join(sprites_folder, "Player_l.png")
PLAYER_JUMP_RIGHT = os.path.join(sprites_folder, "Player_jr.png")
PLAYER_JUMP_LEFT = os.path.join(sprites_folder, "Player_jl.png")
PLAYER_MOVE_0_RIGHT = os.path.join(sprites_folder, "Player_r1.png")
PLAYER_MOVE_1_RIGHT = os.path.join(sprites_folder, "Player_r2.png")
PLAYER_MOVE_2_RIGHT = os.path.join(sprites_folder, "Player_r3.png")
PLAYER_MOVE_3_RIGHT = os.path.join(sprites_folder, "Player_r4.png")
PLAYER_MOVE_4_RIGHT = os.path.join(sprites_folder, "Player_r5.png")
PLAYER_MOVE_5_RIGHT = os.path.join(sprites_folder, "Player_r6.png")

PLAYER_MOVE_0_LEFT = os.path.join(sprites_folder, "Player_l1.png")
PLAYER_MOVE_1_LEFT = os.path.join(sprites_folder, "Player_l2.png")
PLAYER_MOVE_2_LEFT = os.path.join(sprites_folder, "Player_l3.png")
PLAYER_MOVE_3_LEFT = os.path.join(sprites_folder, "Player_l4.png")
PLAYER_MOVE_4_LEFT = os.path.join(sprites_folder, "Player_l5.png")
PLAYER_MOVE_5_LEFT = os.path.join(sprites_folder, "Player_l6.png")

PLAYER_MOVE_RIGHT = [PLAYER_MOVE_0_RIGHT, PLAYER_MOVE_0_RIGHT, PLAYER_MOVE_0_RIGHT, PLAYER_MOVE_1_RIGHT, PLAYER_MOVE_1_RIGHT, PLAYER_MOVE_1_RIGHT, PLAYER_MOVE_2_RIGHT, PLAYER_MOVE_2_RIGHT, PLAYER_MOVE_2_RIGHT, PLAYER_MOVE_3_RIGHT, PLAYER_MOVE_3_RIGHT, PLAYER_MOVE_3_RIGHT, PLAYER_IDLE, PLAYER_IDLE, PLAYER_IDLE, PLAYER_MOVE_3_RIGHT, PLAYER_MOVE_3_RIGHT, PLAYER_MOVE_3_RIGHT, PLAYER_MOVE_4_RIGHT, PLAYER_MOVE_4_RIGHT, PLAYER_MOVE_4_RIGHT, PLAYER_MOVE_5_RIGHT, PLAYER_MOVE_5_RIGHT, PLAYER_MOVE_5_RIGHT, PLAYER_IDLE, PLAYER_IDLE, PLAYER_IDLE]

PLAYER_MOVE_LEFT = [PLAYER_MOVE_0_LEFT, PLAYER_MOVE_0_LEFT, PLAYER_MOVE_0_LEFT, PLAYER_MOVE_1_LEFT, PLAYER_MOVE_1_LEFT, PLAYER_MOVE_1_LEFT, PLAYER_MOVE_2_LEFT, PLAYER_MOVE_2_LEFT, PLAYER_MOVE_2_LEFT, PLAYER_MOVE_3_LEFT, PLAYER_MOVE_3_LEFT, PLAYER_MOVE_3_LEFT, PLAYER_IDLE_LEFT, PLAYER_IDLE_LEFT, PLAYER_IDLE_LEFT, PLAYER_MOVE_3_LEFT, PLAYER_MOVE_3_LEFT, PLAYER_MOVE_3_LEFT, PLAYER_MOVE_4_LEFT, PLAYER_MOVE_4_LEFT, PLAYER_MOVE_4_LEFT, PLAYER_MOVE_5_LEFT, PLAYER_MOVE_5_LEFT, PLAYER_MOVE_5_LEFT, PLAYER_IDLE_LEFT, PLAYER_IDLE_LEFT, PLAYER_IDLE_LEFT]

# Mob textures
ENEMY_0 = os.path.join(sprites_folder, "demon.png")

# Mob settings


# Block textures
BLOCK_0 = os.path.join(sprites_folder, "barrier.png")
BLOCK_1 = os.path.join(sprites_folder, "strong_block0.png")
BLOCK_2 = os.path.join(sprites_folder, "weak_block0.png")
BLOCK_3 = os.path.join(sprites_folder, "weak_block1.png")
BACKGROUND = os.path.join(sprites_folder, "background_block0.png")

# Player setting
PLAYER_ACCELERATION = 0.8
PLAYER_SPRINT_ACCLELRATION = 1
PLAYER_GRAVITY = 0.981
PLAYER_FRICTION = -0.15
PLAYER_JUMP = -17