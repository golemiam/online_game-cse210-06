from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Player(Actor):
    """The player character."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Player.
        
        Args:Args:
            body: A new instance of Body.
            image: The character's image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_image(self):
        """Gets the bat's animation.
        
        Returns:
            The players image.
        """
        return self._image

    def get_body(self):
        """Gets the players's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the player using their velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Steers the player to the left."""
        velocity = Point(-PLAYER_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def swing_right(self):
        """Steers the player to the right."""
        velocity = Point(PLAYER_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def swing_up(self):
        """Steers the player up."""
        velocity = Point(0, -PLAYER_VELOCITY)
        self._body.set_velocity(velocity)
    
    def swing_down(self):
        """Steers the player down."""
        velocity = Point(0, PLAYER_VELOCITY)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the player from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)