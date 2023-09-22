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
    df= pd.read_csv(file_2, encoding='utf-16', usecols=[0,4,7,15], skipinitialspace= True, index_col=0)
    device_list = ['LP01','LP02', 'RP01', 'RP02', 'UL01', 'UL02', 'UL03', 'PC01', 'PC02', 'PC03', 'CC04', 'CC05', 'MSAI01', 'MSAI02', 'MSAI03', 'MSAI04']
    for i in device_list:
        df1 = df[df[df.columns[0]].str.contains(i) == True]

        df1 = df1[df1[df1.columns[1]].str.contains('OK') == False]
        df1 = df1[df1[df1.columns[1]].str.contains('Maintenance LED on SRM PLC is Active Indicating System Maintenance Required') == False]
        df1 = df1[df1[df1.columns[1]].str.contains('SRM Logging Tool is not connected to the PLC') == False]
        df1 = df1[df1[df1.columns[1]].str.contains('Emergency Circuit Activated Digital Alarm') == False]
        df1 = df1[df1[df1.columns[1]].str.contains('Security Door Open 01 Digital Alarm') == False]
        df1 = df1[df1[df1.columns[1]].str.contains('PALLET ARRIVED AT CP2') == False]
        df1 = df1[df1[df1.columns[1]].str.contains('Layer Picker in Manual') == False]
        df1 = df1[df1[df1.columns[1]].str.contains('Access Requested') == False]
        df1 = df1[df1[df1.columns[1]].str.contains('Jog Mode Selected') == False]
        df1 = df1[df1[df1.columns[1]].str.contains('Gate Open') == False]
        df1 = df1[df1[df1.columns[1]].str.contains('Safety Barrier') == False]


        df1[df1.columns[1]] = df1[df1.columns[1]].str.replace('  ', '')
    
        df1.to_csv(f'{window.dirName}\\{date}_{i}.csv', encoding='utf-8-sig')
    
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



