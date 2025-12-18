def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    counter = 0
    unique_vowels = set()
    for char in text:
        if char in vowels:
            counter += 1
            unique_vowels.add(char)
    return counter, unique_vowels
