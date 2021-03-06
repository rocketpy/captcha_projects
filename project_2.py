import cv2
import numpy as np
import pytesseract
from word2number import w2n
from selenium import webdriver
# from fake_useragent import UserAgent


# pip install word2number

# example
# print(w2n.word_to_num('one hundred thirty-five'))
# result: 135

URL = "https://translate.google.com.ua/?hl=ru&tab=rT"  # for separate words
PATH = "C:\..\chromedriver.exe" 
driver = webdriver.Chrome(PATH) 
image = 'file_name'

def clean_image(image):
    #  remove the noise from image
    img = cv2.imread(image_path)
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((4, 4), np.uint8), iterations=1)
    img = cv2.medianBlur(img, 3)
    img = cv2.medianBlur(img, 3)
    img = cv2.medianBlur(img, 3)
    img = cv2.medianBlur(img, 3)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # cv2.imwrite('res.png', img)
    result = pytesseract.image_to_string(img)
    return result

def get_separ_words(wrd):
    try:
        driver.get(URL)
        time.sleep(5)
        search = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')  # input field                                 
        search.send_keys(wrd)  # image_word is a string with a word
        time.sleep(5)
        search = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]')  # output field
        # need add result !!!
        #  'Perhaps you meant:'
        #  '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[4]/div/div/div/span/html-blob/b/i'
    
        perhaps = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[4]/div/div/div/span/html-blob/b/i').text
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        
   return result 
def get_result(words):
        result = w2n.word_to_num(words)
        return result    
    
def main():
    print(get_result(get_separ_words(clean_image(image))))
    
if __name__ == '__main__':
    main()

    
