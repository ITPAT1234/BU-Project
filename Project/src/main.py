from tkinter import *
import sqlite3


def connectDB():
    global connect, cursor
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


def shopMainPage(root):
    Fetch = """
        SELECT Users.username,Items.itemName,Items.img_index,Users.User_ID
        FROM Items
        INNER JOIN Users
        ON Items.User_ID = Users.User_ID
    """
    cursor.execute(Fetch)
    FetchData = cursor.fetchall()
    renderFrame = Frame(root)
    renderFrame.rowconfigure((0, 1, 4, 5, 9), weight=1)
    renderFrame.columnconfigure((0, 1, 2, 3), weight=1)
    firstColumn = FetchData[:4]
    secondColumn = FetchData[4:8]
    thirdColumn = FetchData[8:]
    print(firstColumn, secondColumn, thirdColumn)
    for i in range(len(firstColumn)):
        itemCard = LabelFrame(renderFrame).grid(row=1)
        Label(renderFrame, image=getImg(firstColumn[i][2]), bg='#F2F2F2',
              width=200).grid(row=1, column=i, sticky="ns")
        Label(renderFrame, text=firstColumn[i][1], width=11).grid(
            row=2, column=i, sticky="S")
        Label(renderFrame, text=("Vendor : %s" % firstColumn[i][0]), width=12).grid(
            row=3, column=i, sticky="S")
        Button(renderFrame, text="Detail", width=12,
               bd=0, bg="#A67360").grid(row=4, column=i)

    if secondColumn:
        for i in range(len(secondColumn)):
            itemCard = LabelFrame(renderFrame).grid(row=5)
            Label(renderFrame, image=getImg(secondColumn[i][2]), bg='#F2F2F2',
                  width=200).grid(row=6, column=i, sticky="ns")
            Label(renderFrame, text=secondColumn[i][1], width=12).grid(
                row=7, column=i, sticky="S")
            Label(renderFrame, text=("Vendor : %s" % secondColumn[i][0]), width=12).grid(
                row=8, column=i, sticky="S")
            Button(renderFrame, text="Detail", width=12, bd=0,
                   bg="#A67360").grid(row=9, column=i, padx=10)

            Button(itemCard, text="Profile", bg="#A67360", fg="#F2F2F2").grid(
                row=3, column=3, sticky="e", padx=50, columnspan=2)

    renderFrame.grid(row=1, column=0, columnspan=4)


def getImg(index):
    imageList = [pic, pic2, pic3, pic4]
    return imageList[index]


w = 1000
h = 800
connectDB()
root = mainwindow()
pic = PhotoImage(file="../images/Food1.png").subsample(3, 3)
pic2 = PhotoImage(file="../images/book1.png").subsample(3, 3)
pic3 = PhotoImage(file="../images/cat1.png").subsample(3, 3)
pic4 = PhotoImage(file="../images/pen.png").subsample(3, 3)
shopMainPage(root)
root.mainloop()
