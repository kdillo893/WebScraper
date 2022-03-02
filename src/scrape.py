import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IEOptions

#TODO Figure out why options isn't working; "ignore local proxy" attribute missing
# options = ChromeOptions()
# options._ignore_local_proxy=False
# options.add_argument("start-maximized")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#following selenium webpage tutorial
driver.get("https://www.google.com/")
assert(driver.title == "Google")
driver.implicitly_wait(0.5)
searchbox = driver.find_element(By.NAME, "q")
searchbutton = driver.find_element(By.NAME, "btnK")

searchbox.send_keys("Selenium")
searchbutton.click()
assert(driver.find_element(By.NAME, "q").get_attribute("value") == "Selenium")

driver.quit()