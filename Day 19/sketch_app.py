from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.fd(10)

def move_backward():
    tim.bk(10)

def rotate_right():
    tim.right(10)

def rotate_left():
    tim.left(10)

def clear():
    tim.reset()

screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=rotate_left)
screen.onkey(key="d",fun=rotate_right)
screen.onkey(key="c",fun=clear)
screen.listen()













screen.exitonclick()