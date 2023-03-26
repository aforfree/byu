""""
12 Prove: Assignment Data Analysis
File: cse110_lesson12.py
Author: Evgeny Kozlov
github.com/aforfree/byu
Submission comment:
Grade: 5. Shows creativity and exceeds requirements
Creativity: Added country of interest

"""

lowest_life_expectancy = [0, 0, 0, 100]
highest_life_expectancy = [0, 0, 0, 0]
average_life_expectancy = 0
lowest_life_expectancy_country = [0, 0, 0, 100]
highest_life_expectancy_country = [0, 0, 0, 0]
number_of_countries = 0

min_life_expectancy_country_of_interest = [0, 100]
max_life_expectancy_country_of_interest = [0, 0]
counts_in_country_of_interest = 0
average_life_expectancy_in_country_of_interest = 0


print("Welcome!")
year_of_interest = int(input("Enter a year of interest: "))
country_of_interest = input("Enter country of interest: ")

with open("life-expectancy.csv") as file:
    for line in file:
        row = line.split(",")
        if row[0] == "Entity":
            continue

        life_expectancy = float(row[3])
        country = row[0]
        year = int(row[2])

        if float(lowest_life_expectancy[3]) > life_expectancy:
            lowest_life_expectancy = row

        if float(highest_life_expectancy[3]) < life_expectancy:
            highest_life_expectancy = row

        if year == year_of_interest:
            average_life_expectancy += life_expectancy
            number_of_countries += 1

            if float(lowest_life_expectancy_country[3]) > life_expectancy:
                lowest_life_expectancy_country = row
            if float(highest_life_expectancy_country[3]) < life_expectancy:
                highest_life_expectancy_country = row

        if country.lower() == country_of_interest.lower():
            average_life_expectancy_in_country_of_interest += life_expectancy
            counts_in_country_of_interest += 1
            if min_life_expectancy_country_of_interest[1] > life_expectancy:
                min_life_expectancy_country_of_interest = [year, life_expectancy]
            if max_life_expectancy_country_of_interest[1] < life_expectancy:
                max_life_expectancy_country_of_interest = [year, life_expectancy]

    average_life_expectancy = average_life_expectancy / number_of_countries
    average_life_expectancy_in_country_of_interest = (
        average_life_expectancy_in_country_of_interest / counts_in_country_of_interest
    )

print(
    f"The overall max life expectancy is: {highest_life_expectancy[3]}"
    f"from {highest_life_expectancy[0]} in {highest_life_expectancy[2]}"
)

print(
    f"The overall min life expectancy is: {lowest_life_expectancy[3]}"
    f"from {lowest_life_expectancy[0]} in {lowest_life_expectancy[2]}"
)

print(f"For the year {year_of_interest}:")
print(
    f"The average life expectancy across all countries was {average_life_expectancy:.2f}"
)

print(
    f"The max life expectancy was in {highest_life_expectancy_country[0]} with {float(highest_life_expectancy_country[3]):.2f}"
)
print(
    f"The min life expectancy was in {lowest_life_expectancy_country[0]} with {float(lowest_life_expectancy_country[3]):.2f}"
)

print(
    f"The max life expectancy for {country_of_interest} was {float(min_life_expectancy_country_of_interest[1]):.2f} in {min_life_expectancy_country_of_interest[0]}"
)
print(
    f"The min life expectancy for {country_of_interest} was {float(max_life_expectancy_country_of_interest[1]):.2f} in {max_life_expectancy_country_of_interest[0]}"
)
print(
    f"The average life expectancy for {country_of_interest} was {average_life_expectancy_in_country_of_interest:.2f}"
)
