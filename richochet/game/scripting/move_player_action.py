from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MovePlayerAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        body = player.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
        x = position.get_x()
        y = position.get_y()
        if x < 0:
            position = Point(0, y)
        elif x > (SCREEN_WIDTH - PLAYER_WIDTH):
            position = Point(SCREEN_WIDTH - PLAYER_WIDTH, y)
            
        body.set_position(position)