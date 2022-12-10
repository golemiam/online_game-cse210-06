from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollidePlayerAction(Action):
    """Determines if the player collides with a ball."""
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        balls = cast.get_actors(BALLS_GROUP)
        player = cast.get_first_actor(PLAYER_GROUP)
        over_sound = Sound(OVER_SOUND)
        for ball in balls:
            ball_body = ball.get_body()
            player_body = player.get_body()

            if self._physics_service.has_collided(ball_body, player_body):
                ball.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)

                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
                
                if stats.get_lives() > 0:
                    callback.on_next(TRY_AGAIN)
                else:
                    callback.on_next(GAME_OVER)
                    self._audio_service.play_sound(over_sound)