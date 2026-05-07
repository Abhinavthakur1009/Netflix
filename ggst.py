import pandas as pd
from bs4 import BeautifulSoup
import requests
import pymysql as myc
import numpy as np

url='https://en.wikipedia.org/wiki/List_of_Netflix_original_programming'
headers={
    "user-agent":'Mozilla/5.0'
}
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,'lxml')
table=soup.find('table',class_='wikitable sortable')
rows=table.find_all('tr')
data=[]
for row in rows[1:]:
    cols=row.find_all('td')
    if cols:
        Title=cols[0].text.strip()
        Genre=cols[1].text.strip()
        Premiere=cols[2].text.strip()
        Seasons=cols[3].text.strip()
        Status=cols[5].text.strip()
        data.append([Title,Genre,Premiere,Seasons,Status])

clean=pd.DataFrame(data,columns=[
    'Title','Genre','Premiere','Seasons','Status',
])
clean['Title']=clean['Title'].str.strip()
clean['Title'] = clean['Title'].str.replace(r'\[.*?\]', '', regex=True).str.replace(r'\d+', '', regex=True)

clean['Genre']=clean['Genre'].str.strip()
clean['Genre']=clean['Genre'].str.replace('-'," ")

clean['Premiere']=clean['Premiere'].str.replace(','," ")
clean['Premiere'] = clean['Premiere'].replace('TBA', np.nan)
clean['Premiere'] = pd.to_datetime(clean['Premiere'], errors='coerce')

clean['Seasons'] = clean['Seasons'].str.extract(r'(\d+)')
clean['Seasons'] = pd.to_numeric(clean['Seasons'], errors='coerce')

clean['Status'] = clean['Status'].str.replace(r"\(.*?\)", "", regex=True)
clean['Status'] = clean['Status'].str.replace(r"\[.*?\]", "", regex=True)
clean['Status'] = clean['Status'].str.replace("-", " ")
clean['Status'] = clean['Status'].str.strip()
clean.to_csv('netflix_data.csv',index=False)

conn=myc.connect(
    host='localhost',
    user='root',
    password='Abhinav@2004',
    database='project'
)
cur=conn.cursor()
cur.execute("""
create table if not exists net(
            id int auto_increment primary key,
            Title varchar(150),
            Genre varchar(100),
            Premiere date,
            Seasons int,
            Status varchar(50)
            )
""")
conn.commit()

for i,row in clean.iterrows():
    cur.execute('insert into net(Title,Genre,Premiere,Seasons,Status)values(%s,%s,%s,%s,%s)',
    (
        row['Title'],
        row['Genre'], 
        None if pd.isna(row['Premiere']) else row['Premiere'],
        None if pd.isna(row['Seasons']) else row['Seasons'],
        row['Status'])
    )
conn.commit()



 
