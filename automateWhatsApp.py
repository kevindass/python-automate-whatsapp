# https://dev.to/visheshdvivedi/send-bulk-whatsapp-messages-in-python-automate-whatsapp-using-python-ipo
import time
import os
import platform
from colorama import init, Fore
from termcolor import colored  # pip install -U termcolor
# pip install -U pandas & pip install -U openpyxl ( openpyxl for .xlsx files)
import pandas as pd
import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

FILE_LOC = "FlatOwnersV1.xlsx"
NAME = 'Name'
PHONENUMBER = 'Phone Number'
MESSAGE = 'Message'
commonMessage = ''
REPLACENAME = '{{name}}'
URL = 'https://web.whatsapp.com/'
WAITER_ELEMENT = "landing-title _3-XoE"
#PHONE_NUMER_INPUT = "//*[@id='side']/div[1]/div/label/div/div[2]"
PHONE_NUMER_INPUT = "//*[@id='side']//div[@title='Search input textbox']"
#PERSON_DIV = "//*[@id='pane-side']/div[1]/div/div/div[1]/div/div/div[1]/div/div/img"
#MESSAGE_INPUT = "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]"
MESSAGE_INPUT = "//*[@id='main']/footer//p[@class='selectable-text copyable-text']"

SEND_BUTTON = "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
waiter = WebDriverWait(driver, 10)
data = []


def printData(message, type):
    if type == 'INFO':
        print('[' + colored(datetime.datetime.now().strftime('%H:%M:%S'),
              'cyan') + '][' + colored('INFO', 'green') + '] ' + message)
    elif type == 'WARNING':
        print('[' + colored(datetime.datetime.now().strftime('%H:%M:%S'),
              'cyan') + '][' + colored('WARNING', 'yellow') + '] ' + message)
    elif type == 'ERROR':
        print('[' + colored(datetime.datetime.now().strftime('%H:%M:%S'),
              'cyan') + '][' + colored('ERROR', 'red') + '] ' + message)


def read_data_from_excel(commonMessage):
    try:
        df = pd.read_excel(FILE_LOC)
        printData("Retrieving data from excel", 'INFO')
    except:
        printData("Excel 'data.xlsx' not found", 'ERROR')
    printData("Found {0} messages to be send".format(len(df.index)), 'INFO')
    for i in df.index:
        # if '+' not in str(df[PHONENUMBER][i]):
        #     number = '+91' + str(df[PHONENUMBER][i])
        # else:
        #     number = str(df[PHONENUMBER][i])
        if i == 0:
            commonMessage = df['MESSAGE'][i]
        output = {
            'Name': df['NAME'][i],
            'PhoneNumber': df['PHONENUMBER'][i],
            # 'Message': df['MESSAGE'][i].replace(REPLACENAME, df['NAME'][i])
            'Message': commonMessage
        }
        data.append(output)
        # print("Print Data below")
        # print(data)


def send_whatsapp_message():
    global driver
    driver.get(URL)
    printData("Loading site...", 'INFO')
    # waiter.until(EC.title_is("WhatsApp"))
    waiter.until(EC.title_contains("WhatsApp"))
    printData("Site loaded successfully...", 'INFO')
    printData("Waiting for user to log in using WhatsApp Web", 'INFO')
    waitCounter = 0
    while 1:
        try:
            waiter.until(EC.presence_of_element_located(
                (By.XPATH, "//canvas[@aria-label='Scan me!']")))
            waitCounter += 1
            if waitCounter % 1000 == 0:
                printData("Waiting for user to log in...", 'WARNING')
        except:
            printData("Logged in to WhatsApp", 'INFO')
            break

    for entry in data:
        if entry['Name'] == 'DUMMY':
            continue
        else:
            #driver.find_element_by_xpath(PHONE_NUMER_INPUT).send_keys(
            #    str(entry['PhoneNumber']))
            driver.find_element("xpath",PHONE_NUMER_INPUT).send_keys(
                str(entry['PhoneNumber']))
            time.sleep(5)
            #driver.find_element_by_xpath(
            #    PHONE_NUMER_INPUT).send_keys(Keys.ENTER)
            driver.find_element("xpath",PHONE_NUMER_INPUT).send_keys(Keys.ENTER)
            time.sleep(5)
            #driver.find_element_by_xpath(
            #    MESSAGE_INPUT).send_keys(str(entry['Message']))
            driver.find_element("xpath",
                MESSAGE_INPUT).send_keys(str(entry['Message']))
            time.sleep(5)
            #driver.find_element_by_xpath(SEND_BUTTON).click()
            driver.find_element("xpath",SEND_BUTTON).click()
            time.sleep(5)
            printData("Successfully send message to {0}, name: {1}".format(
                str(entry['PhoneNumber']), str(entry['Name'])), 'INFO')


if __name__ == '__main__':
    # Initialize colorama
    init()

    # Clear the screen
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    # Display ASCII art
    print("WhatsApp Python")
    print(Fore.CYAN + "\nCreated By:" + Fore.RESET +
          " Vishesh Dvivedi [All About Python]\n")
    print(Fore.YELLOW + "GitHub: " + Fore.RESET + "   visheshdvivedi")
    print(Fore.YELLOW + "Youtube:" + Fore.RESET + "   All About Python")
    print(Fore.YELLOW + "Instagram:" + Fore.RESET + " @itsallaboutpython")
    print(Fore.YELLOW + "Blog Site:" + Fore.RESET +
          " itsallaboutpython.blogspot.com\n")

    # Read data from 'data.xlsx' file
    read_data_from_excel(commonMessage)

    # Send whatsapp message
    send_whatsapp_message()

    # Close chromedriver
    driver.close()
