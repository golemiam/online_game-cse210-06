from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        self._draw_label(cast, P1_LIVES_GROUP, P1_IMAGE, stats.get_lives())
        self._draw_label(cast, P2_LIVES_GROUP, P2_IMAGE, stats.get_lives())
        self._draw_label(cast, P3_LIVES_GROUP, P3_IMAGE, stats.get_lives())

    def execute(self, cast, script, callback):
        players = cast.get_actors(PLAYERS_GROUP)
        for player in players:
            body = player.get_body()
            image = player.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)

    def _draw_label(self, cast, group, image_str, data):
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(format_str.format(data))
        position = label.get_position()
        self._video_service.draw_text(text, position)