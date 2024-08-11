from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGH_SCORE_FILE = "Day 24\snake_game_updated\.high_score.txt"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def load_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self, high_score):
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(high_score))
