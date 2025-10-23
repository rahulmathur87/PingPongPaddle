from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.player1score = 0
        self.player2score = 0
        self.goto(-280, 280)
        self.write(f"Player1: {self.player1score}", font=('Arial', 10, 'normal'))
        self.goto(230, 280)
        self.write(f"Player2: {self.player2score}", font=('Arial', 10, 'normal'))
