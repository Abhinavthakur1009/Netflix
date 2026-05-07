from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://en.wikipedia.org/wiki/Table_tennis"
header={
        "user-agent":'Mozilla/5.0'

}
r=requests.get(url,headers=header)
soup=BeautifulSoup(r.text,'lxml')
tab=soup.find('table',class_='wikitable')
a=tab.findAll('tr')
data=[]
for row in a[1:]:
    cols=row.find_all('td')
    if cols:
        Title=cols[0].text.strip()
        Genre=cols[1].text.strip()
        Premiere=cols[2].text.strip()
        Seasons=cols[3].text.strip()
        Status=cols[5].text.strip()
        data.append([Title,Genre,Premiere,Seasons,Status])
all=pd.DataFrame(data,columns=
                 ['Title','Genre','Premiere','Seasons','Status']
                 )
print(all.head())
