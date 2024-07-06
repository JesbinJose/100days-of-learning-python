from turtle import Turtle,Screen 
import random

screen = Screen()
tims = []

user_bet = screen.textinput(prompt="What turtle will win the race? Enter a color: ",title="Turtle race Make your bet",)
screen.setup(width=500,height=400)
colors = ["red","orange","yellow","green","blue"]

y = -100

for i in colors:
    new_tim= Turtle(shape="turtle")
    new_tim.color(i)
    new_tim.penup()
    new_tim.goto(-230,y)
    new_tim.speed(100)
    tims.append(new_tim)
    y += 30
winner_tim = None


while winner_tim == None:
    for tim in tims:
        if tim.xcor() > 230:
            winner_tim = tim
            break
        else:
            tim.forward(random.randint(0,10))


color_won = tim.color()[0]

if user_bet == color_won:
    print(f"You win, {user_bet} won the race!")
else:
    print(f"You Lose, {tim.color()[0]} won the race!")


screen.exitonclick()