from turtle import Turtle

Y_COORDINATES = [-40, -20, 0, 20, 40]


class Paddle:
    def __init__(self, x_coordinate):
        self.body = []
        for coordinate in Y_COORDINATES:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.teleport(x_coordinate, coordinate)
            self.body.append(segment)

    def up(self):
        for segment in self.body:
            segment.goto(segment.xcor(), segment.ycor() + 20)

    def down(self):
        for segment in self.body:
            segment.goto(segment.xcor(), segment.ycor() - 20)
