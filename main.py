import numpy as np
import imageio
import scipy.ndimage
import cv2

def grayscale(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.114])

def dodge(front, back, epsilon=1e-6):  # Added epsilon to prevent division by zero
    result = front * 255 / (255 - back + epsilon)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')

img = "Give Your Image name"

s = imageio.imread(img)
g = grayscale(s)
i = 255 - g
b = scipy.ndimage.filters.gaussian_filter(i, sigma=10)
r = dodge(b, g)

cv2.imwrite('Give your specific name that can save the image', r)
