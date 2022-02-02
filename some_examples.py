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
