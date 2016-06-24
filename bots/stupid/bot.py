# from ..visualize import map
import time
from ... import data

# from ..visualize import map
# counter = 1

def bot():
    # counter +=1
    def run_around():
        data.game_commands.put(["forward", "turn_left"])
    run_around()

    # map.add.item({
    #     "x": 20 +counter,
    #     "y": 30
    # }, "health", 2)
