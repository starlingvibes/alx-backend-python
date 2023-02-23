from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromedriver = "/chromedriver"

option = webdriver.ChromeOptions()

option.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

s = Service(chromedriver)

browser = webdriver.Chrome(service=s, options=option)

browser.get("https://github.com/starlingvibes")

counter = 0
while counter < 5:
    browser.get(browser.current_url())
    counter += 1

browser.quit()
