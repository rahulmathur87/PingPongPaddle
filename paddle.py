from turtle import Turtle


class Paddle:
    def __init__(self, x_coordinate):
        self.body = Turtle("square")
        self.body.color("white")
        self.body.penup()
        self.body.shapesize(stretch_wid=5, stretch_len=1)
        self.body.teleport(x_coordinate, 0)

    def up(self):
        self.body.goto(self.body.xcor(), self.body.ycor() + 20)

    def down(self):
        self.body.goto(self.body.xcor(), self.body.ycor() - 20)
