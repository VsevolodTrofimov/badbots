import datetime
import time
import json

replay = ""
last_time = time.time()

def add(fucntion, params):
	global replay
	global last_time

	gap = time.time() - last_time
	code = "time.sleep(" + str(gap) + ") \n"

	code += fucntion + "("
	code += json.dumps(params)[1:-1]
	code += ") \n"
	
	replay+= code


def save():
	now = str(datetime.datetime.now())
	min_now = now.split(" ")[1].split(".")[0]
	f = open("replays/min/" + min_now + ".txt", "w")
	f.write(replay)