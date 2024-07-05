from turtle import Turtle , Screen
from helper_functions import random_color

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")





def draw_polygon(n):
    for _ in range(n):
        timmy_the_turtle.fd(100)
        timmy_the_turtle.left(360/n)


for n in range(3,11):
    draw_polygon(n)
    timmy_the_turtle.color(random_color())


screen = Screen()
screen.exitonclick()