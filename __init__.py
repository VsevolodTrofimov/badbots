from __future__ import print_function
from vizdoom import *
import sys
import cv2
import time

#edit at will
botname = "lookaround"
config = "basic"
episodes = 10
sleep_time = 20


#importing things other modules need
sys.path.append('./bots/')
sys.path.append('./utilities/')

#import bot
sys.path.append('./bots/' + botname)
import bot

#import utilites

import decode
import data

#import vision
sys.path.append('./vision/')
import fake_see
#start vision
vision1 = fake_see.VisionThread()
vision1.setName("vis1")
vision1.start()
time.sleep(0.0001)
vision2 = fake_see.VisionThread()
vision2.setName("vis2")
vision2.start()

#Putting config
game = DoomGame()
game.load_config("./launchers/configs/" + config + ".cfg")
game.set_screen_format(ScreenFormat.DEPTH_BUFFER8)

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
			img = img.reshape(img.shape[1], img.shape[2], 1)

		counter +=1
		data.last_frame["image"] = counter
		data.last_frame["depth"] = img
		data.last_frame["reserved"] = False
		#acting
		bot_actions = bot.act(state)
		
		game.make_action(
			decode.actions(bot_actions)
		)
		data.playing = True
		# Display the image here!
		cv2.imshow('Doom Buffer', img)
		cv2.waitKey(sleep_time)

cv2.destroyAllWindows()
