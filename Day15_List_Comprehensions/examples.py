# Squares of numbers
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

# Even numbers
numbers = list(range(10))
evens = [x for x in numbers if x % 2 == 0]
print(evens)

# String uppercase
words = ["python", "coding", "ai"]
upper_words = [word.upper() for word in words]
print(upper_words)

# Length of each word
lengths = [len(word) for word in words]
print(lengths)
