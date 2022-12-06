import csv
from constants import *
from game.casting.animation import Animation
#from game.casting.ball import Ball
from game.casting.body import Body
#from game.casting.brick import Brick
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
#from game.casting.racket import Racket
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
#from game.scripting.collide_borders_action import CollideBordersAction
#from game.scripting.collide_brick_action import CollideBrickAction
#from game.scripting.collide_racket_action import CollideRacketAction
#from game.scripting.control_racket_action import ControlRacketAction
#from game.scripting.draw_ball_action import DrawBallAction
#from game.scripting.draw_bricks_action import DrawBricksAction
#from game.scripting.draw_dialog_action import DrawDialogAction
#from game.scripting.draw_hud_action import DrawHudAction
#from game.scripting.draw_racket_action import DrawRacketAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
#from game.scripting.move_ball_action import MoveBallAction
#from game.scripting.move_racket_action import MoveRacketAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


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
    #CONTROL_RACKET_ACTION = ControlRacketAction(KEYBOARD_SERVICE)
    #DRAW_BALL_ACTION = DrawBallAction(VIDEO_SERVICE)
    #DRAW_BRICKS_ACTION = DrawBricksAction(VIDEO_SERVICE)
    #DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    #DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    #DRAW_RACKET_ACTION= DrawRacketAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    #MOVE_BALL_ACTION = MoveBallAction()
    #MOVE_RACKET_ACTION = MoveRacketAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        """"""
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        """"""
        
    def _prepare_next_level(self, cast, script):
        """"""
        
    def _prepare_try_again(self, cast, script):
        """"""

    def _prepare_in_play(self, cast, script):
        """"""

    def _prepare_game_over(self, cast, script):
        """"""

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------

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