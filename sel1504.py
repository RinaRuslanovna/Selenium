from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


import time
from selenium.webdriver.support.ui import Select
try:
    link='https://suninjuly.github.io/selects1.html'
    browser= webdriver.Chrome()
    browser.get(link)
    element=browser.find_element(By.ID,'num1')
    element1=browser.find_element(By.ID,'num2')
    a=element.text
    a=int(a)
    b=element1.text
    b=int(b)
    z=a+b
    select = Select(browser.find_element(By.TAG_NAME,"select"))
    time.sleep(30)
    select.select_by_value(str(z))
    button=browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
    button.click()
finally:
    time.sleep(10)
    browser.quit()