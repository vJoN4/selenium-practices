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

li_list = _Driver.find_elements(By.TAG_NAME, 'li')
by_hours = None

for li in li_list:
  if (li.text == 'Por horas'):
    by_hours = li

if (by_hours != None):
  by_hours.click()
else:
  print("Not found")

time.sleep(3)

_Driver.quit()