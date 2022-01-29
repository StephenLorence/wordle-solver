#helper_funcs.py

import os

def cls():
    """
    Create a function that lets us clear the screen of the terminal
    to make things easier to read.
    """
    os.system('cls' if os.name=='nt' else 'clear')

def generate_word_list(length, original_word_list):
    """
    Use the set of words from an original word list
    and filter that set to return only the words with a specified number
    of letters in them.
    """

    # Filter out periods ('.') first.
    no_periods = filter(lambda x: '.' not in x, original_word_list)

    return list(filter(lambda x: len(x) == length, no_periods))


def validate_string_length(target, guess):
    """
    Compare the length of the guess to the length of
    the target. Both must be valid strings.
    """
    try:
        return len(str(target)) == len(str(guess))
    except TypeError:
        return False

def check_index_position_matches(target, guess):
    """
    Compare two words for letters that are in the same position.
    Example: 'help' and 'halt' match 'h' and 'l' in the same index
        position.

    Returns a list of tuples consisting of each word in the guess and a
    corresponding 'True' or 'False' value for a positional match.
    Example: [('h', True), ('a', False), ('l', True), ('t', False)]
    """
    return list(zip(guess, map(lambda x: x[0] == x[1], zip(target, guess))))

def check_non_index_position_letter_matches(target, guess):
    """
    Compare two words for letters that match but are not in the
    same position.
    Example: 'help' and 'play' match 'p' and 'l' in different index
        positions.
    """

    # Create a dictionary with the index value of each letter in the
    # guess as a key and a tuple containing the letter and a starting
    # value of False.
    result_dict = dict(enumerate(zip(guess, [False] * len(guess))))
    
    # For each index position in guess, check for membership of target.
    # If the letter is in the target, set the second value in the tuple
    # to True.
    for idx, g in enumerate(guess):
        if g[0] in target:
            result_dict[idx] = (g, True)

    return result_dict

def generate_letter_count(word):
    """
    Generate a dictionary consisting of letters and frequency counts
    of a provided word.
    Example: 'porphyry' generates the following dictionary:
        {'p': 2, 'o': 1, 'r': 2, 'h': 1, 'y': 2}
    """

    # Create a set from the letters in the word.
    word_set = set(word)

    # Then create a dictionary from the set members and the count
    # of how many times that letter shows up in the word.
    return {x: word.count(x) for x in word_set}

def compare_target_to_guess(target, guess):
    """
    Check if the guess is equal to the target. If so, success!
    If not, check for index position matches, then check for
    letter matches that aren't index position matches.
    """

    if target == guess:
        return True

    # Generate a letter count for the target word:
    letter_count = generate_letter_count(target)

    # Check for positional matches.
    positional_results = check_index_position_matches(target, guess)

    # Check for non-positional matches.
    non_positional_results = check_non_index_position_letter_matches(target, guess)

    # Create a list of underscores equal to the length of the target word.
    comparison_length = len(target)
    comparison_character = ['_']

    comparison_result = comparison_character * comparison_length

    # For each index position, if the letter from guess matches
    # the letter from target, capitalize that letter and add it
    # to comparison_result.
    for idx, t in enumerate(positional_results):
        if t[1] == True:
            comparison_result[idx] = t[0].capitalize()

            # Also subtract 1 from that letter's value in letter_count.
            letter_count[t[0]] -= 1

    # For each element of non_positional_matches with a value of True in
    # the tuple's second position, skip the position if it is populated
    # with a letter rather than an underscore.
    for idx, t in non_positional_results.items():
        if comparison_result[idx] == '_':
            if t[1] == True:

                # Then, check if that element's letter has a positive value in letter_count.
                if letter_count[t[0]] > 0:

                    # If so, populate the letter into that position in comparison_result.
                    # The letter will be in lowercase to signal that the letter is in the word,
                    # but not in that position.
                    comparison_result[idx] = t[0].lower()

                    # Then subtract 1 from that letter's value in letter_count.
                    letter_count[t[0]] -= 1

    return comparison_result
    