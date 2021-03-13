import os
import cv2
import numpy as np
from PIL import Image
import pytesseract


img = cv2.imread("slack_2.jpg")  # or path to file

first_slice = img[0:34, 30:220]
second_slice = img[34:68, 30:200]
third_slice = img[68:102, 30:215]

# print(image.shape)
# print(image.size) # pixels
# print(img.dtype)
# cv2.imshow("Image", img)

im_v = cv2.hconcat([first_slice, second_slice, third_slice])

# result = pytesseract.image_to_string(im_v)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'
# print(pytesseract.image_to_string(Image.open(im_v), lang="rus"))
# print(result)

# save image to file
# cv2.imwrite('new_image.jpg', im_v)
print(pytesseract.image_to_string(cv2.imread(im_v), lang="rus"))

# Adding custom options
custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(img, config=custom_config)

cv2.imshow("Image", im_v)
cv2.waitKey(0)
cv2.destroyAllWindows()

