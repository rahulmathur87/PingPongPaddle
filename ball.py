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
        self.setheading(get_angle())
        # self.setheading(300)

    def move(self):
        self.forward(15)
