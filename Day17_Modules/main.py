# Importing modules
import math_utils
import string_utils

# Using math functions
print("Addition:", math_utils.add(10, 5))
print("Multiplication:", math_utils.multiply(4, 3))

# Using string functions
name = "   xyz   "
formatted_name = string_utils.format_name(name)
print("Formatted Name:", formatted_name)

text = "Python Programming"
print("Vowel Count:", string_utils.count_vowels(text))
