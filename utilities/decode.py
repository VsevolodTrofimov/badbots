#edit at will
number_of_weapons = 7
number_of_actions = 3

def actions(actions):
	#TURNS NORMAL ACTIONS INTO DOOM REDICULOUS SHIT
	act = []

	for i in range(number_of_actions + number_of_weapons):
		act.append(False)

	for i in range(number_of_weapons):
		if "sel" + i in actions:
			act[i] = True

	if "forward" in actions:
		act[8] = True

	if "backward" in actions:
		act[9] = True

	if "move_left" in actions:
		act[10] = True   

	if "move_right" in actions:
		act[11] = True 

	if "turn_left" in actions:
		act[12] = True 

	if "turn_right" in actions:
		act[13] = True 

	if "attack" in actions:
		act[14] = True 

	return act