from turtle import Turtle

STARTING_POSITION = (0,-250)
PADDLE_COLOUR = "White"
PADDLE_SIZE = 5
PADDLE_SHAPE = "square"

class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.turtlesize(stretch_len=PADDLE_SIZE)
        self.penup()
        self.color(PADDLE_COLOUR)
        self.goto(STARTING_POSITION)
        
    def right(self):
        self.forward(20)
        
    def left(self):
        self.backward(20)