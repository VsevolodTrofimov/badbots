from math import *

def location(player_cords, player_angle, distance, center_shift):
    item_angle = abs(asin(center_shift/distance))
    if center_shift:
        side = center_shift/abs(center_shift)
    else:
        side = 1
    real_angle = player_angle + item_angle * side

    item_x_shift = abs(cos(real_angle)) * distance
    item_y_shift = abs(sin(real_angle)) * distance

    item_cords = {
        "x": item_x_shift + player_cords["x"] * side,
        "y": item_y_shift + player_cords["y"] * side
    }

    print("ia", item_angle)
    print("ra", real_angle)
    print("ixs", item_x_shift)
    print("iys", item_y_shift)

    return item_cords


loc = location({
        "x": 2.0,
        "y": 3.0
    },
    0.0,
    5.0,
    4.0
)

print loc
