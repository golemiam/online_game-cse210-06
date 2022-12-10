from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBallsAction:
    """Determines if two balls collide with eachother."""
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
    
    def execute(self, cast, script, callback):
        bounce_sound = Sound(BOUNCE_SOUND)

        balls = cast.get_actors(BALLS_GROUP)
        beater = balls[0]
        beater_body = beater.get_body()
        bludgeoner = balls[1]
        bludgeoner_body = bludgeoner.get_body()
        thrasher = balls[2]
        thrasher_body = thrasher.get_body()
        self.calc_ball_collision(beater, beater_body, bludgeoner, bludgeoner_body, bounce_sound)
        self.calc_ball_collision(bludgeoner, bludgeoner_body, thrasher, thrasher_body, bounce_sound)
        self.calc_ball_collision(thrasher, thrasher_body, beater, beater_body, bounce_sound)
        
    def calc_ball_collision(self, entity1, body1, entity2, body2, sound):
        """Runs two bodies through some collison checks."""

        if self._physics_service.is_above(body1, body2):
            entity1.bounce_y
            entity2.bounce_y
            self._audio_service.play_sound(sound)
        elif self._physics_service.is_below(body1, body2):
            entity1.bounce_y
            entity2.bounce_y
            self._audio_service.play_sound(sound)
        if self._physics_service.is_left_of(body1, body2):
            entity1.bounce_x
            entity2.bounce_x
            self._audio_service.play_sound(sound)
        elif self._physics_service.is_right_of(body1, body2):
            entity1.bounce_x
            entity2.bounce_x
            self._audio_service.play_sound(sound)