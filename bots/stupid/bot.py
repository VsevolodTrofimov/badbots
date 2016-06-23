from ..visualize import map
import time

map.add.item({
    "x": 20,
    "y": 30
}, "health", 2)

time.sleep(0.5)
map.add.enemy({
    "x": 20,
    "y": 10
}, 70, 1)

for i in range(40):
    time.sleep(0.03)
    map.add.enemy({
        "x": 20,
        "y": 10 + i/2
    }, 180, 1)

map.add.line({
        "x": 1,
        "y": 2
    }, {
        "x": 4,
        "y": 5
    },
    "wall",
    5
)
time.sleep(0.5)

map.remove_item("item", 2)
map.remove_item("line", 5)
time.sleep(0.5)
exit = input()
