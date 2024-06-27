import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_is_game_done(users_score, dealers_score):
    if users_score > 21:
        print("You went over. You lose!")
        return True
    elif dealers_score > 21:
        print("Dealer went over. You win!")
        return True
    else:
        return False

def play_game():
    user_cards = []
    dealer_cards = []

    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    dealer_first_card = dealer_cards[0]

    while True:
        if(11 in user_cards and sum(user_cards) > 21):
            user_cards.remove(11)
            user_cards.append(1)
        print(f"Your cards are {user_cards} and your score is {sum(user_cards)}")
        print(f"Computer's first card: {dealer_first_card}")
        can_continue = not check_is_game_done(sum(user_cards), sum(dealer_cards))
        if can_continue:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                user_cards.append(random.choice(cards))
                os.system('cls')
            else:
                break
        else:
            return

    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))
        if(11 in dealer_cards and sum(dealer_cards) > 21):
            dealer_cards.remove(11)
            dealer_cards.append(1)
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
    if check_is_game_done(sum(user_cards), sum(dealer_cards)):
        return
    elif sum(dealer_cards) == sum(user_cards):
        print("Draw")
    elif sum(dealer_cards) < sum(user_cards):
        print("You win")
    else:
        print("You lose")

should_continue = True
while should_continue:
    should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y'
    if not should_continue:
        print('Thank you for playing and bye bye')
    else:
        os.system('cls')
        print(logo)
        play_game()
