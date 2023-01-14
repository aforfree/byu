# CSE110 lesson 02: Mad Libs
# by Evgeny Kozlov
# github.com/aforfree/byu

# input underlined
def input_underlined(prompt):
    return input(f"\033[0m{prompt}\033[4m")
# output in bold
def bold(arg):
    return f"\033[1m{arg}\033[0m"

print("Please enter the following:\n")

# Input
adjective_1 = input_underlined("adjective: ")
animal = input_underlined("animal: ")
verb_1 = input_underlined("verb: ")
exclamation = input_underlined("exclamation: ").capitalize()
verb_2 = input_underlined("verb: ")
verb_3 = input_underlined("verb: ")
adjective_2 = input_underlined("adjective: ")
print('\033[0m') #underline off

# Output
print(f"Your story is:\n")

# required part
print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f"{bold(adjective_1)} {bold(animal)} {bold(verb_1)} down the hallway. \"{bold(exclamation)}!\" I yelled. But all")
print(f"I could think to do was to {bold(verb_2)} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {bold(verb_3)}")
print(f"right in front of my family.")

# creattive part
article = "an" if adjective_2[0] in "aeiou" else "a"
print(f"I know, the whole story seems to be an AI nonsense or like {bold(article)} {bold(adjective_2)} dream.")
print(f"However, it is a true story, definitely not chatGPT. I hope you enjoyed it!")

