""""
11 Prove: Milestone
File: cse110_lesson11.py
Author: Evgeny Kozlov
github.com/aforfree/byu

"""

lowest_life_expectancy = [0, 0, 0, 100]
highest_life_expectancy = [0, 0, 0, 0]
average_life_expectancy = 0
lowest_life_expectancy_country = [0, 0, 0, 100]
highest_life_expectancy_country = [0, 0, 0, 0]
number_of_countries = 0

print("Welcome!")
year_of_interest = int(input("Enter a year of interest: "))

with open("life-expectancy.csv") as file:
    for line in file:
        row = line.split(",")
        if row[0] == "Entity":
            continue

        life_expectancy = float(row[3])
        if float(lowest_life_expectancy[3]) > life_expectancy:
            lowest_life_expectancy = row

        if float(highest_life_expectancy[3]) < life_expectancy:
            highest_life_expectancy = row

        if int(row[2]) == year_of_interest:
            average_life_expectancy += life_expectancy
            number_of_countries += 1

            if float(lowest_life_expectancy_country[3]) > life_expectancy:
                lowest_life_expectancy_country = row
            if float(highest_life_expectancy_country[3]) < life_expectancy:
                highest_life_expectancy_country = row

    average_life_expectancy = average_life_expectancy / number_of_countries

print(f"The overall max life expectancy is: {highest_life_expectancy[3]}"
      f"from {highest_life_expectancy[0]} in {highest_life_expectancy[2]}")

print(f"The overall min life expectancy is: {lowest_life_expectancy[3]}"
      f"from {lowest_life_expectancy[0]} in {lowest_life_expectancy[2]}")

print(f"For the year {year_of_interest}:")
print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")

print(f"The max life expectancy was in {highest_life_expectancy_country[0]} with {float(highest_life_expectancy_country[3]):.2f}")
print(f"The min life expectancy was in {lowest_life_expectancy_country[0]} with {float(lowest_life_expectancy_country[3]):.2f}")
