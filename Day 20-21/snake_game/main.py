from snake import Snake 
from turtle import Screen
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake(screen)
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up",fun=snake.turn_up)
screen.onkey(key="Down",fun=snake.turn_down)
screen.onkey(key="Left",fun=snake.turn_left)
screen.onkey(key="Right",fun=snake.turn_right)
while True:

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.add_length(True)


    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        break

    # Detect collision with tail
    if snake.did_collide_with_tail():
        score.game_over()
        break

    snake.move_froward()

screen.exitonclick()









