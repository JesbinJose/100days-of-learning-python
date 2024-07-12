from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.right(90)
        self.goto(STARTING_POSITION)
        self.right(180)

    def move_fd(self):
        self.goto(0 , self.ycor() + MOVE_DISTANCE)

    def is_at_finsh_line(self) -> bool:
        if(self.ycor() >= 280):
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

