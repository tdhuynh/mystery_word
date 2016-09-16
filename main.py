
import random
from string import ascii_lowercase

with open("/usr/share/dict/words") as word_list:
    full_list = word_list.read().lower().split()

random_word = random.choice(full_list)

print(random_word)
print("Welcome to Mystery Word! Your word has {} letters.".format(len(random_word)))

good_guess = []
bad_guess = []

line = list(("_" * len(random_word)))
choices = list(ascii_lowercase)

print(*line)
print(*choices)

while len(bad_guess) < 8 and set(good_guess) != set(random_word):
    guess = input("Guess one letter at a time: ")
    guess = guess.lower()

    if guess in good_guess or guess in bad_guess:
        print("You've already guessed that letter!")

    elif guess in random_word:
        print("{} is in the mystery word!".format(guess))
        good_guess.append(guess)
        for location, letter in enumerate(random_word):
            if guess == letter:
                line[location] = guess
        print(*line)

        if guess in choices:
            choices.remove(guess)
            print(*choices)

    else:
        print("{} is not in the mystery word.".format(guess))
        bad_guess.append(guess)

    print("You've used {}/8 bad guesses.".format(len(bad_guess)))

if set(good_guess) == set(random_word):
    print("You win! The mystery word was {}".format(random_word))
if len(bad_guess) == 8:
    print("Game over! The mystery word was {}".format(random_word))
