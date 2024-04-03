#Gidilen bir web sitesinin radyo düğmesi ve chexbox'un tıklı olup olmadığını sorgulayan selenium kodları.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://tomspizzeria.b4a.app/")
time.sleep(2)
orta_boy=driver.find_element(By.CSS_SELECTOR, "input[value='Orta']")
zeytin=driver.find_element(By.CSS_SELECTOR, "input[value='zeytin']")
mantar=driver.find_element(By.CSS_SELECTOR, "input[value='mantar']")
print(orta_boy.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())
orta_boy.click()
zeytin.click()
mantar.click()
print(orta_boy.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())
time.sleep(2)
driver.quit()
