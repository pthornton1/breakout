from turtle import Screen
from paddle import Paddle
from ball import Ball
from day_87.scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(height=600,width=800)
screen.title("Pong")
screen.bgcolor("Black")
screen.listen()
screen.tracer(0)

l_paddle = Paddle("left")
r_paddle = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(fun=r_paddle.up,key="Up")
screen.onkey(fun=r_paddle.down,key="Down")
screen.onkey(fun=l_paddle.up,key="w")
screen.onkey(fun=l_paddle.down,key="s")

game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    ball.move()
    
    # Detect Paddle Ball Collisions
    ball.paddle_collision_check(l_paddle)
    ball.paddle_collision_check(r_paddle)
    
    # Detect if ball out of play
    if ball.ball_out_of_bounds():
        # game_over = True
        scoreboard.score(ball.who_scored())
        ball.reset_position()
    
    screen.update()

screen.exitonclick()