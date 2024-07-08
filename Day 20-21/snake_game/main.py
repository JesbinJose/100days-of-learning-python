from snake import Snake 
from turtle import Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake(screen)
screen.listen()
screen.onkey(key="Up",fun=snake.turn_up)
screen.onkey(key="Down",fun=snake.turn_down)
screen.onkey(key="Left",fun=snake.turn_left)
screen.onkey(key="Right",fun=snake.turn_right)
while True:
    snake.move_froward()

screen.exitonclick()









