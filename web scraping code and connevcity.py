import requests
url="https://quotes.toscrape.com/" 
response=requests.get(url)

# print(response.status_code)
# print(response.text)#shows the code how the coder make the that thing 
# headers willl define the which workbook oor chrome or edge u are using

from bs4 import BeautifulSoup
soup=BeautifulSoup(response.text,'lxml')
# print(soup.title)#gives the tile name
# print(soup.title.text)#gives the title text
# print(soup.text)#gives the data like para of the that thing