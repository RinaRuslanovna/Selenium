#Webdriver - это и есть набор команд для управления браузером
from selenium import webdriver




#импортируем класс By , который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By




import time






link ="https://easysmarthub.ru/contact/"




try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input_1 = browser.find_element(By.NAME, "your_name")
    input_1.send_keys("RINA")
    input_3 = browser.find_element(By.CSS_SELECTOR, "[name='your_email']")
    input_3.send_keys("RINA")
    input_4=browser.find_element(By.CSS_SELECTOR,"[name='your_subject']")
    input_4.send_keys("RINA")
    input_5=browser.find_element(By.CSS_SELECTOR,"[name='your_message']")
    input_5.send_keys("RINA")       
    button=browser.find_element(By.CSS_SELECTOR,"button[type='checkbox']")
    button.click()
    
finally:
    time.sleep(12)
    #закрывает браузер после всех манипуляций даже если была ошибка
    browser.quit()
   



