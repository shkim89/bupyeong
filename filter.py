import pandas as pd

df = pd.read_csv('20231113_RP02.csv', dtype=object)

df = df[df[df.columns[2]].str.contains('Target') == True]
print(df)
df.to_csv('C:\\Users\\kimsh\\OneDrive - dematic.com\\바탕 화면\\faultlog\\bupyeong\\RP2.csv')