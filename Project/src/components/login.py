# <<<<<<< HEAD
from logging import root
from tkinter import *


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

def loginlayout(root):
    global userentry
    global pwdentry
    global loginframe

    loginframe = Frame(root, bg='#D9BA82')
    loginframe.rowconfigure((0, 1, 2, 3), weight=1)
    loginframe.columnconfigure((0, 1), weight=1)

    Label(loginframe, text="Account Login", font="Garamond 26 bold",fg='#4a3933', compound=LEFT, bg='#D9BA82').grid(row=0, columnspan=2)
    Label(loginframe, text="Username : ", bg='#D9BA82',fg='#4a3933', padx=20).grid(row=1, column=0, sticky='e')
    userentry = Entry(loginframe,bg="#A67360", fg='#4a3933',width=20)
    userentry.grid(row=1, column=1, sticky='w', padx=20)

    pwdentry = Entry(loginframe, bg='#A67360', fg='#4a3933',width=20, show='*')
    pwdentry.grid(row=2, column=1, sticky='w', padx=20)
    Label(loginframe, text="Password  : ", bg='#D9BA82',fg='#4a3933', padx=20).grid(row=2, column=0, sticky='e')
    Button(loginframe, text="Register", width=10).grid(row=3, column=1, pady=10, ipady=10,  padx=20)
    Button(loginframe, text="Login", width=10).grid(row=3, column=0, pady=10, ipady=10, padx=20)
    Button(loginframe, text="Exit", width=10).grid(row=3, column=3, pady=10, ipady=10, padx=20)
    loginframe.grid(row=1, column=0, columnspan=3, rowspan=2, sticky='news')


w = 1000
h = 800
root= mainwindow()
loginlayout(root)
root.mainloop()

# =======
# print(1 % 4)
# print(2 % 4)
# print(3 % 4)
# print(4 % 4)
# print(5 % 4)
# print(6 % 4)
# print(7 % 4)
# print(8 % 4)
# >>>>>>> dff75a0164c6ae59101530bf141d7707b25f8bb2

