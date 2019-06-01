import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def getData(url,second=3):
    # specify the url

    # The path to where you have your chrome webdriver stored:
    webdriver_path = 'C:/Program Files (x86)/Google/ChromeDriver/chromedriver.exe'

    # Add arguments telling Selenium to not actually open a window
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920x1080')

    # Fire up the headless browser
    browser = webdriver.Chrome(executable_path=webdriver_path,
                               options=chrome_options)

    # Load webpage
    browser.get(url)

    # It can be a good idea to wait for a few seconds before trying to parse the page
    # to ensure that the page has loaded completely.
    time.sleep(second)

    # Parse HTML, close browser
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    browser.quit()

    return soup
