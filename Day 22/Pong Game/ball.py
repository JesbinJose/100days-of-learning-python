from turtle import Turtle
import random
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_position()
        self.move_speed = 0.05

    def move(self):
        time.sleep(self.move_speed)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.did_collide()

    def did_collide(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed += .001

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed += .001

    def reset_position(self):
        self.x_move = random.randint(-15,15)
        self.y_move = abs(self.x_move) - 20
        if self.x_move == 0 or self.y_move == 0:
            self.y_move = random.randint(-15,15)
            self.x_move = abs(self.y_move) - 20
        self.move_speed = 0.05
        time.sleep(1)
        self.goto(0,0)

        