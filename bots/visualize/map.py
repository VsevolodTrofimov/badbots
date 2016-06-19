import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plot
import numpy as np
from scipy import ndimage
from matplotlib.patches import Wedge

plot.axis([0, 50, 0, 40])
plot.ion()

itemsize = 1.0
drew = {}

def clearfix():
    # plot.axis('equal')
    plot.draw()

class Add:



    def item(self, cords, type):
        type_color = {
            "health": "g"
        }

        print itemsize/2

        marker = plot.Circle(
            (cords["x"], cords["y"]), radius=itemsize/2,
            fc=type_color[type]
        )
        plot.gca().add_patch(marker)
        clearfix()

    def enemy(self, cords, angle, id):

            if id in drew:
                marker = drew[id]
                for part in marker:
                    part.remove()

            def half_circle(cords, angle=0, ax=None):
                """
                Add two half circles to the axes *ax* (or the current axes) at the lower
                left corner of the axes with the specified facecolors *colors* rotated at
                *angle* (in degrees).
                """
                if ax is None:
                    ax = plot.gca()
                center = (cords["x"], cords["y"])
                radius = itemsize/2
                theta1, theta2 = angle, angle + 180
                colors=('y','r')
                w1 = Wedge(center, radius, theta1, theta2, fc=colors[0])
                w2 = Wedge(center, radius, theta2, theta1, fc=colors[1])
                return [w1, w2]

            marker = half_circle(cords, angle)
            drew[id] = marker
            for part in marker:
                plot.gca().add_patch(part)

            clearfix()

add = Add()
plot.show(block=False)
