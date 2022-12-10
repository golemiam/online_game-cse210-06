from game.casting.actor import Actor


class HealthBar(Actor):
    """A healthbar to be displayed."""
 
    def __init__(self, image, position, debug = False):
        """Constructs a new healthbar.
        
        Args:
            text: An image.
            position: An instance of Point.
        """
        super().__init__(debug)
        self._image = image
        self._position = position
        
    def get_position(self):
        """Gets the healthbar's position.
        
        Returns:
            An instance of Point.
        """
        return self._position
    
    def get_image(self):
        """Gets the healthbar's image.
        
        Returns:
            An instance of Image.
        """
        return self._image   