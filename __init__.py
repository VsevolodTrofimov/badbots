from __future__ import print_function
from vizdoom import *
import sys
import cv2
import time

#edit at will
save_min_replay = True

botname = "lookaround"
config = "basic"
vision_threads_amount = 1

episodes = 1
sleep_time = 1


#importing things other modules need
sys.path.append('./bots/')
sys.path.append('./bots/visualize/')
sys.path.append('./utilities/')

#import bot
sys.path.append('./bots/' + botname)
import bot

#import utilites

import decode
import data
import replay

#import vision
sys.path.append('./vision/')
import blob
#start vision
vision_threads = []

for i in range(vision_threads_amount):
	vision_threads.append(blob.VisionThread())
	vision_threads[-1].setName("vis"+str(i))
	vision_threads[-1].start()


#Putting config
game = DoomGame()
game.load_config("./launchers/configs/" + config + ".cfg")
#let`s go!
game.init()

counter = 0
for i in range(episodes):
	game.new_episode()
	while not game.is_episode_finished():
		#getting game state for modules
		state = game.get_state()
		img = state.image_buffer
		if game.get_screen_format() in [ScreenFormat.GRAY8, ScreenFormat.DEPTH_BUFFER8]:
			img_dis = img.reshape(img.shape[1], img.shape[2], 1)
			# Display the image here!
			cv2.imshow('Doom Buffer', img_dis)
			cv2.waitKey(sleep_time)

		counter +=1
		data.last_frame["image"] = img
		data.last_frame["depth"] = img
		data.last_frame["reserved"] = False
		data.last_frame["id"] = counter
		#acting
		bot_actions = bot.act(state)
		
		game.make_action(
			decode.actions(bot_actions)
		)
		data.playing = True
		time.sleep(0.1)
		

if save_min_replay:
	replay.save()

cv2.destroyAllWindows()
