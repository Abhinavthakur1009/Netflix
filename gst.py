import pandas as pd
from bs4 import BeautifulSoup
import requests
import pymysql as myc

url="https://en.wikipedia.org/wiki/List_of_Netflix_original_programming"
headers = {
    "User-Agent": "Mozilla/5.0" 
}
# print('successfully connected to the url')
response=requests.get(url, headers=headers)
soup=BeautifulSoup(response.text,'lxml')
table=soup.find('table',class_='wikitable sortable')
row=table.find_all('tr')
