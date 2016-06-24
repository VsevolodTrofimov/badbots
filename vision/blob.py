from skimage import transform as tf
from skimage.feature import (match_descriptors, corner_peaks, corner_harris,
                             plot_matches, BRIEF, blob_dog)
from math import sqrt
from skimage.color import rgb2gray
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from skimage import novice
import skimage

import sys
sys.path.append(".")
import Array
import data
import threading
import time

class VisionThread( threading.Thread ):
    def process(self, img2, image_gray):
        # img2 = warp(img2)
        patch_size = [640]
        img2 = rgb2gray(img2)
        image_gray = rgb2gray(img2)

        blobs_dog = blob_dog(image_gray, min_sigma=0.2, max_sigma=225, sigma_ratio=1.6, threshold=.5)
        blobs_dog[:, 2] = blobs_dog[:, 2]

        blobs = [blobs_dog]
        colors = ['black']
        titles = ['Difference of Gaussian']
        sequence = zip(blobs, colors, titles)

        # plt.imshow(img2)
        # plt.axis("equal")
        # plt.show()

        for blobs, color, title in sequence:
            print(len(blobs))
            for blob in blobs:
                y, x, r = blob
                plotx = x
                ploty = y
                for i in range (3):
                    keypoints1 = corner_peaks(corner_harris(Array.image_arr[i]), min_distance=1)
                    keypoints2 = corner_peaks(corner_harris(img2), min_distance=1)

                    extractor = BRIEF(patch_size=30, mode="uniform")

                    extractor.extract(Array.image_arr[i], keypoints1)
                    keypoints1 = keypoints1[extractor.mask]
                    descriptors1 = extractor.descriptors

                    extractor.extract(img2, keypoints2)
                    keypoints2 = keypoints2[extractor.mask]
                    descriptors2 = extractor.descriptors

                    matches12 = match_descriptors(descriptors1, descriptors2, cross_check=True)
                    
                    # print(keypoints1, keypoints2)
                    # print(matches12)
                    #FUCKGGGPLAYT
                    for pizdezh in matches12:
                        X = keypoints2[pizdezh[1]][1]
                        Y = keypoints2[pizdezh[1]][0]

                    if sqrt((plotx - X)**2 + (ploty - Y)**2) < r:
                        seen = [{
                            "type": Array.type_arr[i],
                            "center_shift": (plotx - 160/2) * -0.02,
                            "distance": image_gray[y][x] / 0.08
                        }]
                        print seen
                        data.seen.add(seen)
                        break


    def run( self ):
        print("running low")
        while data.playing:
            if not data.last_frame["reserved"]:
                data.last_frame["reserved"] = True
                print("imma", self.name,
                     "and i reserved last frame with",
                     data.last_frame["id"])
                img2 = data.last_frame["image"]
                img_d = data.last_frame["depth"]
                self.process(img2, img_d)
            time.sleep(0.001)

