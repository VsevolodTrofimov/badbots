#edit at will
number_of_actions = 3

def actions(actions):
	#TURNS NORMAL ACTIONS INTO DOOM REDICULOUS SHIT
	act = []

	for i in range(number_of_actions):
		act.append(False)

	if "turn_left" in actions:
		act[0] = True 

	if "turn_right" in actions:
		act[1] = True 

	if "attack" in actions:
		act[2] = True 

	return act