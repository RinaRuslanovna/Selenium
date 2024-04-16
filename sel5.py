#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


import time

link="http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input_1 = browser.find_element(By.CSS_SELECTOR," [placeholder='Input your first name']")
    input_1.send_keys("RINA")
    input_2=browser.find_element(By.CSS_SELECTOR," [placeholder='Input your last name']")
    input_2.send_keys("Enikeeva")
    input_3=browser.find_element(By.CSS_SELECTOR," [placeholder='Input your email']")
    input_3.send_keys('UFA')
    
    button=browser.find_element(By.CSS_SELECTOR,".btn-default")
    button.click()


finally:
    time.sleep(30)
    browser.quit()

