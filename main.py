from turtle import Screen
from paddle import Paddle

# Screen setup
screen = Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

# Importing paddles
left_paddle = Paddle(-385)
right_paddle = Paddle(378)
screen.update()

screen.exitonclick()
