from tkinter import *
import sqlite3
from tkinter import messagebox

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


def userAddItemPage(root):

    userAddItemPageFrame = Frame(root)
    userAddItemPageFrame.columnconfigure((0, 1), weight=1)
    itemPicListFrame = Frame(userAddItemPageFrame, bg="#F2F2F2")
    userInputFrame = Frame(userAddItemPageFrame)

    Button(root, text="Back", bd=0, width=12, bg="#A67360", fg="#F2F2F2").grid(
        row=0, column=0, sticky="NW", padx=10, pady=10)

    Label(itemPicListFrame, image=pic).grid(row=0, column=0, padx=20, pady=20)
    Label(itemPicListFrame, text="1 : Food").grid(row=1, column=0)
    Label(itemPicListFrame, image=pic2).grid(row=0, column=1, padx=20, pady=20)
    Label(itemPicListFrame, text="2 : Book").grid(row=1, column=1)
    Label(itemPicListFrame, image=pic3).grid(row=2, column=0, padx=20, pady=20)
    Label(itemPicListFrame, text="3 : Animal").grid(row=3, column=0)
    Label(itemPicListFrame, image=pic4).grid(row=2, column=1, padx=20, pady=20)
    Label(itemPicListFrame, text="4 : Stationery").grid(row=3, column=1)

    Label(userInputFrame, text="Item Name").grid(
        row=0, column=0, sticky="WN", columnspan=4)
    Entry(userInputFrame, width=20, textvariable=getItemName).grid(
        row=1, column=0, columnspan=4)
    Label(userInputFrame, text="Amount").grid(
        row=2, column=0, sticky="WN", columnspan=4)
    Entry(userInputFrame, width=20, textvariable=getAmount).grid(
        row=3, column=0, columnspan=4)
    Label(userInputFrame, text="Price").grid(
        row=4, column=0, sticky="WN", columnspan=4)
    Entry(userInputFrame, width=20, textvariable=getPrice).grid(
        row=5, column=0, columnspan=4)
    Label(userInputFrame, text="Choose Images").grid(
        row=6, column=0, sticky="WN", columnspan=4)
    Spinbox(userInputFrame, from_=0, to=4,
            textvariable=imageIndex).grid(row=7)
    Button(userInputFrame, text="Submit", bd=0,
           bg="#A67360", command=submit).grid(row=8, pady=20, sticky="news")

    userAddItemPageFrame.grid(
        row=0, column=0, columnspan=4, rowspan=4)
    itemPicListFrame.grid(row=0, column=0)
    userInputFrame.grid(row=0, column=2, padx=30)


def imageIndexValue(index):
    value = 0
    if index == "1":
        value = 0
    elif index == "2":
        value = 1
    elif index == "3":
        value = 2
    elif index == "4":
        value = 3
    return value


def submit():
    itemName = getItemName.get()
    userID = 1
    amount = getAmount.get()
    price = getPrice.get()
    imgIndex = imageIndexValue(imageIndex.get())
    insert = """
        INSERT INTO Items(itemName,User_ID,amount,img_index,price)
        VALUES (?,?,?,?,?)
    """
    cursor.execute(insert, [itemName, userID, amount, imgIndex, price])
    connect.commit()
    messagebox.showinfo("Admin : ", "Post a Product Success !!!")


w = 1000
h = 800
root = mainwindow()
getItemName = StringVar()
getAmount = IntVar()
imageIndex = StringVar()
getPrice = StringVar()
pic = PhotoImage(file="../../images/Food1.png").subsample(3, 3)
pic2 = PhotoImage(file="../../images/book1.png").subsample(3, 3)
pic3 = PhotoImage(file="../../images/cat1.png").subsample(3, 3)
pic4 = PhotoImage(file="../../images/pen.png").subsample(3, 3)
userAddItemPage(root)
root.mainloop()
