from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("http://www...")

try:
    elem = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "some_elem")))
finally:
    driver.quit()
    
    
# Some solution when a reCaptcha in a login page
def check_exist_elem(xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    login_btn_xpath = 'login_button_xpath'
    while True:
        # Here can solve recaptcha during this period and hit the login button.
        if check_exists_by_xpath(login_btn_xpath) is False:
            break

            
#  Text-based, text-in-image CAPTCHAs

# to run script
# python3 captcha_resolver.py captcha.jpg

import sys
import argparse
import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image
from subprocess import check_output


def resolve_captcha(path):
    check_output(['convert', path, '-resample', '600', path])
    return pytesseract.image_to_string(Image.open(path))

if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('path', help = 'Path to file')
    args = argparser.parse_args()
    path = args.path
    captcha_text = resolve(path)
    print('Result: ', captcha_text)
    
    
# Origin taked from:
# https://cloudsek.com/how-to-bypass-captchas-easily-using-python-and-other-methods/
    
import time
from selenium import webdriver


dataset = {'     *       *      *      *      *      ******* ': 'J',
           '*******      *      *      *      *      *      *': 'L',
           '********  *  **  *  **  *  **  *  **  *  * ** ** ': 'B',
           '*       *       *       ****  *     *     *      ': 'Y',
           '*      *      *      ********      *      *      ': 'T',
           ' ***** *     **     **     **     **     * *   * ': 'C',
           '********  *  **  *  **  *  **     **     **     *': 'E',
           '********     **     **     **     **     * ***** ': 'D',
           '*     **     **     *********     **     **     *': 'I',
           ' ***** *     **     **     **     **     * ***** ': 'O',
           '******* *       *       *     *     *     *******': 'M',
           '******* *       *       *       *       * *******': 'N',
           '********  *   *  *   *  *   *      *      *      ': 'F',
           ' **  * *  *  **  *  **  *  **  *  **  *  * *  ** ': 'S',
           ' ***** *     **     **     **   * **    *  **** *': 'Q',
           '*******   *     * *    * *   *   *  *   * *     *': 'K',
           '     **   **   ** *  *   *   ** *     **       **': 'A',
           '******       *      *      *      *      ******* ': 'U',
           '*******   *      *      *      *      *   *******': 'H',
           '**       **       **       *    **   **   **     ': 'V',
           '*     **    ***   * **  *  ** *   ***    **     *': 'Z',
           '********  *   *  *   *  *   *  *   *  *    **    ': 'P',
           '*     * *   *   * *     *     * *   *   * *     *': 'X',
           ' ***** *     **     **     **   * **   * * *  ** ': 'G',
           '********  *   *  *   *  *   *  **  *  * *  **   *': 'R',
           '*******     *     *     *       *       * *******': 'W'}
    

def group_captcha_string(word_pos):
    
    captcha_string = ''
    
    for i in range(len(word_pos[0])):
        temp_list = []
        temp_string = ''

        for j in range(len(word_pos)):
            val = word_pos[j][i]
            temp_string += val

            if val.strip():
                temp_list.append(val)

        if temp_list:
            captcha_string += temp_string
        else:
            captcha_string += 'sp'

    return captcha_string.split("spsp")

# create client
client = webdriver.Chrome()
client.get("http://keith-wood.name/realPerson.html")
time.sleep(3)

# indexing text
_get = lambda _in: {index: val for index, val in enumerate(_in)}

# get text from html tag
captcha = client.find_element_by_css_selector('form [class="realperson-text"]').text.split('\n')

word_position = list(map(_get, captcha))

# group text
text = group_captcha_string(word_position)

# get text(test)
captcha_text = ''.join(list(map(lambda x: dataset[x] if x else '', text)))
print("Captcha:", captcha_text)


