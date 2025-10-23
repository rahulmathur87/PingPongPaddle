from turtle import Turtle
import random

RANGES = [
    (0, 60),
    (120, 240),
    (300, 360)
]


def get_angle():
    start, end = random.choice(RANGES)
    angle = random.randint(start, end)
    return angle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
