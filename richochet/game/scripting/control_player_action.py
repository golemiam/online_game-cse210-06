from constants import *
from game.scripting.action import Action


class ControlPlayerAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            player.move_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            player.move_right()
        if self._keyboard_service.is_key_down(UP):
            player.move_up()
        elif self._keyboard_service.is_key_down(DOWN):
            player.move_down() 
        else: 
            player.stop_moving()

        if self._keyboard_service.is_key_down(SPACE):
            player.dash()