from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# * https://selenium-python.readthedocs.io/locating-elements.html

_Driver = webdriver.Edge("./msedgedriver.exe")

_Driver.get('https://github.com/login')

time.sleep(5)

user = _Driver.find_element(By.ID, 'login_field')
password = _Driver.find_element(By.ID, 'password')

user.send_keys('test@gmail.com')
password.send_keys('#123456')

# user.send_keys(Keys.ENTER)
