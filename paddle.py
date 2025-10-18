from turtle import Turtle

Y_COORDINATES = [-40, -20, 0, 20, 40]


class Paddle:
    def __init__(self, x_coordinate):
        body = []
        for coordinate in Y_COORDINATES:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(x_coordinate, coordinate)
            body.append(segment)
