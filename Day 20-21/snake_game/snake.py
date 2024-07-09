from turtle import Turtle , Screen
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    snake = []
    def __init__(self,screen:Screen):
        self.screen = screen
        for i in range(3):
            self.add_length(False) 
            self.snake[i].goto(-20*i,0)
        self.head = self.snake[0]

    def add_length(self,isEat:bool):
        new_snake = Turtle()
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.penup()
        if isEat:
            new_snake.goto(self.getTail().pos())
        self.snake.append(new_snake)

    def did_collide_with_tail(self):
        for i in self.snake[1:]:
            if i.distance(self.head) < 10:
                return True
        return False

    def getTail(self):
        return self.snake[-1]

    def move_froward(self):
        self.screen.update()
        time.sleep(0.1)
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].goto(self.snake[i-1].pos())
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    
