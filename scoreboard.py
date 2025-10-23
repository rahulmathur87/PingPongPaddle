from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.player1score = 0
        self.player2score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 275)
        self.write(f"Player1: {self.player1score}", font=('Arial', 16, 'normal'))
        self.goto(230, 275)
        self.write(f"Player2: {self.player2score}", font=('Arial', 16, 'normal'))

    def player1_point(self):
        self.player1score += 1

    def player2_point(self):
        self.player2score += 1
