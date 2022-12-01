from game.shared.point import Point
from game.casting.actor import Actor
from game.shared.color import Color
import random
import pyray

CELL_SIZE = 15
FONT_SIZE = 30
COLS = 60
ROWS = 40
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
BLUE = Color(0, 0, 255)

class Director():
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """
    def __init__(self, keyboard_service, video_service, player1_score, player2_score):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.game_state = True
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
            if (self.player1_score and self.player2_score) == 10:
                print("Draw!")
                restart = input("Play Again? yes/no\n")
                if restart.lower() == 'yes':
                    self.player1_score = 0
                    self.player2_score = 0
                    self.start_game(cast)
                else:
                    print("Thanks for playing!")
                    self._video_service.close_window()
            elif self.player1_score == 10:
                #self._handle_game_over("player_one", cast)
                print("Player 1 wins!")
                restart = input("Play Again? yes/no\n")
                if restart.lower() == 'yes':
                    self.player1_score = 0
                    self.player2_score = 0
                    self.start_game(cast)
                else:
                    print("Thanks for playing!")
                    self._video_service.close_window()
            elif self.player2_score == 10:
                #self._handle_game_over("player_two", cast)
                print("Player 2 wins!")
                restart = input("Play Again? yes/no\n")
                if restart.lower() == 'yes':
                    self.player1_score = 0
                    self.player2_score = 0
                    self.start_game(cast)
                else:
                    print("Thanks for playing!")
                    self._video_service.close_window()
        self._video_service.close_window()

    def _get_inputs(self, cast):
        player1 = cast.get_first_actor("player1")
        p1_velocity = self._keyboard_service.get_player1_direction()
        player1.set_velocity(p1_velocity)

        player2 = cast.get_first_actor("player2")
        p2_velocity = self._keyboard_service.get_player2_direction()
        player2.set_velocity(p2_velocity)
    
    def _do_updates(self, cast):
        """Updates the position's position and resolves any collisions with players/their trails.
        Args:
            cast (Cast): The cast of actors.
        """
        # Retrieve actor data
        p1_banner = cast.get_first_actor("p1_banner")
        p2_banner = cast.get_first_actor("p2_banner")
        player1 = cast.get_first_actor("player1")
        p1_position = player1.get_position()
        player2 = cast.get_first_actor("player2")
        p2_position = player2.get_position()

        # Create barriers
        p1_barrier = Actor()
        p1_barrier.set_text("#")
        p1_barrier.set_font_size(FONT_SIZE)
        p1_barrier.set_color(RED)
        p1_barrier.set_position(p1_position)
        cast.add_actor("p1_barriers", p1_barrier)

        p2_barrier = Actor()
        p2_barrier.set_text("#")
        p2_barrier.set_font_size(FONT_SIZE)
        p2_barrier.set_color(BLUE)
        p2_barrier.set_position(p2_position)
        cast.add_actor("p2_barriers", p2_barrier)

        # Update player scores and positions
        p1_banner.set_text(f"P1 Score: {self.player1_score}")
        p2_banner.set_text(f"P2 Score: {self.player2_score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player1.move_next(max_x, max_y)
        player2.move_next(max_x, max_y)

       #Handling Collilions
       """
       ##Header Collisions
        if(player1.get_position().equals(player2.get_position())):
            player1.set_color(WHITE)
            player2.set_color(WHITE)
            self.player1_score += 1
            self.player2_score += 1
            player1.reset_segments()
            cast.reset_actors("p1_barriers")
            player2.reset_segments()
            cast.reset_actors("p2_barriers")
            player1.set_color(RED)
            player2.set_color(BLUE)
       
        ##Cutting Segments 
        if(player1.check_segment_collision(player2)):
            player1.set_color(WHITE)
            self.player1_score += 1
            player1.reset_segments()
            cast.reset_actors("p1_barriers")
            player2.reset_segments()
            cast.reset_actors("p2_barriers")
            player1.set_color(RED)
          
        if(player2.check_segment_collision(player1)):
            self.player2_score += 1
            player2.set_color(WHITE)
            player1.reset_segments()
            cast.reset_actors("p1_barriers")
            player2.reset_segments()
            cast.reset_actors("p2_barriers")
            player2.set_color(BLUE)

       """      
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
    
#    def _handle_game_over(self, collitionSituation, cast):
#        if(self.game_state==True):
#            self.game_state = False
#            x = int(900/2)
#            y = int(600/2)
#            position = Point(x-100,y)
#            secondary_position = Point(x-350,y+100)
#            
#            message = Actor()
#            secondary_message = Actor()
#            secondary_message.set_text("Press Enter to Keep Playing!!!\nPress P Play Again!!!")
#            
#            if(collitionSituation=="truce"):
#                message.set_text("Game Over!!!")
#            elif(collitionSituation=="player_one"):
#                message.set_text("Player One Won!!!")
#            else:
#                message.set_text("Player Two Won!!!")
#                
#            message.set_position(position)
#            secondary_message.set_position(secondary_position)
#            
#            cast.add_actor("messages", message)
#            cast.add_actor("messages", secondary_message)
#            
#            self._keyboard_service.get_end_game(self.game_state)
