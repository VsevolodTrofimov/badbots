from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray

import matplotlib.pyplot as plt
import numpy as np
from skimage import io

image = io.imread("Sprites/blobs.png")
image_gray = rgb2gray(image)

blobs_dog = blob_dog(image_gray, min_sigma=0.2, max_sigma=130, sigma_ratio=1.6, threshold=.1)
blobs_dog[:, 2] = blobs_dog[:, 2]

blobs = [blobs_dog]
colors = ['black']
titles = ['Difference of Gaussian']
sequence = zip(blobs, colors, titles)

for blobs, color, title in sequence:
    fig, ax = plt.subplots(1, 1)
    ax.set_title(title)
    ax.imshow(image_gray, interpolation='nearest')
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=1, fill=False)
        ax.add_patch(c)

plt.show()
