import sys
import memory
import data

def act(state):
	if data.seen.anything:
		data.seen.get()
		print("WOW NYAHA!!")
	return ["turn_right"]