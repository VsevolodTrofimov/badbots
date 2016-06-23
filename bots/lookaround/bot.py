import sys
import memory
import data
import time
import datetime
import json
import os
health_id = 0

replay = ""

def add_to_replay(fucntion, params):
	global replay
	code = fucntion + "("
	code += json.dumps(params)[1:-1]
	code += ") \n\n"
	replay+= code

add_to_replay("add.item", [{"x":1, "y":2}, "health", health_id])
def act(state):
	global health_id
	if data.seen.anything:
		data.seen.get()
		health_id += 1
				
	return ["turn_right"]

def save_replay():
	now = str(datetime.datetime.now())
	min_now = now.split(" ")[1].split(".")[0]
	f = open("replays/min/" + min_now + ".txt", "w")
	f.write(replay)