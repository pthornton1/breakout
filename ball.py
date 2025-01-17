from turtle import Turtle
import math

SHAPE = 'circle'
SIZE = 1
BALL_COLOUR = "White"
STARTING_Y_DIRECTION = 1
STARTING_X_DIRECTION = 1
SCREEN_HEIGHT_LIMIT = 280
SCREEN_PADDLE_LIMIT = -225
SCREEN_WIDTH_LIMIT = 375
BALL_MOVEMENT = 10
INITIAL_BALL_SPEED = 0.1
STARTING_POSITION = (0,-230)

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(BALL_COLOUR)
        self.penup()
        
        self.move_speed = INITIAL_BALL_SPEED
        self.y_direction = STARTING_Y_DIRECTION
        self.x_direction = STARTING_X_DIRECTION
        self.turtlesize(stretch_len=SIZE, stretch_wid=SIZE)
        self.goto(STARTING_POSITION)
        
    def move(self):
        
        current_x = self.xcor()
        current_y = self.ycor()
        
        # Wall Collision
        if current_y > SCREEN_HEIGHT_LIMIT:
            self.y_direction *= -1
            
        if current_x**2 > SCREEN_WIDTH_LIMIT**2:
            self.x_direction *= -1
            
        new_y = current_y + BALL_MOVEMENT* self.y_direction
        new_x = current_x + BALL_MOVEMENT* self.x_direction
        
        self.goto(x=new_x,y=new_y)
        
        
    def paddle_collision_check(self, paddle):
        if self.ycor() < SCREEN_PADDLE_LIMIT and self.distance(paddle) < 50:
            # avoid double bouncing on the same paddle
            self.y_direction = 1
            self.increase_speed()
        
    def block_collision_check(self, blocks, speed_increase=1):
        for block in blocks: 
            x_distance = math.sqrt((self.xcor()-block.xcor())**2)
            y_distance = math.sqrt((self.ycor()-block.ycor())**2)
            
            # check which direction the collision is in relation to the block
            if 45 < x_distance < 60 and  y_distance < 25:
                self.move_speed *= speed_increase
                self.x_direction *= -1
                return True, block
            if x_distance < 45 and 25 < y_distance < 35:
                self.move_speed *= speed_increase
                self.y_direction *= -1
                return True, block                
                
        return False, None
    
    def increase_speed(self, speed_increase=0.9):
        self.move_speed *= speed_increase
    
    def ball_out_of_bounds(self):
        return self.ycor()< -SCREEN_HEIGHT_LIMIT
        
    
    def who_scored(self):
        if self.xcor() > 1:
            return "left"
        else:
            return "right"
    
    def reset_position(self):
        self.move_speed = INITIAL_BALL_SPEED
        self.goto(STARTING_POSITION)
        self.x_direction *= -1
        self.y_direction = STARTING_X_DIRECTION