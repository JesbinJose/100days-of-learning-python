from turtle import Turtle , Screen
from helper_functions import random_color
import random

timmy = Turtle()
directions = [0,90,180,270]

def walk():
    rad_direction = random.choice(directions)
    timmy.right(rad_direction)
    timmy.forward(30)


timmy.width(10)
timmy.speed(1000)

while True:
    timmy.color(random_color())
    walk()


screen = Screen()
screen.exitonclick()