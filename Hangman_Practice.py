##### Psudeo code#####
# 1) generate list of words
# 2) ask user for a letter
# 3) check if letter is in the word
#   3a) if not, reduce lives by 1
#   3b) if it is, add to "guessed" variable and show remaining spaces
# 4) if lives == 0, end game
# 5) if all letters guessed, end game
######################

import random
blanks = ''
lives = 14

# list of words to work with
words_list = ['chicken', 'horse', 'cat', 'mouse', 'dog', 'goat']

# randomly chooses a word from words_list then prints it to stdout
chosen_word = random.choice(words_list)
print('Randomly chosen word:', chosen_word)


guessed_letter = input('Guess a letter')
while lives < 14:
    for each_letter in chosen_word: #not right. prints all print statements for each letter in the chosen word
        if guessed_letter == each_letter:
            print('You got one right. ', guessed_letter, "is in the word")
            continue
        elif lives < 14:
            print('Guess again')
        else:
            print('Sorry, ', guessed_letter, 'is not in the word')
            lives = lives - 1
    break
        #blanks = blanks + '_ '

#print(blanks)
