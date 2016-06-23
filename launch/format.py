#!/usr/bin/env python
#####################################################################
# This script presents different formats of the screen buffer.
# OpenCV is used here to display images, install it or remove any
# references to cv2
# Configuration is loaded from "../../examples/config/basic.cfg" file.
# <episodes> number of episodes are played.
# Random combination of buttons is chosen for every action.
# Game variables from state and last reward are printed.

# To see the scenario description go to "../../scenarios/README.md"
#
#####################################################################
from __future__ import print_function

from random import choice
from vizdoom import *
from utility.decode_actions import decode
from .. import data
from ..bots.stupid import bot
import cv2

game = DoomGame()


# Use other config file if you wish.
game.load_config("badbots/launch/default.cfg")
# game.set_window_visible(False)

game.set_vizdoom_path("badbots/bin/vizdoom")

# Sets path to doom2 iwad resource file which contains the actual doom game. Default is "./doom2.wad".
game.set_doom_game_path("badbots/scenarios/freedoom2.wad")
# game.set_doom_game_path("../../scenarios/doom2.wad")  # Not provided with environment due to licences.

# Sets path to additional resources iwad file which is basically your scenario iwad.
# If not specified default doom2 maps will be used and it's pretty much useles... unless you want to play doom.
game.set_doom_scenario_path("badbots/scenarios/basic.wad")

# This is most fun. It looks best if you inverse colors.
game.set_screen_format(ScreenFormat.DEPTH_BUFFER8)

# These formats can be use bet they do not make much sense for cv2, you'll just get mixed up colors.
# game.set_screen_format(ScreenFormat.BGR24)
# game.set_screen_format(ScreenFormat.RGBA32)
# game.set_screen_format(ScreenFormat.BGRA32)
# game.set_screen_format(ScreenFormat.ABGR32)

# This one makes no sense in particular
# game.set_screen_format(ScreenFormat.DOOM_256_COLORS)

game.set_screen_resolution(ScreenResolution.RES_640X480)
game.init()

actions = [[True, False, False], [False, True, False], [False, False, True]]

episodes = 40
# sleep time in ms
sleep_time = 50



for i in range(episodes):
    print("Episode #" + str(i + 1))
    # Not needed for the first episdoe but the loop is nicer.
    game.new_episode()
    while not game.is_episode_finished():
        # Gets the state and possibly to something with it
        s = game.get_state()
        img = s.image_buffer
        misc = s.game_variables

        # Gray8 shape is not cv2 compliant
        if game.get_screen_format() in [ScreenFormat.GRAY8, ScreenFormat.DEPTH_BUFFER8]:
            img = img.reshape(img.shape[1], img.shape[2], 1)

        # Display the image here!
        cv2.imshow('Doom Buffer', img)
        cv2.waitKey(sleep_time)

        # Makes a random action and save the reward.
        # commands = game.make_action(
        #     decode(data.game.commands.get())
        # )
        act = decode(data.game.commands.get())
        r = game.make_action(act)

        print(act)

        print("State #" + str(s.number))
        print("Game Variables:", misc)
        print("=====================")

    print("Episode finished!")
    print("total reward:", game.get_total_reward())
    print("************************")

cv2.destroyAllWindows()
