import sys
import random
from string import ascii_lowercase

with open("/usr/share/dict/words") as word_list:
    full_list = word_list.read().lower().split()


def replay():
    play_again = input("Play again? Y/n: ")
    if play_again.lower() != 'n':
        return levels()
    else:
        print("Thanks for playing!")
        sys.exit()

def levels():
    difficulty = input("Pick a difficulty level -- [e]asy, [n]ormal, [h]ard: ")
    difficulty = difficulty.lower()
    if difficulty == 'e':
        while True:
            random_word = random.choice(full_list)
            if len(random_word) in range(4, 7):
                game(random_word)

    elif difficulty == 'n':
        while True:
            random_word = random.choice(full_list)
            if len(random_word) in range(7, 11):
                game(random_word)

    else:
        while True:
            random_word = random.choice(full_list)
            if len(random_word) in range(10, 50):
                game(random_word)

    return random_word

def game(random_word):
    good_guess = []
    bad_guess = []
    line = list(("_" * len(random_word)))
    choices = list(ascii_lowercase)
    print(*line)
    print(*choices)
    print("Welcome to Mystery Word! Your word has {} letters.".format(len(random_word)))

    while len(bad_guess) < 8 and set(good_guess) != set(random_word):
        guess = input("Guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("You can only guess one letter at a time! Try again.")
            continue

        if guess in good_guess or guess in bad_guess:
            print("You've already guessed that letter! Try again.")
        elif guess in random_word:
            print("'{}' is in the mystery word!".format(guess))
            good_guess.append(guess)
            for location, letter in enumerate(random_word):
                if guess == letter:
                    line[location] = guess
            print(*line)
            if guess in choices:
                choices.remove(guess)
                print(*choices)
        else:
            print("'{}' is not in the mystery word.".format(guess))
            bad_guess.append(guess)
            print(*line)
            if guess in choices:
                choices.remove(guess)
                print(*choices)

        print("You've used {}/8 bad guesses.".format(len(bad_guess)))

    if set(good_guess) == set(random_word):
        print("You win! The mystery word was {}".format(random_word))
    if len(bad_guess) == 8:
        print("Game over! The mystery word was {}".format(random_word))

    replay()

levels()
