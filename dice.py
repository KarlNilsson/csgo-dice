import random
from sets import Set

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

def roll_session():
	equipment = Set([])
	flash_count = 0
	grenade_count = 0

	while True:
		die = roll()

		if die[0] != 6 and (die not in [(5,4), (5,3)]):
			equipment.add(die)
			break
		elif die == (6, 3) and flash_count < 2 and grenade_count < 4:
			flash_count += 1
			grenade_count += 1
		elif die[0] == 6 and die not in equipment and grenade_count < 4:
			grenade_count += 1

		equipment.add(die)

	equipment_list = list(equipment)
	if flash_count == 2 and grenade_count < 4:
		equipment_list.append((6,3))
	return sorted(equipment_list, key=lambda x: x[0])
