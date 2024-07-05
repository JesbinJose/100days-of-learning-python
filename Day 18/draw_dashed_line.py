from turtle import Turtle , Screen

timmy_the_turtle = Turtle()

def draw_dashed_line(count):
    for _ in range(count):
        timmy_the_turtle.fd(10)
        timmy_the_turtle.pu()
        timmy_the_turtle.fd(10)
        timmy_the_turtle.pd()


timmy_the_turtle.shape("arrow")
timmy_the_turtle.color("black")

draw_dashed_line(15)

screen = Screen()
screen.exitonclick()