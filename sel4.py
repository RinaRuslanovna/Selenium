#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME,'input')
    for i in elements:
        i.send_keys("gggggggggggggggggggggggggggggggggggggggggggggggggggg")
    buttom=browser.find_element(By.CSS_SELECTOR,'.btn-default')
    button.click()


finally:
    time.sleep(30)
    browser.quit()

