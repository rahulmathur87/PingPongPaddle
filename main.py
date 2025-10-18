from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Variables
bounce_angle = 60


# Screen setup
screen = Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

# Importing paddles and ball
left_paddle = Paddle(-385)
right_paddle = Paddle(378)
ball = Ball()
screen.update()

# Paddle movement control
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

screen.listen()

# Game loop
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    if ball.ycor() >= 280:
        if ball.xcor() < 0:
            ball.left(bounce_angle)
        else:
            ball.right(bounce_angle)
    elif ball.ycor() <= -280:
        if ball.xcor() > 0:
            ball.left(bounce_angle)
        else:
            ball.right(bounce_angle)
    ball.move()

screen.exitonclick()
