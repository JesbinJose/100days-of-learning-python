import random
import os
from art import logo 
def play_game():
    os.system('cls')
    print(logo)
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 1000)
    print("I'm thinking of a number between 1 and 1000")
    users_level  = input("Choose a difficulty. Type 'easy' or 'hard' :")
    if users_level == "easy":
        lives = 20
    else :
        lives = 10
    while lives > 0 :
        print(f"You have {lives} attemtps remaining to guess the number")
        guess = int(input("Make a guess: "))
        if number == guess:
            print(f"You got it! The number is {number}")
            break
        elif number > guess:
            print("Too low")
        else:
            print("Too high")

        lives -= 1
        if lives == 0:
            print("You've run out of lives. You lose.")
            print(f"The number was {number}")


while input("Do you want to play the game 'y' for yes and 'n' for no :") == 'y':
    play_game()
