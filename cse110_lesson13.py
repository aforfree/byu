""""
13 Prove: Weather Data
File: cse110_lesson13.py
Author: Evgeny Kozlov
github.com/aforfree/byu

"""

"""
Wind Chill Calculator

"""


def get_wind_chill(temperature: float, wind_speed: float) -> float:
    """
    Calculates wind chill
    """
    wind_chill = (
        35.74
        + 0.6215 * temperature
        - 35.75 * wind_speed**0.16
        + 0.4275 * temperature * wind_speed**0.16
    )
    return wind_chill


def convert_celcius_to_fahrenheit(celcius: float) -> float:
    """
    Converts celcius to fahrenheit
    """
    fahrenheit = celcius * 9 / 5 + 32
    return fahrenheit


def convert_meters_per_second_to_miles_per_hour(meters_per_second: float) -> float:
    """
    Converts meters per second to miles per hour
    """
    miles_per_hour = meters_per_second * 2.237
    return miles_per_hour


if __name__ == "__main__":
    print("Welcome!")
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").lower()

    if unit.lower() == "c":
        temperature = convert_celcius_to_fahrenheit(temperature)

    for s in range(5, 61, 5):
        wind_chill = get_wind_chill(temperature, s)
        print(
            f"At temperature {temperature:.1f}F, and wind speed {s} mph, the windchill is: {wind_chill:.2f}F"
        )
