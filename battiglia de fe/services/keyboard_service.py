import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.
    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size
        self._p1_dx = 0
        self._p1_dy = 0
        self._p1_sermon_attack = False
        self._p1_chat = False
        self._p2_dx = 0
        self._p2_dy = 0
        self._p2_sermon_attack = False
        self._p2_chat = False

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
        elif pyray.is_key_down(pyray.KEY_1): #Aggresive sermon
            self._p1_sermon_attack
        elif pyray.is_key_down(pyray.KEY_2): #Open chat box
            self._p1_chat


        else:
            pass

        direction = Point(self._p1_dx, self._p1_dy)
        direction = direction.scale(self._cell_size)
        
        return direction
    
    def get_player2_direction(self):
        """Gets the selected direction based on the currently pressed keys.
        Returns:
            Point: The selected direction.
        """
        if pyray.is_key_down(pyray.KEY_J): #Left
            self._p2_dx = -1
            self._p2_dy = 0
        elif pyray.is_key_down(pyray.KEY_K): #Down
            self._p2_dx = 0
            self._p2_dy = 1
        elif pyray.is_key_down(pyray.KEY_L): #Right
            self._p2_dx = 1
            self._p2_dy = 0
        elif pyray.is_key_down(pyray.KEY_I): #Up
            self._p2_dx = 0
            self._p2_dy = -1
        elif pyray.is_key_down(pyray.KEY_0): #Aggresive sermon
            self._p2_sermon_attack
        elif pyray.is_key_down(pyray.KEY_9): #Open chat box
            self._p2_chat
        else:
            pass

        direction = Point(self._p2_dx, self._p2_dy)
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





