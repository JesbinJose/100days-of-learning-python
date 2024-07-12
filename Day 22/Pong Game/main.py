from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800,600)
screen.tracer(0)
# Paddles for left and right player
left_paddle = Paddle((-345,0))
right_paddle = Paddle((345,0))
screen.tracer(1)
screen.listen()
screen.onkey(key="Up",fun=right_paddle.go_up)
screen.onkey(key="Down",fun=right_paddle.go_down)
screen.onkey(key="w",fun=left_paddle.go_up)
screen.onkey(key="s",fun=left_paddle.go_down)

# ball
ball = Ball()

score_board =ScoreBoard()


game_is_on = True

while game_is_on:
    # Left paddle collision control
    if ball.xcor() < -320 and ball.xcor() > -350 and ball.distance(left_paddle.pos()) < 50 and ball.x_move < 0:
        ball.bounce_x()
    # Right paddle collision control
    if ball.xcor() > 320 and ball.xcor() < 350 and ball.distance(right_paddle.pos()) < 50 and ball.x_move > 0:
        ball.bounce_x()

    if ball.xcor() > 380 or ball.xcor() < -380:
        print("hello")
        screen.tracer(0)
        if ball.xcor() < 0:
            score_board.increase_left_score()
        else:
            score_board.increase_right_score()
        ball.reset_position()
        screen.tracer(1)
    
    ball.move()






screen.exitonclick()