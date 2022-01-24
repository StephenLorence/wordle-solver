# target_word.py

from ..helpers.helper_funcs import cls, compare_target_to_guess, validate_string_length


class TargetWord():
    """
    Class to serve as the target word to be guessed.
    Contains:
        word: the word itself.
        guess_set: a set of the guesses from the user.
    """
    def __init__(self, word):
        self.word = str(word).casefold()
        self.guess_set = set()
        self.letter_set = set()
        self.all_letters = set('abcdefghijklmnopqrstuvwxyz')
        self.result_list = []

    def guess_word(self, guess):
        """
        The user can guess the target word. They input a guess,
        which is validated (must be equal to the length of the
        target word), then added to the guess_set. Then, the
        new guess is compared to the target word and evaluated
        for correctness. The user is presented with feedback
        based on how close the guess was to the target word.
        """
        # Clean up the guess to ensure it's a string with no case.
        guess = str(guess).casefold()

        # Verify the guess is the same length as the target word.
        valid = validate_string_length(self.word, guess)

        if not valid:
            return f"{guess} is not {len(self.word)} letters long."
        else:
            # Verify that the guess hasn't already been tried.
            if guess in self.guess_set:
                return f"{guess} has already been tried."
            else:
                self.guess_set.add(guess)
                guess_result = compare_target_to_guess(self.word, guess)
                self.result_list.append(guess_result)
                self.letter_set = self.letter_set | set(guess)

        # Clear the screen
        cls()

        if guess_result is True:
            return 1
        else:
            # Print out each guess already tried.
            print('\n')
            for g in self.guess_set:
                print(g.upper())
            print ('\n\n')
            # Print out the current list of guess results.
            for r in self.result_list:
                print(r)
            print('\n\n')
            print(f"Letters guessed: {sorted(list(self.letter_set))}")
            print(f"Letters remaining: {sorted(list(self.all_letters - self.letter_set))}")




    
