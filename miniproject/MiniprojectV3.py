import struct
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

img = cv2.imread("rbs_image.png")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

res = 25

coloraverages_red = np.zeros((res, res))
coloraverages_green = np.zeros((res, res))
coloraverages_blue = np.zeros((res, res))
for x in range(res):
    for y in range(res):
        avg_color_per_row = np.average(img[0 + x * int(500/res):int(500/res) + x * int(500/res), 0 + y * int(500/res):int(500/res) + y * int(500/res)], axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        coloraverages_red[x, y] = avg_color[2]
        coloraverages_green[x, y] = avg_color[1]
        coloraverages_blue[x, y] = avg_color[0]

average_color_image = np.dstack((coloraverages_red, coloraverages_green, coloraverages_blue))
normalized_color_averages = np.stack((coloraverages_red, coloraverages_green, coloraverages_blue), axis=-1) / 255.0
plt.imshow(normalized_color_averages, interpolation='nearest')
plt.show()