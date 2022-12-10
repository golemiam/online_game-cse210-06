import pyray
from game.casting.point import Point
from game.services.keyboard_service import KeyboardService


class RaylibKeyboardService(KeyboardService):
    """A Raylib implementation of KeyboardService."""

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid. (If omitted, cell_size is 1)
        """
        self._cell_size = cell_size
        self._p1_dx = 0
        self._p1_dy = 0
        self._p2_dx = 0
        self._p2_dy = 0
        self._p3_dx = 0
        self._p3_dy = 0

    def get_player1_direction(self):
        """Gets the selected direction based on the currently pressed keys.
        Returns:
            Point: The selected direction.
        """
        if pyray.is_key_down(pyray.KEY_A): #Left
            self._p1_dx = -1
            self._p1_dy = 0
        elif pyray.is_key_down(pyray.KEY_S): #Down
            self._p1_dx = 0
            self._p1_dy = 1
        elif pyray.is_key_down(pyray.KEY_D): #Right
            self._p1_dx = 1
            self._p1_dy = 0
        elif pyray.is_key_down(pyray.KEY_W): #Up
            self._p1_dx = 0
            self._p1_dy = -1
        if pyray.is_key_down(pyray.KEY_LEFT_SHIFT): #Sprint
            pass

        direction = Point(self._p1_dx, self._p1_dy)
        direction = direction.scale(self._cell_size)
        
        return direction
    
    def get_player2_direction(self):
        """Gets the selected direction based on the currently pressed keys.
        Returns:
            Point: The selected direction.
        """
        if pyray.is_key_down(pyray.KEY_K): #Left
            self._p2_dx = -1
            self._p2_dy = 0
        if pyray.is_key_down(pyray.KEY_L): #Down
            self._p2_dx = 0
            self._p2_dy = 1
        if pyray.is_key_down(pyray.KEY_SEMICOLON): #Right
            self._p2_dx = 1
            self._p2_dy = 0
        if pyray.is_key_down(pyray.KEY_O): #Up
            self._p2_dx = 0
            self._p2_dy = -1
        if pyray.is_key_down(pyray.KEY_LEFT_SHIFT): #Sprint
            pass

        direction = Point(self._p2_dx, self._p2_dy)
        direction = direction.scale(self._cell_size)
        
        return direction
    
    def get_player3_direction(self):
        """Gets the selected direction based on the currently pressed keys.
        Returns:
            Point: The selected direction.
        """
        if pyray.is_key_down(pyray.KEY_LEFT): #Left
            self._p3_dx = -1
            self._p3_dy = 0
        elif pyray.is_key_down(pyray.KEY_DOWN): #Down
            self._p3_dx = 0
            self._p3_dy = 1
        elif pyray.is_key_down(pyray.KEY_RIGHT): #Right
            self._p3_dx = 1
            self._p3_dy = 0
        elif pyray.is_key_down(pyray.KEY_UP): #Up
            self._p3_dx = 0
            self._p3_dy = -1
        if pyray.is_key_down(pyray.KEY_NUM_0): #Sprint
            pass

        direction = Point(self._p3_dx, self._p3_dy)
        direction = direction.scale(self._cell_size)
        
        return direction
    
    def get_entity_direction(self):
        """Sets the entities direction to fall.
        Returns:
            Point: The direction.
        """
        dx = 0
        dy = 1

        direction = Point(dx, dy)
        return direction
    
    def get_end_game(self, status):
        if (status == False):
            if(pyray.is_key_down(pyray.KEY_L)):
                print("pressed")
    
    def is_key_down(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_down(raylib_key)
    
    def is_key_pressed(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_pressed(raylib_key)
    
    def is_key_released(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_released(raylib_key)
    
    def is_key_up(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_up(raylib_key)
    
    def get_end_game(self, status):
        if (status == False):
            if(pyray.is_key_down(pyray.KEY_L)):
                print("pressed")