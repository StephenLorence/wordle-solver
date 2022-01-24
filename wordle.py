# wordle.py

from random import choice
from english_words import english_words_lower_alpha_set as english_words
from application import generate_word_list, TargetWord


def wordle():

    while True:
        length = input("Enter word length: ")

        try:
            length = int(length)
            break
        except ValueError as ex:
            continue

    # Generate a list of words of the appropriate length.
    word_list = generate_word_list(length, english_words)

    # Randomly choose a target word from the filtered list.
    target_word = choice(word_list)

    # Create a TargetWord instance using the selected word.
    t = TargetWord(target_word)

    guess_count = 0

    while guess_count < length:

        guess = input(f"Guess a {length} letter word: ")

        result = t.guess_word(guess)
        if result == 1:
            print(t.word.upper())
            print("Success!")
            break
        else:
            guess_count += 1

    if result != 1:
        print("Sorry, you have run out of guesses.")
        print(f"The word was {t.word.upper()}")

    print("\n\n")

    retry = input("Game over! Play again? (Y or N): ")

    if retry.casefold() == 'y':
        wordle()
    else:
        return

if __name__ == '__main__':
    wordle()