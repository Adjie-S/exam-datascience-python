# import libraries
from bs4 import BeautifulSoup
# import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# specify the url
url = 'https://kawalpemilu.org/#pilpres:0'

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
time.sleep(10)

# Parse HTML, close browser
soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup)
pretty = soup.prettify()
browser.quit()
# find results within table
results = soup.find('table',{'class':'table'})
rows = results.find_all('tr',{'class':'row'})
array = []
#jokowi = []
#prabowo = []
total2019 = []

# print(rows)
for r in rows:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
# write columns to variables
    wilayah = data[1].find('a').getText()
    if wilayah != 'KALIMANTAN UTARA':
        #satu = data[2].find('span', attrs={'class':'abs'}).getText()
        #dua = data[3].find('span', attrs={'class': 'abs'}).getText()
        tiga = data[4].find('span', attrs={'class': 'sah'}).getText()
        # Remove decimal point
        #satu = satu.replace('.','')
        #dua = dua.replace('.','')
        tiga = tiga.replace('.', '')
        # Cast Data Type Integer
        #satu = int(satu)
        #dua = int(dua)
        tiga = int(tiga)
        array.append(wilayah)
        #jokowi.append(satu)
        #prabowo.append(dua)
        total2019.append(tiga)

# Convert to numpy
np_array = np.array(array)
#np_jokowi= np.array(jokowi)
#np_prabowo= np.array(prabowo)
np_total = np.array(total2019)

# Naming label
plt.xlabel('provinsi')
plt.ylabel('perolehan suara')

# styling x,y value
plt.xticks(rotation=30,ha='right')
plt.yticks(np.arange(np_total.min(),np_total.max(),4000000))

# plot data
#plt.plot(np_array,np_jokowi,color='red',label='Jokowi 2019',linestyle='--', marker='o')
#plt.plot(np_array2,np_jokowi2,color='black',label='Jokowi 2014',linestyle='--', marker='o')
#plt.plot(np_array,np_prabowo,color='blue',label='Prabowo 2019',linestyle='--', marker='o')
#plt.plot(np_array2,np_prabowo2,color='green',label='Prabowo 2014',linestyle='--', marker='o')
plt.plot(np_array,np_total,color='orange',label='Total Suara Sah 2019',linestyle='--', marker='o')
plt.legend(loc='upper right')
plt.yscale('linear')
plt.show()