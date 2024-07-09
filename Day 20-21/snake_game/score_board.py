from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("courier", 14, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("courier", 40, "normal"))