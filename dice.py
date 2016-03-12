import random

def roll():
	correct_roll = False
	die1 = random.randint(1,6)
	while not correct_roll:
		die2 = random.randint(1,6)
		if die1 == 4:
			correct_roll = True
		elif die1 != 5 and die2 <= 5:
			correct_roll = True
		elif die1 == 5 and die2 <= 4:
			correct_roll = True
	return (die1, die2)