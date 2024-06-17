import random

import assets


word = random.choice(assets.word_list)

print("Welcome to Hangman!")

print(assets.logo)

print("You have 6 chances to guess the word.")

current_word = "_" * len(word)

print(current_word)

wrong_count = 6

while True:

    guess = input("Guess a letter: ").lower()[0]
    if guess in word:
        if guess in current_word:
            print(f"You've already guessed {guess}")
            continue
        for index, char in enumerate(word):
            if char == guess:
                current_word = current_word[:index] + char + current_word[index+1:]
    else:
        print(f"{guess} is not in the word and you lose a life.")
        wrong_count -= 1

    print(current_word)
    print(assets.stages[wrong_count])


    if current_word == word:
        print("You win!")
        break

    if wrong_count <= 0:
        print(f"You lose!. The word was {word}")
        break
