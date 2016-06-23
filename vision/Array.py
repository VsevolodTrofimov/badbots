import json
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

image_file2 = io.imread("Sprites\Test.png")
img2 = rgb2gray(image_file2)

image_file = io.imread("Sprites\healthFace.png")
Health = rgb2gray(image_file)

image_file3 = io.impread("Sprites\Enemie.PNG")
Enemie = rgbgray(image_file3)

image_file4 = io.imread("Sprites\Armor.png")
Armor = rgb2gray(image_file4)

image_file5 = io.impread("Sprites\Shells.PNG")
Shells = rgb2gray(image_file5)

image_file6 = io.impread("Sprites\chain__gun.png")
Chain_gun = rgb2gray(image_file6)

image_file7 = io.impread("Sprites\chain__saw.png")
chain__saw = rgb2gray(image_file7)

image_file8 = io.impread("Sprites\double_shot_gun.png")
double_shot_gun = rgb2gray(image_file8)

image_file9 = io.impread("Sprites\plasma_gun.png")
plasma_gun = rgb2gray(image_file9)

image_file10 = io.impread("Sprites/rocket_launcher.png")
rocket_launcher = rgb2gray(image_file10)

image_file11 = io.impread("Sprites/rockets.png")
rockets = rgb2gray(image_file11)

image_file12 = io.impread("Sprites\shot_gun.png")
shot_gun = rgb2gray(image_file12)

image_arr = [Health, Enemie, Armor, Shells, Chain_gun, chain__saw, double_shot_gun, plasma_gun, rocket_launcher, rockets, shot_gun]

json.dumps(image_arr[])
