from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 270)
        self.write(f"{self.right_score}",align="center",font=("courier", 20, "bold"))
        self.goto(-100, 270)
        self.write(f"{self.left_score}",align="center",font=("courier", 20, "bold"))

    def increase_left_score(self):
        self.left_score += 1
        self.update_score()

    def increase_right_score(self):
        self.right_score += 1
        self.update_score()