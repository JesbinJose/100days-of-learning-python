from turtle import Turtle , Screen
from helper_functions import random_color

timmy = Turtle()

timmy.shape("turtle")


def draw_spirograph(no_of_circle):
    for _ in range(no_of_circle):
        timmy.circle(100)
        timmy.right(360/no_of_circle)
        timmy.color(random_color())


timmy.speed(100)
draw_spirograph(120)
screen = Screen()
screen.exitonclick()