import json
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

image_file = io.imread("vision/Sprites/healthFace.png")
Health = rgb2gray(image_file)

image_file3 = io.imread("vision/Sprites/Enemie.png")
Enemie = rgb2gray(image_file3)

image_file4 = io.imread("vision/Sprites/ammo.png")
Ammo = rgb2gray(image_file4)

# image_file5 = io.imread("Sprites/Shells.PNG")
# Shells = rgb2gray(image_file5)

# image_file6 = io.imread("Sprites/chain__gun.PNG")
# Chain_gun = rgb2gray(image_file6)

# image_file7 = io.imread("Sprites/chain__saw.PNG")
# chain__saw = rgb2gray(image_file7)

# image_file8 = io.imread("Sprites/double_shot_gun.PNG")
# double_shot_gun = rgb2gray(image_file8)

# image_file9 = io.imread("Sprites/plasma_gun.PNG")
# plasma_gun = rgb2gray(image_file9)

# image_file10 = io.imread("Sprites/rocket_launcher.PNG")
# rocket_launcher = rgb2gray(image_file10)

# image_file11 = io.imread("Sprites/rockets.PNG")
# rockets = rgb2gray(image_file11)

# image_file12 = io.imread("Sprites/shot_gun.PNG")
# shot_gun = rgb2gray(image_file12)

image_arr = [Health, Enemie, Ammo]
type_arr = ["health", "enemy", "ammo"]
#, Chain_gun, chain__saw, double_shot_gun, plasma_gun, rocket_launcher, rockets, shot_gun]
