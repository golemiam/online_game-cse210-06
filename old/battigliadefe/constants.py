import pathlib
import pyray
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Battiglia Di Fe"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "battigliadefe/assets/fonts/logbook-prime-v2_0.ttf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "battigliadefe/assets/sounds/boing.wav"
WELCOME_SOUND = "battigliadefe/assets/sounds/start.wav"
OVER_SOUND = "battigliadefe/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
PAUSE = "escape" or "p"

P1_LEFT = "a"
P1_RIGHT = "d"
P1_UP = "w"
P1_DOWN = "s"
P1_SPRINT = "left shift"
P1_PREACH = "space"

P2_LEFT = "k"
P2_RIGHT = "semicolon"
P2_UP = "o"
P2_DOWN = "l"
P2_SPRINT = "right shift"
P2_PREACH = "alt"

P3_LEFT = "numpad 4"
P3_RIGHT = "numpad 6"
P3_UP = "numpad 8"
P3_DOWN = "numpad 5"
P3_SPRINT = "numpad 0"
P3_PREACH = "left"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 5
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
SCORE_FORMAT = "SCORE: {}"

# HEALTH BARS
P1_LIVES_GROUP = "p1_lives"
P1_H0 = "battigliadefe/assets/images/200.png"
P1_H1 = "battigliadefe/assets/images/201.png"
P1_H2 = "battigliadefe/assets/images/202.png"
P1_H3 = "battigliadefe/assets/images/203.png"
P1_H4 = "battigliadefe/assets/images/204.png"
P1_HEALTH_STATES = [P1_H0, P1_H1, P1_H2, P1_H3, P1_H4]

P2_LIVES_GROUP = "p2_lives"
P2_H0 = "battigliadefe/assets/images/210.png"
P2_H1 = "battigliadefe/assets/images/211.png"
P2_H2 = "battigliadefe/assets/images/212.png"
P2_H3 = "battigliadefe/assets/images/213.png"
P2_H4 = "battigliadefe/assets/images/214.png"
P2_HEALTH_STATES = [P2_H0, P2_H1, P2_H2, P2_H3, P2_H4]

P3_LIVES_GROUP = "p3_lives"
P3_H0 = "battigliadefe/assets/images/220.png"
P3_H1 = "battigliadefe/assets/images/221.png"
P3_H2 = "battigliadefe/assets/images/222.png"
P3_H3 = "battigliadefe/assets/images/223.png"
P3_H4 = "battigliadefe/assets/images/224.png"
P3_HEALTH_STATES = [P3_H0, P3_H1, P3_H2, P3_H3, P3_H4]

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO PREACH!"
WAS_GOOD_GAME = "GAME OVER"

# PLAYER CHARACTERS
PLAYERS_GROUP = "players"
PLAYER_HEIGHT = 28
PLAYER_WIDTH = 28
PLAYER_VELOCITY = 7
## PLAYER 1 INFORMATION
P1_IMAGE = "assets/images/000.png"
P1_X = int(SCREEN_WIDTH / 4)
P1_Y = CENTER_Y
## PLAYER 2 INFORMATION
P2_IMAGE = "assets/images/001.png"
P2_X = CENTER_X
P2_Y = CENTER_Y
## PLAYER 3 INFORMATION
P3_IMAGE = "assets/images/002.png"
P3_X = int(CENTER_X*1.5)
P3_Y = CENTER_Y

# WORLD OBSTACLES
