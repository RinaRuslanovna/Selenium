#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import Select


import time

import os


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")
    
    btn = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
    btn.click()
    message=browser.find_element(By.ID,'verify_message')
    assert 'successful' in message.text
finally:
    time.sleep(10)
    browser.quit    