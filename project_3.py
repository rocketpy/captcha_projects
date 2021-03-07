# import os
import cv2
import numpy as np
# import Image
# from tesseract import image_to_string


img = cv2.imread("slack_2.jpg")  # or path to file

first_slice = img[0:34, 30:220]
second_slice = img[34:68, 30:200]
third_slice = img[68:102, 30:215]

# print(image.shape)
# print(image.size) # pixels
# print(img.dtype)
# cv2.imshow("Image", img)

im_v = cv2.hconcat([first_slice, second_slice, third_slice])

cv2.imshow("Image", im_v)
cv2.waitKey(0)
cv2.destroyAllWindows()

