from tkinter import *
import sqlite3

w = 1000
h = 800
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

def mutiCount(FetchData, index):
    summary = 0
    for i in range(len(FetchData)):
        summary += FetchData[i][index]
    return summary


def userOwnItem(root):
    userID = 2
    fetch = f"""
	SELECT Users.username,Items.itemName,Items.amount,Items.img_index,Items.sell_count
	FROM Users
	INNER JOIN Items
	ON Users.User_ID = Items.User_ID
	WHERE Users.User_ID = ?
    LIMIT 4
        """
    cursor.execute(fetch, [userID])
    FetchData = cursor.fetchall()
    summarySell = mutiCount(FetchData, 4)
    summaryAmount = mutiCount(FetchData, 2)
    userOwnItemFrame = Frame(root, bg="#D9BA82")
    renderItemListFrame = Frame(root, bg="#F2F2F2")
    userOwnItemFrame.columnconfigure((0, 1, 2, 3), weight=1)
    userOwnItemFrame.rowconfigure((0, 1, 2, 3), weight=1)
    Button(root, text="Back", bd=0, width=12, bg="#A67360", fg="#F2F2F2").grid(
        row=0, column=0, sticky="NW", padx=10, pady=10)
    Button(root, text="Add Item Page", bd=0, bg="#A67360", fg="#F2F2F2").grid(
        row=0, column=3, sticky="NE", padx=10, pady=10)

    Label(userOwnItemFrame, image=LOGO, width=500, bg="#D9BA82").grid(
        row=0, column=0, columnspan=4)
    Label(userOwnItemFrame, text=("Username : %s" % FetchData[0][0]), bg="#F2CB9B", relief="solid").grid(
        row=2, column=0, columnspan=4, pady=50, sticky="news")
    Label(userOwnItemFrame, text=("Sold : %s" % (summarySell)), bg="#F2CB9B", relief="solid").grid(
        row=3, column=0, columnspan=4, sticky="W", ipadx=10)
    Label(userOwnItemFrame, text=("Supplies : %s" % (summaryAmount)), bg="#F2CB9B").grid(
        row=3, column=0, columnspan=4, sticky="E")

    for i in range(len(FetchData)):
        Label(renderItemListFrame, image=getImg(FetchData[i][3])).grid(
            row=0, column=i, padx=30)
        Label(renderItemListFrame, text=FetchData[i][1]).grid(
            row=1, column=i, padx=30)
        Label(renderItemListFrame, text=("Supplies : %s" % FetchData[i][2])).grid(
            row=2, column=i, padx=30)

    userOwnItemFrame.grid(row=0, column=0, columnspan=4)
    renderItemListFrame.grid(row=1, column=0, columnspan=4)


def getImg(index):
    imageList = [pic, pic2, pic3, pic4]
    return imageList[index]


root = mainwindow()
LOGO = PhotoImage(file="../../images/LOGO.png").subsample(4, 4)
pic = PhotoImage(file="../../images/Food1.png").subsample(3, 3)
pic2 = PhotoImage(file="../../images/book1.png").subsample(3, 3)
pic3 = PhotoImage(file="../../images/cat1.png").subsample(3, 3)
pic4 = PhotoImage(file="../../images/pen.png").subsample(3, 3)
userOwnItem(root)
root.mainloop()
