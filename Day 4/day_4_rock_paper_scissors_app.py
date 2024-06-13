import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Welcome to Rock, Paper, Scissors")
while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    moves = [rock, paper, scissors]
    print(moves[user_choice])


    random_number = random.randint(0, 2)
    computer_choice = random_number
    print("Computer chose:")
    print(moves[computer_choice])

    if((user_choice==0 and computer_choice==2)or
    (user_choice==1 and computer_choice==0)or
    (user_choice==2 and computer_choice==1)):
        print("You win")
    elif(user_choice==computer_choice):
        print("Draw")
    else:
        print("You lose")

    play_again = input("Do you want to play again? Type 'y' or 'n'.\n")
    if play_again == 'n':
        break