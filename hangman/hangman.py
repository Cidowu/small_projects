import random

with open("wordlist.txt", "r") as file:
    words = file.readlines()

word = random.choice(words).strip()

guesses = []
tries = 7
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print("")

    guess = input(f"you have {tries} tries left. Guess a letter: ").lower().strip()
    guesses.append(guess)

    for letter in guesses:
        if letter not in word.lower():
            tries -= 1
            if tries == 0:
                break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"Congratulations! You guessed the word: {word}")
else:
    print(f"Sorry, you ran out of tries. The word was: {word}")
