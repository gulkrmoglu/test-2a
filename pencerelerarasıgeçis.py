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
print(driver.title)
apple=driver.current_window_handle
driver.switch_to.new_window("tab")
driver.get("https://www.tesla.com/")
time.sleep(3)
print(driver.title)
tesla=driver.window_handles[1]
driver.switch_to.window(apple)
print(driver.title)
time.sleep(2)
driver.switch_to.window(tesla)
time.sleep
driver.switch_to.window(apple)
time.sleep(2)
driver.quit()

