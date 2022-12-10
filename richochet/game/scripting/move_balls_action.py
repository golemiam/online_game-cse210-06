from constants import *
from game.scripting.action import Action


class MoveBallsAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        balls = cast.get_actors(BALLS_GROUP)
        for ball in balls:
            body = ball.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
