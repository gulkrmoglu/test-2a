from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# WebDriver'ı başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://www.apple.com/")
time.sleep(3)
driver.switch_to.new_window("tab")
time.sleep(3)
#driver.switch_to.new_window("windows")
#time.sleep(3)
driver.get("https://www.tesla.com/")
time.sleep(3)
driver.quit()