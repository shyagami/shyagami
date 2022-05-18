# This is my first python file to test my knowledge!

# Modules and Packages
from datetime import date


who = input("Who are you, what is your full name? ")
age = int(input("Tell me you age, how many years you will complete this year? "))
years = date.today().year

print(f'Did you know, that you name have about {len(who)} letters and you born on {years - age}?')