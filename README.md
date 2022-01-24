The intent of this utility is to be able to solve 'Wordle' puzzles in an automated fashion.

Wordle is a game where users are asked to guess a five-letter word. The user has five total chances to guess the word. After each guess, the Wordle interface tells the user whether a given letter is 1.) in the word and in that exact spot;  2.) in the word at least once (but potentially more than once) but not in that spot; or 3.) not used in the word at all.

The plan with this utility is to take in a target_word parameter and then solve for that word in the fewest iterations possible, given feedback in the same fashion as Wordle.

I will start by re-creating the Wordle game with manual user input. The functions necessary for this should help when creating the automated solver.