# from ..visualize import map
import time
from ... import data


# map.add.item({
#     "x": 20,
#     "y": 30
# }, "health", 2)

def run_around():
    print("cmd")
    data.game.commands.add(["forward", "turn_left"])

run_around()
time.sleep(0.02)
run_around()
