# import random module which is used to randomly choose a word from the words variable
import random

#  List of words to guess
words = ['chicken', 'dog', 'cat', 'mouse', 'frog']

# Player starts with 14 lives. Decrements by one for every wrong guess
lives_remaining = 14

# Letters guessed by Player assigned to this variable
# Used by print_word_with_blanks()
guessed_letters = ''

def pick_a_word():
	return random.choice(words)


# Controls the game. Calls pick_a_word() function and assigns value to the word variable.
# While loop will end either when Player guesses the word (process_guess()) or lives_remaining == 0
def play():
	word = pick_a_word()
	while True:
		guess = get_guess(word)
		if process_guess(guess, word): # process_guess() stub where every guess is wrong
			print ('You win!')
			break
		if lives_remaining == 0:
			print ()
			print ('You are Hung!')
			print ('The word was: ' + word)
			break

# Prompts Player to guess a letter
# Prints progress to screen. Shows letters (guess variable) Player has guessed correctly so far
# Prints a '-' for each letter Player has yet to guess
def get_guess(word):
	print_word_with_blanks(word)
	print ('Lives Remaining: ' + str(lives_remaining))
	guess = input (' Guess a letter ')
	return guess

# Evaluates each letter in guessed_letters.
# If letter exists, letter is added to display_word
# If letter does not exist, '-' is added to display_word
# get_guess() uses this to print game progress to screen
def print_word_with_blanks(word):
	display_word = ''
	for letter in word: # Evaluate each letter in randomly chosen word
		if guessed_letters.find(letter) > -1: # .find returns -1 if letter is not found in guessed_letters
			# guessed letter found in word
			display_word = display_word + letter
		else:
			# guessed letter NOT found in word
			display_word = display_word + '-'
	print (display_word)

# Adds Player guess to guessed_letters and decrements lives_remaining by 1
def process_guess(guess, word):
	global lives_remaining
	global guessed_letters
	if word.find(guess) == -1: # Compare word and guess. If they are different the word has not been guessed
		lives_remaining = lives_remaining - 1 # Guess was wrong. Decrement lives_remaining by one
	guessed_letters = guessed_letters + guess # Assign guess to guessed_letters
	if all_letters_guessed(word):
		return True

def all_letters_guessed(word):
	for letter in word:
		if guessed_letters .find(letter) == -1: # Compare each letter in word against guess (guessed_letters set to guess in process_guess()
			return False # Letter in word is not found in guess
	return True

'''
# Adds Player guess to guessed_letters and decrements lives_remaining by 1
def process_guess(guess, word):
	global lives_remaining
	global guessed_letters
	lives_remaining = lives_remaining - 1
	guessed_letters = guessed_letters + guess
	return False
'''



play()