from ..visualize import map
import time

for i in range(1, 10):
    map.add.item({
        "x": i*2,
        "y": i*3
    }, "health")
    print i
    time.sleep(0.5)

exit = input()
