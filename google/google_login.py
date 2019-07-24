from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Firefox()

def startService():
    url = 'https://www.google.com'
    browser.get(url)
    browser.find_element_by_css_selector('#gb_70').click()
    browser.find_element_by_css_selector('#identifierId').send_keys('account@gmail.com'+Keys.RETURN)
    #browser.find_element_by_css_selector('.I0VJ4d > div:nth-child(1) > input:nth-child(1)').send_keys('password' + Keys.RETURN)
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.I0VJ4d > div:nth-child(1) > input:nth-child(1)'))
        )
        time.sleep(1)
        element.send_keys('password' + Keys.RETURN)
        time.sleep(5)
    except NoSuchElementException:
        print('NoSuchElementException')
    finally:
        browser.close()

if __name__ == '__main__':
    startService()