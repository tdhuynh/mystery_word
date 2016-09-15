
import random

with open("/usr/share/dict/words") as word_list:
    full_list = word_list.read().upper().split()

random_word = random.choice(full_list)
print(random_word)

print("Welcome to Mystery Word! Your word has {} letters.".format(len(random_word)))

good_guess = []
bad_guess = []

while len(bad_guess) < 8:
    guess = input("Guess one letter at a time: ")
    guess = guess.upper()

    if guess in good_guess or guess in bad_guess:
        print("You've already guessed that letter!")

    elif guess in random_word:
        print("{} is in the mystery word!".format(guess))
        good_guess.append(guess)
        print(good_guess)

    else:
        print("{} is not in the mystery word.".format(guess))
        bad_guess.append(guess)
        print(bad_guess)
    print("You've used {}/8 bad guesses.".format(len(bad_guess)))

if len(bad_guess) == 8:
    print("Game over! The mystery word was {}".format(random_word))
