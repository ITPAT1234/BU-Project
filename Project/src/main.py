from tkinter import *
import sqlite3


def connectDB():
    global connect,cursor
    connect = sqlite3.connect("../DB/BumarketApp.db")
    cursor = connect.cursor()
    print("Connect DB Success!!!")

def mainwindow():
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.config(bg='#D9BA82')
    root.title("BU Market APP ")
    root.option_add('*font', "Garamond 22 bold")
    root.rowconfigure((0, 1, 2, 3), weight=1)
    root.columnconfigure((0, 1, 2, 3), weight=1)
    return root


w = 1000
h = 800
connectDB()
root = mainwindow()
root.mainloop()