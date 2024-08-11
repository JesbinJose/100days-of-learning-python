from snake import Snake 
from turtle import Screen
from food import Food
from score_board import ScoreBoard

def reset_game():
    snake.reset()
    food.refresh()
    score.reset()
    game_loop()

def game_loop():
    while True:
        screen.update()
        snake.move_froward()

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

    # Wait for player to press "Space" to restart the game
    screen.listen()
    screen.onkey(reset_game, "space")

# Set up the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create game objects
snake = Snake(screen)
food = Food()
score = ScoreBoard()

# Listen for arrow key inputs
screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

# Start the game loop
game_loop()

screen.exitonclick()
