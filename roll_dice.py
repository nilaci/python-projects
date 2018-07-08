import random

def roll_dice():
	return random.randint(1,6)

def compare(usr, comp):
	delim = '============='
	if usr == comp:
		print("%s\n It's a draw!\n User: %d\n Computer: %d\n%s" % (delim, usr, comp, delim))
		return
	if usr > comp:
		print("%s\n User wins!\n User: %d\n Computer: %d\n%s" % (delim, usr, comp, delim))
		return
	if usr < comp:
		print("%s\n Computer wins!\n User: %d\n Computer: %d\n%s" % (delim, usr, comp, delim))
	
user_rand_num = roll_dice()
comp_rand_num = roll_dice()

compare(user_rand_num, comp_rand_num)