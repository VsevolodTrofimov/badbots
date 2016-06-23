from skimage import data
from skimage import transform as tf
from skimage.feature import (match_descriptors, corner_peaks, corner_harris,
                             plot_matches, BRIEF, blob_dog)
from math import sqrt
from skimage.color import rgb2gray

import matplotlib.pyplot as plt
import numpy as np
from skimage import io

from skimage import novice
from skimage import data
from . import Array

seen[]

picture = novice.open(data.data_dir + 'Sprites/blobs.png')

image = io.imread("Sprites/blobs.png")
image_gray = rgb2gray(image)

blobs_dog = blob_dog(image_gray, min_sigma=0.2, max_sigma=130, sigma_ratio=1.6, threshold=.1)
blobs_dog[:, 2] = blobs_dog[:, 2]

blobs = [blobs_dog]
colors = ['black']
titles = ['Difference of Gaussian']
sequence = zip(blobs, colors, titles)

plot[]

for blobs, color, title in sequence:
    fig, ax = plt.subplots(1, 1)
    ax.set_title(title)
    ax.imshow(image_gray, interpolation='nearest')
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=1, fill=False)
        ax.add_patch(c)
        plotx = picture.size/2 - (x*(-1) + picture.size)
        ploty = picture.size/2 - (y*(-1) + picture.size)
        for i in range (12):
            keypoints1 = corner_peaks(corner_harris(Array.image_arr[i]), min_distance=1)
            keypoints2 = corner_peaks(corner_harris(img2), min_distance=1)

            extractor = BRIEF()

            extractor.extract(Array.image_arr[i], keypoints1)
            keypoints1 = keypoints1[extractor.mask]
            descriptors1 = extractor.descriptors

            extractor.extract(img2, keypoints2)
            keypoints2 = keypoints2[extractor.mask]
            descriptors2 = extractor.descriptors

            matches12 = match_descriptors(descriptors1, descriptors2, cross_check=True)

            fig, ax = plt.subplots(nrows=2, ncols=1, sharex = True, sharey = True)
            if (plotx - X)**2 + (ploty - Y)**2 < r
                seen = [{
					"type": data.Array.image_arr[i],
					"center_shift": plotx,
					"distance": color/0.08
				}]
