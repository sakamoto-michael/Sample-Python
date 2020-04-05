# Exploring the standard library
import random
import math
import datetime
import calendar
import os
import antigravity # Python memes

# Using the random module
characters = ['Pikachu', 'Joker', 'ZSS', 'R.O.B.', 'Link']

random_character = random.choice(characters)
print(random_character)

# Using the math module
rads = math.radians(90)
print(math.sin(rads))

# Using datetime
today = datetime.date.today()
print(today)

# Using calendar
print(calendar.isleap(2020))

# Using OS module
print(os.getcwd()) # Gets current working directory

# Dunder = double underscore
print(os.__file__) # File location of the OS module