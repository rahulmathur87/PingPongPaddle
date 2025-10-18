from turtle import Screen
from paddle import Paddle
from ball import Ball


# Screen setup
screen = Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

# Importing paddles
left_paddle = Paddle(-385)
right_paddle = Paddle(378)
ball = Ball()
screen.update()

screen.exitonclick()
