# I give thanks to KidsCanCode for making a comprehensive and clear tutorial that I used to complete this game.
# I credit Malik Middleton with the name Musa Hop. He thought of the name, not me.
# game options/settings

TITLE = "Musa Hop"

WIDTH = 480

HEIGHT = 600

FPS = 60

FONT_NAME = 'arial'

HS_FILE = "HS.txt"

SPRITESHEET = "spritesheet_jumper.png"


# Player properties

PLAYER_ACC = 0.5

PLAYER_FRICTION = -0.12

PLAYER_GRAV = 0.8

PLAYER_JUMP = 25

# Game properties

BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0



# Starting platforms

PLATFORM_LIST = [(0, HEIGHT - 60),

                 (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 50),

                 (125, HEIGHT - 350),

                 (350, 200),

                 (175, 100)]



# define colors

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)

LIGHTBLUE = (0, 155, 155)

GREY = (192, 192, 192)

NICECOLOR = (51, 153, 255)

BGCOLOR = NICECOLOR
