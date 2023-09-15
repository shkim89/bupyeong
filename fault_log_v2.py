import pandas as pd
from tkinter import *
from tkinter import filedialog
from os import path
import os
from openpyxl.styles import Font
from openpyxl import load_workbook

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
    writer = pd.ExcelWriter(f'{window.dirName}\\{date}.xlsx', engine='xlsxwriter')
    

    df= pd.read_csv(file_2, encoding='utf-16', usecols=[0,1,4,7,15], skipinitialspace= True)
    device_list = ['LP01','LP02', 'RP01', 'RP02', 'UL01', 'UL02', 'UL03', 'PC01', 'PC02', 'PC03', 'CC04', 'CC05', 'MSAI01', 'MSAI02', 'MSAI03', 'MSAI04']
    for i in device_list:
        df1 = df[df[df.columns[2]].str.contains(i) == True]
        df1 = df1[df1[df1.columns[3]].str.contains('OK') == False]
        df1.to_excel(writer, sheet_name= i)

    writer.save()

    wb = load_workbook(f'{window.dirName}\\{date}.xlsx')
    for i in device_list:
        wb[i].column_dimensions['A'].width = 25
        wb[i].column_dimensions['B'].width = 10
        wb[i].column_dimensions['C'].width = 100
        wb[i].column_dimensions['D'].width = 15
        wb[i].delete_cols(1)
        wb[i].delete_cols(2)
    wb.save(f'{window.dirName}\\{date}.xlsx')


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



