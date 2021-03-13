#  To preprocess image for Tesseract, use any of the following python functions


import cv2
import numpy as np


img = cv2.imread('image.jpg')

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
