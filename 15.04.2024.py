from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import Select

import time
import math


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/alert_accept.html')
    button=browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept() # принять
    x=browser.find_element(By.ID,'input_value')
    x = x.text
    print(x)
    def calc(x):
         return (math.log(abs(12*math.sin(x))))
    element=browser.find_element(By.ID,'answer')
    element.send_keys(str(calc(x)))
    button=browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    button.click()
finally:
    time.sleep(10)
    browser.quit    