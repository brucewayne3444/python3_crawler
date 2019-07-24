import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

def startService():
    try:
        url = 'https://www.google.com'
        browser.get(url)
        elem = browser.find_element_by_css_selector('.gLFyf')
        elem.send_keys('bruce')
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
    finally:
        browser.close()
    pass

if __name__ == '__main__':
    startService()