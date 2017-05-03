##### Psudeo code#####
# 1) generate list of words
# 2) ask user for a letter
# 3) check if letter is in the word
#   3a) if not, reduce lives by 1
#   3b) if it is, add to "guessed" variable and show remaining spaces
# 4) if lives == 0, end game
# 5) if all letters guessed, end game
######################

# import random module
import random

# initialize blanks variable to empty string. Don't recall the purpose for this...
blanks = ''

# lives left initialized to 14
lives = 14

# list of words to work with
words_list = ['chicken', 'horse', 'cat', 'mause', 'dag', 'goat']


# while lives do not equal zero, chose a random, prompt the user for a guess, then analyze the guess
while lives != 0:
    # randomly choose a word from words_list then prints it to stdout
    chosen_word = random.choice(words_list)
    print('Randomly chosen word:', chosen_word)

    # ask user for a letter
    guessed_letter = input('Guess a letter: ')
    print('You guessed the letter,', str.upper(guessed_letter))

    the_word = ''

    for x in chosen_word:
        if x == guessed_letter:
            print(x)
        else:
            print('- ')
            continue
            lives = lives - 1
            print('Lives remaining:', lives)

'''
    if guessed_letter == match:
        print('You got one right.', str.upper(guessed_letter), "is in", chosen_word)
        continue
    else:
        print('Sorry, the letter', str.upper(guessed_letter), 'is not in', chosen_word)
        # lives = lives - 1
         #blanks = blanks + '_ '
        continue

    break
#print(blanks)
'''