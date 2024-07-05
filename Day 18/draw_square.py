import turtle as t

timmy_the_turtle = t.Turtle()

def draw_square():
    for _ in range(4):
        timmy_the_turtle.fd(100)
        timmy_the_turtle.right(90)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

draw_square()

screen = t.Screen()
screen.exitonclick()