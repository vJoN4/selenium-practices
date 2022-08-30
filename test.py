from selenium import webdriver

_Driver = webdriver.Edge("./msedgedriver.exe")

_Driver.get("http://www.youtube.com")
# oDrvier.close()
