from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# path = r'C:\Users\kdass\Documents\selenium\chromeWebDriver\chromedriver.exe'
# browser = webdriver.Chrome(path)

options = Options()
options.add_argument("start-maximized")

# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element(By.NAME, 'p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
