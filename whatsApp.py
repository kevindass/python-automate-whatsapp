import sys
import time
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ---------------------
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-webgl")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# ---------------------
# sourec https://www.youtube.com/watch?v=eela1UYObWE

# below code is to skip whatsapp QR code everytime we run pythin code
# options = webdriver.ChromeOptions()
# options.add_argument(
#     r'--user-data-dir=C:\Users\kdass\AppData\Local\Google\Chrome\User Data\Default')
# options.add_argument('--profile-directory=Default')

# # # create selenium webdriver instnace
chromeBrowser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))

chromeBrowser.get('https://web.whatsapp.com/')

# # #----------------------
# # # TEST
# # #----------------------
# # # https://www.geeksforgeeks.org/whatsapp-using-python/
wait = WebDriverWait(chromeBrowser, 90)
# # #----------------------

# # # Part-1
# target = '"LB Shakti Dash"'
# x_arg = '//span[contains(@title,' + target + ')]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()

# string = "Message sent using Python!!!"
# # # <div title="Type a message" role="textbox" class="_13NKt copyable-text selectable-text" contenteditable="true" data-tab="10" dir="ltr" spellcheck="true"></div>
# inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="10"]'

# input_box = wait.until(EC.presence_of_element_located((
#     By.XPATH, inp_xpath)))
# for i in range(1):
#     input_box.send_keys(string + Keys.ENTER)
#     time.sleep(1)

# # #----------------------
# # #Part-2
# # # <span data-testid="chat" data-icon="chat" class=""><svg viewBox="0 0 24 24" width="24" height="24" class="">
# x_arg = '//span[@class=""][@data-icon="chat"]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()

# time.sleep(1)
# # # ----------------------
# # # Part-3
# chromeBrowser.get('http://api.whatsapp.com/send?phone=+919483958407')
# wait = WebDriverWait(chromeBrowser, 90)

# # # <a class="_36or _2y_c _2z0c _2z07" href="https://web.whatsapp.com/send?phone=+91+94839+58407" title="Share on WhatsApp" id="action-button">Continue to Chat</a>
# x_arg = '//a[@class="_36or _2y_c _2z0c _2z07"][@id="action-button"]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()

# # # <a class="_36or" href="https://web.whatsapp.com/send?phone=+91+94839+58407">use WhatsApp Web</a>
# x_arg2 = '//a[contains(@href,"web.whatsapp.com")]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg2)))
# group_title.click()

# time.sleep(60)
# # #----------------------
# target = '"GM Daffodils flat owners"'
# x_arg = '//span[contains(@title,' + target + ')]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()

# # # # <span data-testid="menu" data-icon="menu" class=""><svg viewBox="0 0 24 24" width="24" height="24" class="">
# # # # //*[@id="main"]/header/div[3]/div/div[2]/div/div/span
# # # # coudl not use just data-icon="menu" class="" as right side panel also has same menu
# x_arg = '//*[@id="main"]/header/div[3]/div/div[2]/div/div/span[@class=""][@data-icon="menu"]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()

# # # # <div class="_2oldI dJxPU" role="button" aria-label="Group info">Group info</div>
# x_arg = '//div[@class="_2oldI dJxPU"][@aria-label="Group info"]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()

# # # # //*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/button/div[2]
# x_arg = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div[2]/button/div[2]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()

# # # # <span dir="auto" title="+91 94481 21210" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">+91 94481 21210</span>
# contactNo = '"+91 94481 21210"'
# x_arg = '//span[contains(@title,' + contactNo + ')]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()

# time.sleep(60)
# ----------------------

chromeBrowser.quit()

# https://stackoverflow.com/questions/57480789/how-to-determine-if-whatsapp-contact-search-find-results-with-selenium-python
# https://dev.to/visheshdvivedi/send-bulk-whatsapp-messages-in-python-automate-whatsapp-using-python-ipo
