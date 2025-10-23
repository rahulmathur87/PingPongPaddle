from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.teleport(x_coordinate, 0)

    def up(self):
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -260:
            self.goto(self.xcor(), self.ycor() - 20)
