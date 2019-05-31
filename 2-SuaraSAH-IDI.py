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
url2 = 'https://www.bps.go.id/dynamictable/2017/05/04/1241/indeks-demokrasi-indonesia-idi-menurut-provinsi-2009-2017.html'

# The path to where you have your chrome webdriver stored:
webdriver_path = 'C:/Program Files (x86)/Google/ChromeDriver/chromedriver.exe'

# Add arguments telling Selenium to not actually open a window
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')

# Fire up the headless browser
browser = webdriver.Chrome(executable_path=webdriver_path,
                           options=chrome_options)
browser2 = webdriver.Chrome(executable_path=webdriver_path,
                           options=chrome_options)
# Load webpage
browser.get(url)
browser2.get(url2)

# It can be a good idea to wait for a few seconds before trying to parse the page
# to ensure that the page has loaded completely.
time.sleep(10)

# Parse HTML, close browser
soup = BeautifulSoup(browser.page_source, 'html.parser')
soup2 = BeautifulSoup(browser2.page_source,'html.parser')
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

# find results within table
result_value    = soup2.find('table', attrs={'id': 'tableRightBottom'})
rows_value      = result_value.find_all('tr')
value = []

for id, r in enumerate(rows_value[:-1]):
    # find all columns per result
    data_value = rows_value[id].find_all('td', attrs={'class': 'datas'})

    # check that columns have data
    if len(data_value) == 0:
        continue

    # write columns to variables
    #wilayah = data_wilayah[0].find('b').getText()

    nilai = data_value[-1].getText()
    # Remove decimal point
    # nilai = nilai.replace('.','')
    # Cast Data Type Integer
    nilai = float(nilai)
    value.append(nilai)


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
        tsah = data[5].find('span', attrs={'class':'tsah'}).getText()
        # Remove decimal point
        #satu = satu.replace('.','')
        #dua = dua.replace('.','')
        tiga = tiga.replace('.', '')
        tsah = tsah.replace('.','')

        # Cast Data Type Integer
        #satu = int(satu)
        #dua = int(dua)
        tiga = float(tiga)
        tsah = float(tsah)
        perbandingan = tiga/(tiga+tsah)*100

        array.append(wilayah)
        #jokowi.append(satu)
        #prabowo.append(dua)
        total2019.append(perbandingan)

# Convert to numpy
np_array = np.array(array)
#np_jokowi= np.array(jokowi)
#np_prabowo= np.array(prabowo)
np_total = np.array(total2019)
np_value = np.array(value)

# # Naming label
# plt.xlabel('provinsi')
# plt.ylabel('perolehan suara')
#
# # styling x,y value
# plt.xticks(rotation=30,ha='right')
# plt.yticks(np.arange(np_total.min(),np_total.max(),4000000))
#
# # plot data
# #plt.plot(np_array,np_jokowi,color='red',label='Jokowi 2019',linestyle='--', marker='o')
# #plt.plot(np_array2,np_jokowi2,color='black',label='Jokowi 2014',linestyle='--', marker='o')
# #plt.plot(np_array,np_prabowo,color='blue',label='Prabowo 2019',linestyle='--', marker='o')
# #plt.plot(np_array2,np_prabowo2,color='green',label='Prabowo 2014',linestyle='--', marker='o')
# plt.plot(np_array,np_total,color='orange',label='Total Suara Sah 2019',linestyle='--', marker='o')
# plt.legend(loc='upper right')
# plt.yscale('linear')
# plt.show()

# # plot data
# fig,ax = plt.subplots(figsize=(10,5))
# # fig,ax = plt.subplots()
# # print(ax)
# pos = list(range(len(np_array)))
# width = 0.25
#
# # print(ind-width/2)
#
# rects1 = ax.bar(pos,np_total,width,color='red',label='Persentase Suara SAH')
# rects2 = ax.bar([p + width for p in pos],np_value,width,color='blue',label='Indeks Demokrasi Indonesia')
# # ax.set_xticks(ind)
# ax.set_xticks([p + 0.5 * width for p in pos])
# ax.set_xticklabels(np_array)
# # # Naming label
# plt.xlabel('provinsi')
# plt.ylabel('perolehan suara')
# # Set Text Value
# def autolabel(rects):
#     """
#     Attach a text label above each bar displaying its height
#     """
#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width()/2., height,
#                 '%d' % int(height),
#                 ha='center', va='bottom')
#
# autolabel(rects1)
# autolabel(rects2)
#
# print (value)
# # # styling x,y value
# # plt.xticks(rotation=30,ha='right')
# plt.yticks(np.arange(np_total.min(),np_total.max(),4000000))
# plt.xticks(rotation=30,ha='right')
# plt.legend(loc='upper right')
# plt.yscale('linear')
#
#
# plt.show()


df =pd.DataFrame({'x':np_array,'persentase suara sah':np_total,'Index Demokrasi Indonesia':np_value})

plt.plot( 'x', 'persentase suara sah', data=df, marker='o',  markersize=4,  linewidth=1)
plt.plot( 'x', 'Index Demokrasi Indonesia', data=df, marker='o',  markersize=4,  linewidth=1)

plt.xticks(rotation=30,ha='right')
plt.legend(loc='upper right')

plt.show()