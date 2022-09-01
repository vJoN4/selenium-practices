from selenium import webdriver
from selenium.webdriver.common.by import By
import time

_Driver = webdriver.Edge("./msedgedriver.exe")

_Driver.get('https://www.clima.com/')

time.sleep(3)

mx = _Driver.find_element(By.CLASS_NAME, 'm_list_countrys_mx')
mx.click()

time.sleep(3)

location = _Driver.find_element(By.ID, 'geoposition')
location.click()

time.sleep(3)

by_hours = _Driver.find_element(By.XPATH, '/html/body/div[5]/div/div[4]/div/section[4]/section/div/article/section/ul/li[2]')
by_hours.click()

time.sleep(3)

_Driver.quit()