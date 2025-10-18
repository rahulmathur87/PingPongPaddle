from turtle import Screen
from paddle import Paddle
from ball import Ball


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
    screen.update()

screen.exitonclick()
