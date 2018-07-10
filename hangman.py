import noun
	
delim = '=================='
GAME_START = 'Game begins! Guess the word!'
HIDE = '*'
MOVES = 6

def update_x_word(index, letter, x_word):
	new_x_word = ""
	for i in range(len(x_word)):
		if i in index:
			new_x_word += letter
		else:
			new_x_word += x_word[i]
	return new_x_word

def hide_word(game_word):
	x_word = ''
	for c in game_word:
		x_word += HIDE
	print('You have to guess a %d length word!' % (len(game_word)))	
	print(x_word)
	return x_word
	
def take_new_action():
	action = input("Press 'n' for a new game or any key to quit: ")
	return action
	
print(delim+'\n'+GAME_START)	
game_word = noun.get_word()
x_word = hide_word(game_word)

count = 0
game_on = True
while(game_on):
	letter = input('Please enter a letter: ')
	if len(letter) != 1:
		print("Multiple letters inserted, read carrefully the indication!")
		continue
	if letter in game_word:
		print("You guessed letter '%s'" %(letter))
		i = [i for i in range(len(game_word)) if game_word[i] == letter]
		x_word = update_x_word(i, letter, x_word)
		print(x_word)
	else:
		count += 1
	
	if HIDE in x_word and count < MOVES:
		continue
	elif HIDE not in x_word:
		print("You beat the game!")
	
	if count >= MOVES:
		print("GAME OVER! You failed to guess '%s' ..." %(game_word))
		
	if take_new_action() == 'n':
		game_word = noun.get_word()
		x_word = hide_word(game_word)
		count = 0
		continue
		
	game_on = False
	