# import os
import cv2
import numpy as np
# import Image
# from tesseract import image_to_string


image = cv2.imread("slack_2.jpg")  # or path to file
print(image.shape)
# print(image.size) # pixels
# print(img.dtype)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
