# Exercise 1
# Print first and last character
text = "Python"
print(text[0])
print(text[-1])

# Exercise 2
# Convert string to uppercase
name = "xyz"
print(name.upper())

# Exercise 3
# Replace a word
sentence = "I love Python"
print(sentence.replace("Python", "coding"))

# Exercise 4
# Check if string contains only digits
num = "12345"
print(num.isdigit())

# Exercise 5
# Text Analyzer
text = input("Enter a sentence: ")

print("\nAnalysis:")
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Number of characters:", len(text))
print("Contains digits:", any(char.isdigit() for char in text))
