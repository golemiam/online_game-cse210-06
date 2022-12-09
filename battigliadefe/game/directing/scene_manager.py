import csv
from constants import *
from game.casting.animation import Animation
from game.casting.body import Body
from game.casting.image import Image
from game.casting.healthbar import HealthBar
from game.casting.label import Label
from game.casting.point import Point
from game.casting.player import Player
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.control_player_action import ControlPlayerAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_player_action import DrawPlayerAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_player_action import MovePlayerAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService
PLAYER_COUNT = 2

class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    #COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    #COLLIDE_BRICKS_ACTION = CollideBrickAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    #COLLIDE_RACKET_ACTION = CollideRacketAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_PLAYER_ACTION = ControlPlayerAction(KEYBOARD_SERVICE)
    #DRAW_BALL_ACTION = DrawBallAction(VIDEO_SERVICE)
    #DRAW_BRICKS_ACTION = DrawBricksAction(VIDEO_SERVICE)
    #DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_PLAYER_ACTION= DrawPlayerAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    #MOVE_BALL_ACTION = MoveBallAction()
    MOVE_PLAYER_ACTION = MovePlayerAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            PLAYER_COUNT = input("How many players are there? (2 or 3) ")
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)

    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_lives(cast)
        self._add_players(cast)
        #self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_try_again(self, cast, script):
        self._add_players(cast)
        #self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        #script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        #self._activate_ball(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_PLAYER_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_ball(cast)
        self._add_player(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _add_lives(self, cast):
        cast.clear_actors(P1_LIVES_GROUP)
        image = Image(P1_H0)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        healthbar = HealthBar(image, position)
        cast.add_actor(P1_LIVES_GROUP, healthbar)
        
        cast.clear_actors(P2_LIVES_GROUP)
        image = Image(P2_H0)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        healthbar = HealthBar(image, position)
        cast.add_actor(P2_LIVES_GROUP, healthbar)

        cast.clear_actors(P3_LIVES_GROUP)
        image = Image(P3_H0)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        healthbar = HealthBar(image, position)
        cast.add_actor(P3_LIVES_GROUP, healthbar)

    def _add_players(self, cast):
        cast.clear_actors(PLAYERS_GROUP)
        x = P1_X - PLAYER_WIDTH / 2
        y = P1_Y - PLAYER_HEIGHT
        position = Point(x, y)
        size = Point(PLAYER_WIDTH, PLAYER_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(P1_IMAGE)
        player = Player(body, image)
        cast.add_actor(PLAYERS_GROUP, player)

        x = P2_X - PLAYER_WIDTH / 2
        y = P2_Y - PLAYER_HEIGHT
        position = Point(x, y)
        size = Point(PLAYER_WIDTH, PLAYER_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(P2_IMAGE)
        player = Player(body, image)
        cast.add_actor(PLAYERS_GROUP, player)

        if PLAYER_COUNT == 3:
            x = P3_X - PLAYER_WIDTH / 2
            y = P3_Y - PLAYER_HEIGHT
            position = Point(x, y)
            size = Point(PLAYER_WIDTH, PLAYER_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(P3_IMAGE)
            player = Player(body, image)
            cast.add_actor(PLAYERS_GROUP, player)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        #Enter Output Actions Here v
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        # Add Update Script Actions Here v
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)