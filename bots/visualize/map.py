import numpy as np
import matplotlib.pyplot as plot

plot.axis([0, 50, 0, 40])
plot.ion()

class Add:
    def item(self, cords, type):

        type_color = {
            "health": "g"
        }

        marker = plot.Circle(
            (cords["x"], cords["y"]), radius=0.5,
            fc=type_color[type]
        )
        plot.gca().add_patch(marker)
        plot.draw()

    def direcional(cords, direction):
        pass


add = Add()
plot.show(block=False)
