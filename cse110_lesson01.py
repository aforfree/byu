# CSE110 lesson 01
# by Evgeny Kozlov
# github.com/aforfree/byu

# colored 'color' word
OUTPUT_COLOR_WORD = f"\033[91m{'c'}\033[00m\033[92m{'o'}\033[00m\033[93m{'l'}\033[00m\033[94m{'o'}\033[00m\033[95m{'r'}\033[00m"

# User input
input_name = input(f"Hello there, what's your name (press enter after): ")
input_color = input(
    f"and what's your favorite {OUTPUT_COLOR_WORD} (press enter after): ")

# Answer
print(f"\nOh, I guess your favorite {OUTPUT_COLOR_WORD} is:")
# Print the color in bold
print("\033[01m", input_color, "\033[00m")
print(f"That's one of my favorite {OUTPUT_COLOR_WORD}s too!")
# Farewell on a grey background
print("\033[47m", f"Bye, {input_name}!", "\033[0m")
