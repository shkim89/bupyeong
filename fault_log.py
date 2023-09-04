import pandas as pd
from tkinter import *
from tkinter import filedialog
from os import path
import os

window=Tk()

window.title("로그로그")
window.geometry("300x300+200+200")
window.resizable(False, False)


def open_dialog_1():
    global df
    global file_2
    global date
    window.dirName=filedialog.askdirectory()
    print(window.dirName)
    date = str(file_2[-12:-4])
    df= pd.read_csv(file_2, encoding='utf-16', usecols=[0,1,4,7,15], skipinitialspace= True)
    df1 = df[df[df.columns[2]].str.contains('LP01') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"LP01"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('LP02') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"LP02"}.csv', encoding='utf-8-sig')   

    df1 = df[df[df.columns[2]].str.contains('RP01') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"RP01"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('RP02') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"RP02"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('UL01') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"UL01"}.csv', encoding='utf-8-sig')  

    df1 = df[df[df.columns[2]].str.contains('UL02') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"UL02"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('UL03') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"UL03"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('PC01') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"CC01"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('PC02') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"CC02"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('PC03') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"CC03"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('CC04') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"CC04"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('CC05') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"CC05"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('MSAI01') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"MSAI01"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('MSAI02') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"MSAI02"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('MSAI03') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"MSAI03"}.csv', encoding='utf-8-sig')

    df1 = df[df[df.columns[2]].str.contains('MSAI04') == True]
    df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
    df1.to_csv(f'{window.dirName}\\{date}_{"MSAI04"}.csv', encoding='utf-8-sig')

    os.startfile(window.dirName)
    window.destroy()



def open_dialog_2():
    global df
    global file_2
    global date
    file_2 = filedialog.askopenfilename(initialdir= path.dirname(__file__))  

button = Button(window, text="로그열기", command=open_dialog_2)
button.place(x=10, y=10, width=280, height=135)

button = Button(window, text="저장경로", command=open_dialog_1)
button.place(x=10, y=150, width=280, height=135)

window.mainloop()



