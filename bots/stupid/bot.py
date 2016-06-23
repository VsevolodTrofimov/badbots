# from ..visualize import map
import sys
sys.path.append('../calculate/')
sys.path.append('../')

from location import location
import memory
attack = False

def act(game_state):
    global attack
    if attack:
        attack = False
        return ["attack"]
    else:
        attack = True
        return ["turn_left", "attack"]
