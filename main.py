from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from block import Block

import time

BLOCK_COLORS = ("Green", "Yellow", "Orange", "Red")

# SETUP SCREEN
screen = Screen()
screen.setup(height=600,width=800)
screen.title("Breakout")
screen.bgcolor("Black")
screen.listen()
screen.tracer(0)


# CREATE ON SCREEN ELEMENTS
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()


# CREATE BLOCK ARRAY
blocks = []
i = 0
for y in range(0,200,50):
    for x in range(-350,400,70):
        block = Block(position=(x,y),color=BLOCK_COLORS[i])
        blocks.append(block)
    i += 1

# BIND KEYS
screen.onkey(fun=paddle.left,key="Left")
screen.onkey(fun=paddle.right,key="Right")

#  MAIN LOOP
game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    ball.move()
    
    # Detect Paddle Ball Collisions
    ball.paddle_collision_check(paddle)
    
    # Detect Block Ball Collisions
    collison, block = ball.block_collision_check(blocks)
    if collison:
        blocks.remove(block)
        block.remove()
        scoreboard.add_score()
    
    # Detect if ball out of play
    if ball.ball_out_of_bounds():
        # game_over = True
        scoreboard.lose_life()
        ball.reset_position()
    
    # Check if user out of lives or no more blocks
    if scoreboard.lives == 0 or scoreboard.score == 44:
        for block in blocks:
            block.remove()
        scoreboard.game_over()
        game_over = True
    screen.update()

screen.exitonclick()