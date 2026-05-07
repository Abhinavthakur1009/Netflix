# Example Dataset (We Will Use This)
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# data = {
#     "Age": [25, np.nan, 35, 40, 29, 120, 30, np.nan],
#     "Salary": [50000, 60000, np.nan, 80000, 52000, 1000000, 58000, 50000],
#     "City": ["Delhi", "Mumbai", "Delhi", "Chennai", np.nan, "Delhi", "Mumbai", "Chandigarh"],
#     "Purchased": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes","No"]
# }

# df = pd.DataFrame(data)
# print(df.isnull().sum())

# print(df['Age'].isnull().sum()/len(df["Age"])*100)

# all=list(df.columns)
# no=[]
# per=[]
# ya=[]
# npe=[]
# for i in all:
#     a=df[i].isnull().sum()
#     no.append(a)
#     b=df[i].isnull().sum()/len(df[i])
#     per.append(b)
#     c=df[i].notnull().sum()
#     ya.append(c)
#     d=df[i].notnull().sum()/len(df[i])
#     npe.append(d)
#     print(f"{i}\t{no}\t{per}%\t{ya}\t{npe}%")

# dic = {
#     "columns_name " : all,
#     "count_null" : no,
#     "%age_null" : per,
#     "count_not_null" : ya,
#     "%age_not" : npe
# }
# null_df = pd.DataFrame(dic)
# print(null_df)

data = {
    "Age": [25, np.nan, 35, 40, 29, 120, 30, np.nan],
    "Salary": [40000, 60000, np.nan, 80000, 52000, 1000000, 58000, 50000],
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai", np.nan, "Delhi", "Mumbai", "Chandigarh"],
    "Purchased": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes","No"]
}

df = pd.DataFrame(data)
low=df['Salary'].quantile(0.01)
high=df['Salary'].quantile(0.99)
print(f'{low}\n{high}')
# print('*'*50)
# print(df[(df["Salary"]<low)|(df["Salary"]>high)])
# print('*'*50)
# df_trimmed = df[(df["Salary"] >= low) & (df["Salary"] <= high)]
# print(df_trimmed)
# a=df[(df["Salary"] >= low) & (df["Salary"] <= high)]
# print(a)
# df['ss']=np.where(
#     df['Salary']>high,high,
#     np.where(df["Salary"]<low,low,df['Salary'])
# )
# print(df["ss"])

df["Salary_bin"] = pd.cut(df["Salary"], bins=6)
print(df["Salary_bin"])
