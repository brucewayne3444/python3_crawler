from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
from pyquery import PyQuery as pq

browser = webdriver.Firefox()
browser.maximize_window()
wait = WebDriverWait(browser, 10)

def get_info():
    try:
        CSS_SELECTOR = '.gl-warp'
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))
        )
        scroll_step = 600
        for i in range(10):
            browser.execute_script("window.scrollTo(%d, %d);" % (i * scroll_step, (i + 1) * scroll_step))
            #time.sleep(0.1)
        html = browser.page_source
        doc = pq(html)
        items = doc(CSS_SELECTOR+ ' li').items()
        for item in items:
            info = {
                'name': item.find('.p-name em').text(),
                'price': item.find('.p-price i').text(),
                'commit': item.find('.p-commit a').text(),
                'shop': item.find('.p-shopnum').text(),
                'img': item.find('.p-img img').attr('src')
            }
            print(info)
            #print(item.find('.p-name em').text())
    except TimeoutException:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'timeout')

def next_page(page_total, page_now=1):
    try:
        page_next = page_now+1
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'next page', page_next)
        CSS_SELECTOR = 'input.input-txt:nth-child(2)'
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))
        )
        element.send_keys(str(page_next)+Keys.RETURN)
        get_info()
        page_now = page_next
        if page_total <= page_now:
            print('the end.')
            return
    except WebDriverException:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'next_page error')
    next_page(page_total, page_now)

def search():
    try:
        CSS_SELECTOR = '#key'
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))
        )
        element.send_keys('尼采'+Keys.RETURN)
        CSS_SELECTOR = '.p-skip > em:nth-child(1) > b:nth-child(1)'
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))
        )
        page_total = int(element.text)
        print('total page', page_total)
        get_info()
        next_page(page_total)
    except WebDriverException:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'search error')
    finally:
        browser.close()

def startService():
    try:
        url = 'https://www.jd.com'
        browser.get(url)
        search()
    except WebDriverException:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'error')

if __name__ == '__main__':
    startService()