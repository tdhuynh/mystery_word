import sys
import random

with open("/usr/share/dict/words") as word_list:
    full_list = word_list.read().lower().split()

def game():
    good_guess = []
    bad_guess = []
    random_word = random.choice(full_list)
    line = list(("_" * len(random_word)))
    print(random_word)
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
            print("{} is in the mystery word!".format(guess))
            good_guess.append(guess)
            for location, letter in enumerate(random_word):
                if guess == letter:
                    line[location] = guess
            print(*line)
        else:
            print("{} is not in the mystery word.".format(guess))
            bad_guess.append(guess)
        print("You've used {}/8 bad guesses.".format(len(bad_guess)))

    if set(good_guess) == set(random_word):
        print("You win! The mystery word was {}".format(random_word))
    if len(bad_guess) == 8:
        print("Game over! The mystery word was {}".format(random_word))

def replay():
    play_again = input("Play again? Y/n: ")
    if play_again.lower() != 'n':
        return game()
    else:
        print("See you later!")
        sys.exit()

game()

while True:
    replay()
