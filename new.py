import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymysql as myc
import matplotlib.pyplot as plt
url="https://en.wikipedia.org/wiki/List_of_countries_by_oil_extraction"
headers = {
    "User-Agent": "Mozilla/5.0"
}
respone=requests.get(url,headers=headers)
soup=BeautifulSoup(respone.text,'lxml')
table=soup.find('table',class_= 'wikitable')
row=table.find_all('tr')
data=[]
for rows in row[2:]:
    cols=rows.find_all('td')
    if cols:
        country=cols[0].text.strip()
        crud_oil=cols[1].text.strip()
        continent=cols[2].text.strip()
        data.append([country,crud_oil,continent])

all=pd.DataFrame(data,columns=[
    'country','crud_oil','continent'
])
all['crud_oil'] = all['crud_oil'].str.replace(',', '', regex=False)
all['crud_oil'] = all['crud_oil'].str.replace(r'\[.*?\]', '', regex=True) 
all['crud_oil'] = all['crud_oil'].str.strip()
all['crud_oil'] = pd.to_numeric(all['crud_oil'], errors='coerce')
all['crud_oil'] = all['crud_oil'].fillna(0)
all['country'] = all['country'].str.strip()
all.drop_duplicates(inplace=True)
# all.reset_index(drop=True, inplace=True)
print(all)

# conn=myc.connect(
#     host="localhost",
#     user="root",
#     password="Abhinav@2004",
#     database="crud"
# )
# cur=conn.cursor()
# cur.execute("""
# create table if not exists opertaion(
#             id int auto_increment primary key,
#             country varchar(200),
#             crud_oil float,
#             continent varchar(200)
#             )
#             """)
# conn.commit()

# for i,row in all.iterrows():
#     cur.execute(
#         'insert into opertaion(country,crud_oil,continent)values(%s,%s,%s)',
#          (row['country'],row['crud_oil'],row['continent'])
#     )
# conn.commit()

# top=all.sort_values(by='crud_oil',ascending=False).head(5)
# average = all.groupby('continent')['crud_oil'].mean().round(1).sort_values(ascending=False).head(5).reset_index()

# x=top['country']
# y=top['crud_oil']
# fig, axs = plt.subplots(2,2, figsize = (12, 8))
# fig.suptitle("-- Country Crud Oil Production --", fontsize=20, weight='bold', color='darkblue')
# fig.patch.set_facecolor("#EDC574")
# axs[0,0].bar(x,y,color=['orange','r','g','b','c'])
# axs[0,0].set_xlabel('Country',weight='bold',size=10)
# axs[0,0].tick_params(axis='x', rotation=25 )
# axs[0,0].set_ylabel('Crud_oil',weight='bold',size=10)
# axs[0,0].set_title('-- Top 5 Countries by Crud Oil Production -- ',weight='bold',color='green',size=15)
# axs[0,0].grid(alpha=0.2,color='black')
# for i in range(len(x)):
#     axs[0,0].annotate(text=f"{y[i]}",xy=(x[i] ,y[i]),ha='center',weight='bold',size=8)


# x=average['continent']
# y=average['crud_oil']
# axs[0,1].bar(x,y,color=['m','r','g','b','c'])
# axs[0,1].set_xlabel('Country',weight='bold',size=10)
# axs[0,1].tick_params(axis='x', rotation=25 )
# axs[0,1].set_ylabel('Crud_oil',weight='bold',size=10)
# axs[0,1].set_title('-- Average Crud Oil Production by Continent -- ',weight='bold',color='lightcoral',size=15)
# axs[0,1].grid(alpha=0.2,color='black')
# for i in range(len(x)):
#     axs[0,1].annotate(text=f"{y[i]}",xy=(x[i] ,y[i]),ha='center',weight='bold',size=8)


# u=all.groupby('continent')['crud_oil'].sum().sort_values(ascending=False).head(5).reset_index()
# x=u['continent']
# y=u['crud_oil']
# axs[1,0].bar(x,y,color=['c','y','m','b','g'])
# axs[1,0].set_xlabel('Country',weight='bold',size=10)
# axs[1,0].tick_params(axis='x', rotation=25 )
# axs[1,0].set_ylabel('Crud_oil',weight='bold',size=10)
# axs[1,0].set_title('-- Total Crud Oil Production by Continent -- ',weight='bold',color='maroon',size=15)
# axs[1,0].grid(alpha=0.2,color='black')
# for i in range(len(x)):
#     axs[1,0].annotate(text=f"{y[i]}",xy=(x[i] ,y[i]),ha='center',weight='bold',size=8)

# a=all.sort_values(by='crud_oil', ascending=False).head(5)
# x=a['country']
# y=a['crud_oil']
# axs[1,1].pie(y,labels=x,autopct='%1.0f%%',colors=['y','r','c','b','g'])
# axs[1,1].set_title('-- Pie Chart of Top 5 Countries by Crud Oil Production -- ',weight='bold',color='magenta',size=15)    


    
# plt.tight_layout(pad=2)
# plt.show()

