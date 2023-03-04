""""
08 Prove: Milestone & Final - Wordle Game
File: cse110_lesson08.py
Author: Evgeny Kozlov
github.com/aforfree/byu

Submission comment:
Grade: 5. Shows creativity and exceeds requirements
Creativity: Two logical paths, two different approaches,
            combined Milestone and Final,
            added quit option, random choice of word
"""
from random import choice

WORDS = ["Moroni", "Amulek", "Helaman", "Nephi", "Abinadi", "Alma", "Ammon"]


def play_with_hints(word):
    print("\n"
          "You are playing with hints. \n"
          "(Enter QUIT to quit the game)"
          "\n")

    hint = ['_' for i in range(len(word))]
    print(f"Your hint is: {' '.join(hint)}")

    guess_count = 0

    while user_input := input("What is your guess: ").lower():
        if user_input == "quit":
            print("You quit the game.")
            break

        if len(user_input) != len(word):
            print("Sorry, the guess must have the same number \n"
                  "of letters as the secret word.")
            continue

        guess_count += 1
        if user_input == word:
            print("You guessed the word! Congratulations! "
                  f"It took you {guess_count} guesses.")
            break
        else:
            print("")
            for i in range(len(word)):
                if user_input[i] in word:
                    if user_input[i] == word[i]:
                        hint[i] = user_input[i].upper()
                    else:
                        hint[i] = user_input[i]
                else:
                    hint[i] = '_'

            print(f"Your hint is: {' '.join(hint)}")


def play_without_hints(word):
    print("\n"
          "You are playing without hints. \n"
          "(Enter HINT if you want to play with hints \n"
          "otherwise enter QUIT to quit the game.)"
          "\n")

    guess_count = 0

    while user_guess := input("Enter the word to guess: ").lower():

        guess_count += 1

        if user_guess == word:
            print("You guessed the word!"
                  f"It took you {guess_count} guesses.")
            break
        else:
            match user_guess:
                case "hint":
                    play_with_hints(word)
                    break
                case "quit":
                    print("You quit the game.")
                    break
                case _:
                    print("Your guess was not correct. Please try again.\n")


print("Welcome to the word guessing game!")
while True:
    word = choice(WORDS).lower()
    user_choice = input(
        "Choose what Wordle game will you play, \n"
        "Enter 1 (with hints) or 2 (without hints): ").lower()
    if user_choice == "1":
        play_with_hints(word)
        break
    elif user_choice == "2":
        play_without_hints(word)
        break
    elif user_choice == "quit":
        print("You quit the game.")
        break
    else:
        print("Invalid input. Please try again. \n"
              "Or enter QUIT to quit the game.")
