# String Utility Functions
def format_name(name):
    return name.strip().title()

def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)
