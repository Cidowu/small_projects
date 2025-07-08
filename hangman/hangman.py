import random

with open("wordlist.txt", "r") as file:
    words = file.readlines()

word = random.choice(words).strip()
print(word)