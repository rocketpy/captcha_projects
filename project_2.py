import cv2
import numpy as np
import pytesseract
from word2number import w2n
from selenium import webdriver
from fake_useragent import UserAgent


# pip install word2number

# example
# print(w2n.word_to_num('one hundred thirty-five'))
# result: 135

URL = "https://translate.google.com.ua/?hl=ru&tab=rT"  # for separate words


#  remove the noisy dots from image
img = cv2.imread(image_path)
_, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((4, 4), np.uint8), iterations=1)
img = cv2.medianBlur(img, 3)
img = cv2.medianBlur(img, 3)
img = cv2.medianBlur(img, 3)
img = cv2.medianBlur(img, 3)
img = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imwrite('res.png', img)

print(pytesseract.image_to_string('res.png'))


driver.get(URL)
driver.

