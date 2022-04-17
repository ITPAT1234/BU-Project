# <<<<<<< HEAD
from tkinter import *
from tkinter import messagebox
import sqlite3


connect = sqlite3.connect("../../DB/BumarketApp.db")
cursor = connect.cursor()

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

def loginPage(root):
    global loginframe

    loginframe = Frame(root, bg='#D9BA82')
    loginframe.rowconfigure((0, 1, 2, 3), weight=1)
    loginframe.columnconfigure((0, 1), weight=1)
    Label(loginframe, text="Account Login", font="Garamond 26 bold",fg='#4a3933', compound=LEFT, bg='#D9BA82').place(x=380,y=30)

    Label(loginframe, text="Username : ", bg='#D9BA82',fg='#4a3933', padx=20,).grid(row=1, column=0, sticky='e')
    Entry(loginframe,bg="#A67360", fg='#4a3933',width=20,textvariable=usernameInput).grid(row=1, column=1, sticky='w', padx=20,columnspan=3)
    Label(loginframe, text="Password  : ", bg='#D9BA82',fg='#4a3933', padx=20).grid(row=2, column=0, sticky='e')
    Entry(loginframe, bg='#A67360', fg='#4a3933',width=20, show='*',textvariable=passwordInput).grid(row=2, column=1, sticky='w', padx=20,columnspan=3)

    Button(loginframe, text="Login", width=10,command=lambda :checkLogin(usernameInput.get(),passwordInput.get())).grid(row=3, column=0, pady=10, ipady=10, padx=20)
    Button(loginframe, text="Register", width=10).grid(row=3, column=1, pady=10, ipady=10,  padx=20)
    Button(loginframe, text="Exit", width=10).grid(row=3, column=2, pady=10, ipady=10, padx=20)
    loginframe.grid(row=1, column=0, columnspan=3, rowspan=2, sticky='news')


def checkLogin(username,password):
    fetch = """
    SELECT * 
    FROM Users
    WHERE Users.username = ? AND Users.password = ?
    """
    cursor.execute(fetch, [username,password])
    fetchData = cursor.fetchall()
    if fetchData :
	    messagebox.showinfo("Admin : ", "Login Success!!!")
    else : 
	    messagebox.showinfo("Admin : ", "Username and Password is Incorrect !!!")
    
    
w = 1000
h = 800
root= mainwindow()
usernameInput = StringVar()
passwordInput = StringVar()
loginlayout(root)
root.mainloop()
# >>>>>>> dff75a0164c6ae59101530bf141d7707b25f8bb2

