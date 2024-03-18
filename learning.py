from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
service = Service(chrome_driver_path) 
driver = webdriver.Chrome(service=service) 
url = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(url) 
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a" ) 
print (article_count.text) 

driver.close()

