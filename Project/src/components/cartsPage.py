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


def cartPage(root, userID):
    Fetch = """
    SELECT Carts.Cart_ID,Carts.Item_ID,Carts.User_ID,Items.itemName,Items.img_index
    FROM Carts
    INNER JOIN Items
    ON Items.Item_ID = Carts.Item_ID
    INNER JOIN Users
    ON Users.User_ID = Carts.User_ID
    WHERE Users.User_ID = ?
    """
    global cartPageFrame
    cursor.execute(Fetch, [userID])
    FetchData = cursor.fetchall()
    cartPageFrame = Frame(root, bg="#F2CB9B")
    cartPageFrame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    #cartPageFrame.columnconfigure((0, 1, 2, 3), weight=1)
    firstColumnFrame = Frame(cartPageFrame, bg="#F2F2F2")
    secondColumnFrame = Frame(cartPageFrame, bg="#F2F2F2")
    firstColumn = FetchData[:4]
    secondColumn = FetchData[4:8]
    BackButton = Button(cartPageFrame, text="Back", bd=0, width=12, bg="#A67360", fg="#F2F2F2").grid(
        row=0, column=0, sticky="NW", padx=10, pady=10)

    for i in range(len(firstColumn)):
        itemCard = LabelFrame(firstColumnFrame, bg="black").grid(
            row=0, rowspan=4, padx=100)
        Label(firstColumnFrame, image=getImg(firstColumn[i][4]), height=150
              ).grid(row=0, column=i, rowspan=2)
        Label(firstColumnFrame, text=firstColumn[i][3], width=11).grid(
            row=1, column=i, sticky="S")
        Button(firstColumnFrame, text="Buy", width=10,
               bd=0, bg="#F2CB9B").grid(row=2, column=i)
        Button(firstColumnFrame, text="Delete", width=10, command=lambda i=i: deleteItemInCart(firstColumn[i][0], userID),
               bd=0, bg="#A67360").grid(row=3, column=i, pady=10)

    if secondColumn:
        for i in range(len(secondColumn)):
            itemCard = LabelFrame(secondColumnFrame, bg="black").grid(
                row=0, rowspan=4, padx=100)
            Label(secondColumnFrame, image=getImg(secondColumn[i][4]), height=150
                  ).grid(row=0, column=i, rowspan=2)
            Label(secondColumnFrame, text=secondColumn[i][3], width=11).grid(
                row=1, column=i, sticky="S")
            Button(secondColumnFrame, text="Buy", width=10,
                   bd=0, bg="#F2CB9B").grid(row=2, column=i)
            Button(secondColumnFrame, text="Delete", width=10, command=lambda i=i: deleteItemInCart(secondColumn[i][0], userID),
                   bd=0, bg="#A67360").grid(row=3, column=i, pady=10)

    cartPageFrame.place(x=0, y=0, width=w, height=h)
    firstColumnFrame.grid(row=0, padx=110, pady=100)
    secondColumnFrame.grid(row=1)


def deleteItemInCart(cartID, userID):
    delete = """
    DELETE FROM Carts
    WHERE Carts.Cart_ID = ?
    """
    cursor.execute(delete, [cartID])
    connect.commit()
    cartPageFrame.destroy()
    CartPage(root, userID)


def getImg(index):
    imageList = [pic, pic2, pic3, pic4]
    return imageList[index]


w = 1000
h = 800
root = mainwindow()
pic = PhotoImage(file="../../images/Food1.png").subsample(3, 3)
pic2 = PhotoImage(file="../../images/book1.png").subsample(3, 3)
pic3 = PhotoImage(file="../../images/cat1.png").subsample(3, 3)
pic4 = PhotoImage(file="../../images/pen.png").subsample(3, 3)
cartPage(root, 1)
root.mainloop()
