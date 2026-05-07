import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymysql as myc
import matplotlib.pyplot as plt
url="https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,'lxml')
table=soup.find('table',class_='wikitable')
rows=table.find_all('tr')
data=[]
for row in rows[2:]:
    cols=row.find_all('td')
    if cols:
        country=cols[0].text.strip()
        population=cols[1].text.strip()
        Date=cols[3].text.strip()
        world_population=cols[2].text.strip()
        Source=cols[4].text.strip()
        data.append([country,population,Date,world_population,Source])



#data cleaning   
hy=pd.DataFrame(data,columns=[
    'country','population','Date','world_population','Source'
])
hy['population']=hy['population'].str.replace(',','')
hy['world_population']=hy['world_population'].str.replace('%','')
hy['world_population'] = pd.to_numeric(hy['world_population'], errors='coerce')
hy['population']=pd.to_numeric(hy['population'])
hy['population']=hy['population'].fillna(0)
hy['country']=hy['country'].fillna('NA')
hy['country']=hy['country'].str.strip()
hy['Source']=hy['Source'].fillna('NA')
hy['Source']=hy['Source'].str.strip().str.title()
hy.drop_duplicates(inplace=True)
hy.reset_index(drop=True,inplace=True)




#sql connectivity
conn=myc.connect(
    host="localhost",
    user="root",
    password="Abhinav@2004",
    database="webprocessing"
)
cur=conn.cursor()
cur.execute("""
            create table IF NOT EXISTS
            proces(
            id int auto_increment primary key,
            country varchar(300),
            population BIGINT,
            world_population float,
            date text,
            source varchar(300)
            )
            """)
conn.commit()
for i,row in hy.iterrows():
    cur.execute(
        "insert into proces(country,population,world_population,date,source)values(%s,%s,%s,%s,%s)", 
        (row['country'],row['population'],row['world_population'],row['Date'],row['Source'])
    )
conn.commit()
conn.close()



# Exploratory Analysis
top=hy.sort_values(by='population',ascending=False).head(5)
bottom=hy.sort_values(by='population').head(5)
avg=hy['population'].mean()
total=hy['world_population'].sum()


#graphs
x=top['country']
y=top['population']
fig, axs = plt.subplots(2,2, figsize = (12, 8))
fig.suptitle("-- Country Population Analysis Dashboard --", fontsize=20, weight='bold', color='darkblue')
fig.patch.set_facecolor("#E6E6FA")
axs[0,0].bar(x,y,color=['orange','r','g','b','c'])
axs[0,0].set_xlabel('Country',weight='bold',size=10)
axs[0,0].tick_params(axis='x', rotation=25 )
axs[0,0].set_ylabel('Population',weight='bold',size=10)
axs[0,0].set_title('-- Vertical Bar Chart -- ',weight='bold',color='green',size=15)
axs[0,0].grid(alpha=0.2,color='black')
for i in range(len(x)):
    axs[0,0].annotate(text=f"{y[i]}",xy=(x[i] ,y[i]),ha='center',weight='bold',size=8)


a = hy.sort_values(by='population', ascending=False).head(4)
x=a['country']
y=a['population']
axs[0,1].set_title('-- Pie Chart -- ',weight='bold',color='green',size=15,y=1.08) 
axs[0,1].pie(y,labels=x,autopct="%1.0f%%", explode=(0,0.05,0,0),labeldistance=1.2 , shadow = True)

a = hy.sort_values(by='world_population', ascending=False).head(5)
x=a['country']
y=a['world_population']
axs[1,0].plot(x,y,marker='*',mfc='r',mec='black')
axs[1,0].set_title('-- Line Plot -- ',weight='bold',color='green',size=15)
axs[1,0].grid(alpha=0.2,color='black')
axs[1,0].set_xlabel('Country',weight='bold',size=10)
axs[1,0].set_ylabel('World_Population',weight='bold',size=10)
for i in range(len(x)):
    axs[1,0].annotate(text=f"{y[i]}",xy=(x[i],y[i]),weight='bold',ha='left',size=10)


x=bottom['country']
y=bottom['population']
axs[1,1].barh(x,y,color=['orange','r','g','b','c'])
axs[1,1].set_xlabel('Population',weight='bold',size=10)
axs[1,1].set_ylabel('Country',weight='bold',size=10)
axs[1,1].set_title('-- Horizontal Bar Chart -- ',weight='bold',color='green',size=15)
axs[1,1].grid(alpha=0.2,color='black')

plt.tight_layout(pad=2)
plt.show()

