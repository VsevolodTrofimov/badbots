from __future__ import print_function
import time
import threading
import sys

sys.path.append('./../utilities/')
import data

class VisionThread( threading.Thread ):
	def run( self ):
		print("running low")
		while data.playing:
			if not data.last_frame["reserved"]:
				data.last_frame["reserved"] = True
				print("imma", self.name,
					 "and i reserved last frame with",
					 data.last_frame["image"])
				time.sleep(2)
				img1 = data.last_frame["image"]
				img_d = data.last_frame["depth"]
				
				seen = [{
					"type": "health",
					"center_shift": 10,
					"distance": 20
				}]

				for item in seen:
					data.seen.add(item)
				data.playing = False
			time.sleep(0.1)