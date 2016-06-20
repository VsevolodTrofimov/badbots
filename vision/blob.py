from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray

import matplotlib.pyplot as plt
import numpy as np
from skimage import io

image = io.imread("Sprites/blobs.png")
image_gray = rgb2gray(image)

blobs_dog = blob_dog(image_gray, min_sigma=0.1, max_sigma=225, threshold=0.1, overlap=0.7)

blobs = [blobs_dog]
colors = ['white']
titles = ['Difference of Gaussian']
sequence = zip(blobs, colors, titles)

for blobs, color, title in sequence:
    fig, ax = plt.subplots(1, 1)
    ax.set_title(title)
    ax.imshow(image, interpolation='nearest')
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=1, fill=False)
        ax.add_patch(c)

plt.show()
