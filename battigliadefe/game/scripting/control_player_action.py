from constants import *
from game.scripting.action import Action


class ControlPlayerAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        players = cast.get_first_actor(PLAYERS_GROUP)
        for players[0] in players:
            player = players[0]
            if self._keyboard_service.is_key_down(P1_LEFT or P2_LEFT or P3_LEFT): 
                player.swing_left()
            if self._keyboard_service.is_key_down(P1_RIGHT or P2_RIGHT or P3_RIGHT): 
                player.swing_right()
            if self._keyboard_service.is_key_down(P1_UP or P2_UP or P3_UP): 
                player.swing_right() 
            if self._keyboard_service.is_key_down(P1_DOWN or P2_DOWN or P3_DOWN): 
                player.swing_right() 
            else: 
                player.stop_moving()
        for players[1] in players:
            player = players[1]
            if self._keyboard_service.is_key_down(P2_LEFT): 
                player.swing_left()
            if self._keyboard_service.is_key_down(P2_RIGHT): 
                player.swing_right()
            if self._keyboard_service.is_key_down(P2_UP): 
                player.swing_right() 
            if self._keyboard_service.is_key_down(P2_DOWN): 
                player.swing_right() 
            else: 
                player.stop_moving()
        for players[2] in players:
            player = players[2]
            if self._keyboard_service.is_key_down(P3_LEFT): 
                player.swing_left()
            if self._keyboard_service.is_key_down(P3_RIGHT): 
                player.swing_right()
            if self._keyboard_service.is_key_down(P3_UP): 
                player.swing_right() 
            if self._keyboard_service.is_key_down(P3_DOWN): 
                player.swing_right() 
            else: 
                player.stop_moving()