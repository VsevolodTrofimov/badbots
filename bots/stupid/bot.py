from ..visualize import map
import time

map.add.item({
    "x": 20,
    "y": 30
}, "health")

time.sleep(0.5)
map.add.enemy({
    "x": 20,
    "y": 10
}, 70, 1)

for i in range(40):
    time.sleep(0.03)
    map.add.enemy({
        "x": 20 + i,
        "y": 10
    }, -90, 1)

exit = input()
