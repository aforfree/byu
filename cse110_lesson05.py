""""
05 Prove: Milestone - Adventure Game
File: cse110_lesson05.py
Author: Evgeny Kozlov
github.com/aforfree/byu

Submission comment:
Grade: 5. Shows creativity and exceeds requirements
Creativity: Two logical paths, two different approaches, added quit option
"""


def nested_if_statements():
    print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.")
    print("Which one do you want to pick up? (you might also QUIT)")

    user_input = input("Enter MATCH, FLASHLIGHT, or QUIT: ").lower()

    if user_input == "match":
        print("You pick up the match and strike it, and for an instant, the forest around you is illuminated."
              "You see a large grizzly bear, and then the match burns out."
              "Do you want to RUN, or HIDE behind a tree?")
        user_input = input("Enter RUN or HIDE: ").lower()
        if user_input == "run":
            print("You run away from the bear and get away safely.")
        elif user_input == "hide":
            print(
                "You hide behind a tree and the bear finds you. You are eaten by the bear.")
        else:
            print("Invalid input. You are eaten by the bear.")
    elif user_input == "flashlight":
        print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, "
              "but you thought you also heard something off to the side. "
              "Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
        user_input = input("Enter FOLLOW or LOOK: ").lower()
        if user_input == "follow":
            print("You made a few steps and came across two grizzly bears. "
                  "They asked you politely what time it was implying that it's too late. "
                  "Do you want to RUN or FIGHT the bears?")
            user_input = input("Enter RUN or FIGHT: ").lower()
            if user_input == "RUN":
                print("You run away from the bears and get away safely.")
            elif user_input == "FIGHT":
                print("As you moved towards them making awful look, bears got very frightened. "
                      "They run away and you are safe now. NO-BEAR ZONE!")
            else:
                print("Invalid input. Two grizzly bears came from trees and ate you.")
        elif user_input == "look":
            print("You saw two grizzly bears. You decide you'd rather not go further. "
                  "Smart choice! You go home safely.")
        else:
            print(
                "Invalid input. While you were hesitating a rotten tree fell on you. You are dead.")
    elif user_input == "quit":
        print("You quit the game.")
    else:
        print("Invalid input. You are eaten by the bear.")


def dictionary_tree():
    scenario_tree = {
        "start": {
            "text": "You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. "
                    "Which one do you want to pick up? (you might also QUIT any time) ",
            "match": {
                "text": "You pick up the match and strike it, and for an instant, "
                        "the forest around you is illuminated. You see a large grizzly bear, "
                        "and then the match burns out. Do you want to RUN, or HIDE behind a tree? ",
                "run": {
                    "text": "You run away from the bear and get away safely. "
                            "Game over."
                },
                "hide": {
                    "text": "You hide behind a tree and the bear goes around, eventually he'll find you. "
                            "Would you SHOUT out loud or throw a ROCK at the bear? ",
                    "shout": {
                        "text": "You shout at the bear and it runs away. You are safe. "
                                "Game over."
                    },
                    "rock": {
                        "text": "You throw a rock at the bear and it runs away. You are safe. "
                                "Game over."
                    }
                }
            },
            "flashlight": {
                "text": "You pick up the flashlight and turn it on. You see the pathway lit up "
                        "in front of you, but you thought you also heard something off to the side. "
                        "Do you want to FOLLOW the path or LOOK in the trees for the thing that "
                        "made the noise? ",
                "follow": {
                    "text": "You made a few steps and came across two grizzly bears. "
                            "They asked you politely what time it was implying that it's too late. "
                            "Do you want to RUN or FIGHT the bears? ",
                    "run": {
                        "text": "You run away from the bears and get away safely. "
                                "Game over."
                    },
                    "fight": {
                        "text": "As you moved towards them making awful look, bears got very frightened. "
                                "They run away and you are safe now. NO-BEAR ZONE !"
                                "Game over."
                    }
                },
                "look": {
                    "text": "You saw two grizzly bears. You decide you'd rather not go further. "
                            "Smart choice! You go home safely. "
                            "Game over."
                }
            }
        },
    }

    current_scenario = scenario_tree["start"]
    while True:
        if "Game over." in current_scenario["text"]:
            print('\n'+current_scenario["text"])
            break

        user_input = input('\n'+current_scenario["text"]).lower()
        if current_scenario.get(user_input, None) is not None:
            current_scenario = current_scenario[user_input]
        elif user_input == "quit":
            print("You quit the game.")
            break
        else:
            print("Invalid input. Please try again. Or enter QUIT to quit the game.")


print("Welcome to the adventure game!")
while True:
    user_choice = input(
        "Choose one of them. Enter 1 (Nested if statements) or 2 (Dictionary tree): ").lower()
    if user_choice == "1":
        nested_if_statements()
        break
    elif user_choice == "2":
        dictionary_tree()
        break
    elif user_choice == "quit":
        print("You quit the game.")
        break
    else:
        print("Invalid input. Please try again. Or enter QUIT to quit the game.")
