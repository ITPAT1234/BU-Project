from tkinter import *
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


def userPage(root, userID=0):
    fetch = """
	SELECT * 
	FROM Users
	WHERE Users.User_ID = ?
        """
    cursor.execute(fetch, [userID])
    fetchData = cursor.fetchall()
    print(fetchData)
    userPageFrame = Frame(root, bg="#D9BA82")
    userPageFrame.columnconfigure((0, 1), weight=1)
    userDetailFrame = Frame(userPageFrame, bg="#D9BA82")
    userButtonFrame = Frame(userPageFrame, bg="#D9BA82")
    BackButton = Button(userPageFrame, text="Back", bd=0, width=12, bg="#A67360", fg="#F2F2F2").grid(
        row=0, column=0, sticky="NW", padx=10, pady=10)

    Label(userDetailFrame, text="Username : %s" % fetchData[0][1], width=25, bg="#F2CB9B", relief="solid").grid(
        row=0, column=0, columnspan=2, pady=20)
    Label(userDetailFrame, text="Gender : %s" % fetchData[0][3], width=25, bg="#F2CB9B", relief="solid").grid(
        row=1, column=0, columnspan=2, pady=20)
    Label(userDetailFrame, text="Year of birth : %s" % fetchData[0][4], width=25, bg="#F2CB9B", relief="solid").grid(
        row=2, column=0, columnspan=2, pady=20)
    Label(userDetailFrame, text="User Money : %s" % fetchData[0][5], width=25, bg="#F2CB9B", relief="solid").grid(
        row=3, column=0, columnspan=2, pady=20)

    Button(userButtonFrame, text="Cart Page", bd=0, width=12, bg="#A67360", fg="#F2F2F2").grid(
        row=4, column=0, sticky="NW", padx=30)
    Button(userButtonFrame, text="Add Money", bd=0, width=12, bg="#A67360", fg="#F2F2F2").grid(
        row=4, column=1, sticky="NW", padx=30)
    Button(userButtonFrame, text="Own Item Page", bd=0, width=12, bg="#A67360", fg="#F2F2F2").grid(
        row=4, column=2, sticky="NW", padx=30)

    userPageFrame.place(x=0, y=0, width=w, height=h)
    userDetailFrame.grid(row=1, column=0, columnspan=2, pady=80)
    userButtonFrame.grid(row=2, column=0, columnspan=2, pady=50)


w = 1000
h = 800
root = mainwindow()
userPage(root, 1)
root.mainloop()
