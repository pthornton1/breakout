from turtle import Turtle

SHAPE = 'circle'
SIZE = 1
BALL_COLOUR = "White"
STARTING_Y_DIRECTION = 1
STARTING_X_DIRECTION = 1
SCREEN_HEIGHT_LIMIT = 280
SCREEN_PADDLE_LIMIT = 320
SCREEN_WIDTH_LIMIT = 380
BALL_MOVEMENT = 10
INITIAL_BALL_SPEED = 0.1

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
        
    def move(self):
        
        current_x = self.xcor()
        current_y = self.ycor()
        
        # Wall Collision
        if current_y**2 > SCREEN_HEIGHT_LIMIT**2:
            self.y_direction *= -1
            
        new_y = current_y + BALL_MOVEMENT* self.y_direction
        new_x = current_x + BALL_MOVEMENT* self.x_direction
        
        self.goto(x=new_x,y=new_y)
        
        
    def paddle_collision_check(self, paddle):
        if self.xcor()**2 > SCREEN_PADDLE_LIMIT**2 and self.distance(paddle) < 50:
            # avoid double bouncing on the same paddle
            if paddle.xcor() > 0:
                self.x_direction = -1
                self.increase_speed()
            
            if paddle.xcor() < 0:
                self.x_direction = 1
                self.increase_speed()
        
    def increase_speed(self, speed_increase=0.9):
        self.move_speed *= speed_increase
    
    def ball_out_of_bounds(self):
        return self.xcor()**2 > SCREEN_WIDTH_LIMIT**2
    
    def who_scored(self):
        if self.xcor() > 1:
            return "left"
        else:
            return "right"
    
    def reset_position(self):
        self.move_speed = INITIAL_BALL_SPEED
        self.goto(0,0)
        self.x_direction *= -1
        self.y_direction = STARTING_X_DIRECTION