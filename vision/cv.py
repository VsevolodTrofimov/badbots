from skimage import data
from skimage import transform as tf
from skimage.feature import (match_descriptors, corner_peaks, corner_harris,
                             plot_matches, BRIEF)
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np
from skimage import io

image_file2 = io.imread("Sprites\Test.png")
img2 = rgb2gray(image_file2)

image_file = io.imread("Sprites\healthFace.png")
img1 = rgb2gray(image_file)

image_file3 = io.impread("Sprites\Enemie.PNG")
img3 = rgbgray(image_file3)

image_file4 = io.imread("Sprites\Armor.png")
img4 = rgb2gray(image_file4)

image_file5 = io.impread("Sprites\Shells.PNG")
img5 = rgb2gray(image_file5)

image_file6 = io.impread("Sprites\Weapon.PNG")
img6 = rgb2gray(image_file6)

image_arr = [img1, img3, img4, img5, img6]

for i in range (6):
    keypoints1 = corner_peaks(corner_harris(image_arr[i]), min_distance=1)
    keypoints2 = corner_peaks(corner_harris(img2), min_distance=1)

    extractor = BRIEF()

    extractor.extract(image_arr[i], keypoints1)
    keypoints1 = keypoints1[extractor.mask]
    descriptors1 = extractor.descriptors

    extractor.extract(img2, keypoints2)
    keypoints2 = keypoints2[extractor.mask]
    descriptors2 = extractor.descriptors

    matches12 = match_descriptors(descriptors1, descriptors2, cross_check=True)

    fig, ax = plt.subplots(nrows=2, ncols=1)

    plt.gray()

    plot_matches(ax[0], image_arr[i], img2, keypoints1, keypoints2, matches12)
    ax[0].axis('off')

plt.show()
