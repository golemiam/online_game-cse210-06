from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Player(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Bat.
        
        Args:Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_image(self):
        """Gets the bat's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._image

    def get_body(self):
        """Gets the bat's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def move_left(self):
        """Moves the player left."""
        velocity = Point(-PLAYER_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def move_right(self):
        """Moves the player right."""
        velocity = Point(PLAYER_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def move_up(self):
        """Moves the player up."""
        velocity = Point(0, -PLAYER_VELOCITY)
        self._body.set_velocity(velocity)
    
    def move_down(self):
        """Moves the player down."""
        velocity = Point(0, PLAYER_VELOCITY)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the bat from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)