from __future__ import print_function
from vizdoom import *
import sys

import cv2

#edit at will
botname = "stupid"
config = "basic"
episodes = 10
sleep_time = 20

#import bot
sys.path.append('./bots/' + botname)
import bot

#import utilites
sys.path.append('./utilities/')
import decode


#Putting config
game = DoomGame()
game.load_config("./launchers/configs/" + config + ".cfg")
game.set_screen_format(ScreenFormat.DEPTH_BUFFER8)

#let`s go!
game.init()

for i in range(episodes):
	game.new_episode()
	while not game.is_episode_finished():
		#getting game state for modules
		state = game.get_state()
		img = state.image_buffer
		if game.get_screen_format() in [ScreenFormat.GRAY8, ScreenFormat.DEPTH_BUFFER8]:
			img = img.reshape(img.shape[1], img.shape[2], 1)

		#acting
		bot_actions = bot.act(state)
		
		game.make_action(
			decode.actions(bot_actions)
		)
		
		# Display the image here!
		cv2.imshow('Doom Buffer', img)
		cv2.waitKey(sleep_time)

cv2.destroyAllWindows()
