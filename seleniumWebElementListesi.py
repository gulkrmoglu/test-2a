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
driver.get("https://www.imdb.com")
time.sleep(2)

driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']").click()
time.sleep(2)  
film_isimleri=driver.find_elements(By.XPATH, "//table/tbody//tr//td[@class='titleColumn']")
                           
time.sleep(2)

for i in range(20):
    print(film_isimleri[i].text)
    time.sleep(2)

driver.quit(2)

