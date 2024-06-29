import art
import random
import os

from game_data import data
def play_game():
    score = 0
    second_index = random.randint(0,len(data)-1)
    while True:
        print(art.logo)
        if not score  == 0:
            print(f"You're right! Current score: {score}")

        first_index = second_index
        second_index = random.randint(0,len(data)-1)

        while first_index == second_index:
            second_index = random.randint(0,len(data)-1)

        first_person = data[first_index]
        second_person = data[second_index]

        print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")
        print(art.vs)
        print(f"Compare B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")

        does_a_have_more_followers = first_person['follower_count'] > second_person['follower_count']

        users_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if not (users_choice == 'A' or users_choice == 'B'):
            print("Wrong input. Please type 'A' or 'B' this level canceled")
            if not (input("Are you in the game do you want to continue 'yes' or 'no:") == 'yes'):
                os.system('cls')
                print(art.logo)
                print("Thank you for playing and bye bye")
                exit()
        os.system('cls')
        if does_a_have_more_followers :
            
            if users_choice == 'A':
                score += 1
            else:
                break
        else:
            if users_choice == 'B':
                score += 1
            else:
                break
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")

while input("Do you want to play the game 'yes' or 'no' :") == 'yes':
    play_game()