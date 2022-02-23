# What is python used for?

"""

Web Development

Data Science
Machine Learning
Artificial Intelligence

Web Scraping

Automation (Dev Ops & General tasks)

"""

from logging import StringTemplateStyle
print("\nIn this tutorial, I learned about: \n\n * Strings, \n * Integers & Floats, \n * String Concatenation, \n * Defining variables and Defining functions! \n\nI coded out formulas to: \n\n * Calculate the number of minutes & number of seconds in a static number of days, \n * Calculate the number of minutes & number of seconds in any day using user input, \n * and Defined formulas as functions! \n")

# Simplest program we can write.


# print(1)

# # A little more complicated but essentially the same simple code as above.
# print("200 is a great number")

# # Data Types String (str), Integer - whole number (int), Floating Point Number - fraction/decimal (float).
# print(3.5)
# print(3)

# Arithmetic Operators
minutes_for_20_days = (20 * 24 * 60)

# How do we combine text and calculation? string concatenation str + variable/calc + str
# concatenation without using format
# print("20 days are " + str(minutes_for_20_days) + " minutes")
# # concatenation with using format
# print(f"20 days are {minutes_for_20_days} minutes")

# This is a variable representing a days to minutes conversion and the goal is to have an input driven version of this at the end.
minutes_for_35_days = (35 * 24 * 60)

# Formatting a variable.
# print(f"35 days are {minutes_for_35_days} minutes")

# # Changing the variable manually.
# minutes_for_110_days = (110 * 24 * 60)

# # Formatting the new variable.
# print(f"110 days are {minutes_for_110_days} minutes")

# Creating a variable to accept input.
days_to_convert = input(
    "Enter the number of days you want to convert: ")

# Print statement using variables and commas to concatenate.
# print(days_to_convert, "days are", int(days_to_convert) * 24 * 60, "minutes.")

# Variable created using input variable and formula concatenation.
minute_conversion = int(days_to_convert) * 24 * 60

# Perfected operation without formatting.
# print(days_to_convert, "days are", minute_conversion, "minutes.")

# Perfected operation with formatting.
# print(f"{days_to_convert} days are {minute_conversion} minutes")

# its_boolean = (f"{days_to_convert.isdigit()},  {days_to_convert.isalpha()}")
# print(its_boolean)

# Days to seconds as an input variable.
second_conversion = int(days_to_convert) * 24 * 60 * 60

# Using formatting to code similar to conversation.
# print(f"{days_to_convert} days are {second_conversion} seconds")


# creating a function to convert days into minutes
def days_to_minutes(days_to_convert):
    print(f"{days_to_convert} days are {minute_conversion} minutes")


# creating a function to convert days into seconds
def days_to_seconds(days_to_convert):
    print(f"{days_to_convert} days are {second_conversion} seconds")


days_to_minutes(days_to_convert)

days_to_seconds(days_to_convert)
