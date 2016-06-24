import sys
import memory
import data
import time
import json
import os
import replay

health_id = 0

def act(state):
	global health_id
	if data.seen.anything:
		data.seen.get()
		replay.add("add.item", [{"x":1 + health_id*2, "y":2 + health_id*3}, "health", health_id])
		health_id += 1
				
	return ["turn_right"]

