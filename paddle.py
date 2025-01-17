from turtle import Turtle
STARTING_POSITION = {
    "right":(350, 0),
    "left":(-350, 0)
}
PADDLE_COLOUR = "White"
PADDLE_SIZE = 5
PADDLE_SHAPE = "square"

class Paddle(Turtle):
    
    def __init__(self, paddle_side="right"):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.turtlesize(stretch_len=PADDLE_SIZE)
        self.penup()
        self.color(PADDLE_COLOUR)
        self.left(90)
        self.goto(STARTING_POSITION[paddle_side])
        
    def up(self):
        self.forward(20)
        
    def down(self):
        self.backward(20)