#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


import time
import math
import os


try:
    browser = webdriver.Chrome()
    #говорим webdriver искать каждый элемент в течени 5 секунд
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    element = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    btn = browser.find_element(By.CSS_SELECTOR,"[class='btn btn-primary']")
    btn.click()
    
    def calc(x):
        return str(math.log(abs(12*math.sin(x))))
    math_element = browser.find_element(By.CSS_SELECTOR,'[id="input_value"]')
    x = int(math_element.text)
    input_form = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input_form.send_keys(calc(x))
    button = browser.find_element(By.ID, 'solve')
   
    button.click()

finally:
    time.sleep(5)
    browser.quit   
