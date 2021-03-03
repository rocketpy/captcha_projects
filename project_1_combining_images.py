import os
import cv2
import numpy as np
import Image
from tesseract import image_to_string


# take horizontal slices
img = Image.open('file_name')
first_slice = img.crop(((10, 0, 50, 10)))
second_slice = img.crop(((20, 0, 50, 20)))
third_slice = img.crop(((30, 0, 50, 30)))

# first.save('file_name.jpg')
# second.save('file_name.jpg')
# third.save('file_name.jpg')

"""
# First , need make horizontal slices
image = cv2.imread("file_name")  # or path to file 
#  need change pixels
first_slice = image[10:500, 500:2000] 
second_slice = image[10:500, 500:2000]
third_slice = image[10:500, 500:2000]
"""

# Second, combining three images
image = cv2.imread('file_name')
image = cv2.resize(image, (0, 0), None, .25, .25) # resized the image to a quarter of its original size

grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# Make the grey scale image have three channels
grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)  # grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

numpy_vertical = np.vstack((image, grey_3_channel))
numpy_horizontal = np.hstack((image, grey_3_channel))

numpy_vertical_concat = np.concatenate((image, grey_3_channel), axis=0)
numpy_horizontal_concat = np.concatenate((image, grey_3_channel), axis=1)

cv2.imshow('Main', image)
cv2.imshow('Numpy Vertical', numpy_vertical)
# cv2.imshow('Numpy Horizontal', numpy_horizontal)
cv2.imshow('Numpy Vertical Concat', numpy_vertical_concat)
# cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)

cv2.waitKey()

"""
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
"""

"""
import cv2
import numpy as np


list_of_img_paths = [path2, path3, path4]
im = cv2.imread(path1)
imstack = cv2.resize(im,(1000, 800))

for path in list_of_img_paths:
    im = cv2.imread(path)
    im = cv2.resize(im,(1000,800))
    imstack = np.hstack(imstack, im)

cv2.imshow('stack', imstack)
cv2.waitKey(0)
"""

"""
# only equally sized Images

im = cv2.imread('1.png')
img = cv2.imread('2.jpg')
both = np.hstack((im, im))
cv2.imshow('imgc', both)
cv2.waitKey(10000)
"""

print(image_to_string(Image.open('test.png')))
print(image_to_string(Image.open('test-english.jpg'), lang='eng'))

