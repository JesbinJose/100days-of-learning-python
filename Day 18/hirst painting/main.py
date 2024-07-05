from get_colors import rgb_colors
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()


screen.colormode(255)
timmy.speed(100)
timmy.hideturtle()

def draw_painting():
    for _ in range(10):
        for _ in range(10):
            timmy.color(random.choice(rgb_colors))
            timmy.dot(20)
            timmy.fd(50)
        timmy.setheading(90)
        timmy.fd(50)
        timmy.setheading(180)
        timmy.fd(500)
        timmy.setheading(0)

screen.screensize(300, 300)
timmy.penup()
timmy.goto(-200, -200)
draw_painting()
screen.mainloop()
screen.exitonclick()