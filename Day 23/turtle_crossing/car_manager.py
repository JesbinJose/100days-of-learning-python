from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = MOVE_INCREMENT
        self.cars_possibility = 7

    def create_car(self):
        random_choice = random.randint(1,self.cars_possibility)
        if(random_choice != 1):
            return
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.shapesize(1,2)
        turtle.color(random.choice(COLORS))
        turtle.goto(250,float(random.randint(-250,250)))
        self.cars.append(turtle)

    def move_car(self):
        for i in self.cars:
            i.goto(i.xcor()-20,i.ycor())
        
    def speed_up(self):
        self.speed += 10

            
    
