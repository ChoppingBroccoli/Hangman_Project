import random

word_with_dashes = ''
lives_remaining = 14

while True:
    if lives_remaining == 0:
        print('You are out of lives.')
        break
    else:
        words_list = ['cat', 'mouse', 'dog', 'snake', 'pig', 'horse']
        random_word = random.choice(words_list)
        print('Random word is: ', random_word)

        user_guess = input('Guess a letter: ')
        print('You guessed ' + user_guess)
    
# For each letter in random_word, if user_guess is in random_word, add the letter
# to a variable to be printed later

        for x in random_word:
            if x == user_guess:
                word_with_dashes = word_with_dashes + user_guess
            else:
                word_with_dashes = word_with_dashes + '-'
            continue

    print(word_with_dashes)


'''
### PSEUDO CODE ###

First,  check if the user has more than 14 lives. If True, randomly select a word
from words_list. If False, game ends.

If the user has more than 14 lives remaining, ask the user to guess one of
the letters in random_word. If they guess a letter correctly then update word_with_dashes
with the user_guess. If they guess incorrectly, update word_with_dashes with a '-'.

Ask the user for another guess then evaluate until all letters have been guessed.


'''
