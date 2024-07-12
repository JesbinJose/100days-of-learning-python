import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
score_board = Scoreboard()


screen.listen()
screen.onkeypress(fun=turtle.move_fd,key="w")
screen.onkeypress(fun=turtle.move_fd,key="Up")
car_manager = CarManager()
for i in range(5):
    car_manager.create_car()

game_is_on = True

while game_is_on:
    car_manager.create_car()
    car_manager.move_car()
    time.sleep(0.1)
    for car in car_manager.cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            break
           
    if turtle.is_at_finsh_line():
        score_board.pass_level()
        car_manager.speed_up()
        if car_manager.speed % 10 == 0:
            car_manager.cars_possibility -= 1
    screen.update()

score_board.game_over()

screen.exitonclick()