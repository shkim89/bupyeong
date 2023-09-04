import pandas as pd


df= pd.read_csv('20230904_RP01.csv', encoding='utf-8', skipinitialspace= True)
df1 = df[df[df.columns[4]].str.contains('The Target Space Is Occupied Or Not Accessible Digital Alarm') == True]
print(df1)
df1.to_csv('sorted.csv', encoding='utf-8-sig')