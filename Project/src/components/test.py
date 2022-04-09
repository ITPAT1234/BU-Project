from tkinter import *
import sqlite3

conn = sqlite3.connect("../../../Project/DB/BumarketApp.db")
cursor = conn.cursor()


def mainwindow():
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.config(bg='#D9BA82')
    root.title("BU Market APP ")
    root.option_add('*font', "Garamond 22 bold")
    root.rowconfigure((0, 1, 4, 5, 9), weight=1)
    root.columnconfigure((0, 1, 2, 3), weight=1)
    return root


def renderItemList(root):
    Fetch = """
        SELECT Users.username,Items.itemName,Items.img_index,Users.User_ID
        FROM Items
        INNER JOIN Users
        ON Items.User_ID = Users.User_ID
    """
    cursor.execute(Fetch)
    FetchData = cursor.fetchall()
    renderFrame = Frame(root)
    firstColumn = FetchData[:4]
    secondColumn = FetchData[4:]
    print(firstColumn, secondColumn)
    for i in range(len(firstColumn)):
        itemCard = LabelFrame(renderFrame).grid(row=1)
        Label(itemCard, image=pic, bg='#F2F2F2',
              width=200).grid(row=1, column=i, sticky="ns")
        Label(itemCard, text=firstColumn[i][1], width=11).grid(
            row=1, column=i, sticky="S")
        Label(itemCard, text=firstColumn[i][0], width=12).grid(
            row=2, column=i, sticky="S")
        Button(itemCard, text="Detail", width=12).grid(row=3, column=i)

    if secondColumn:
        for i in range(len(secondColumn)):
            itemCard = LabelFrame(renderFrame).grid(row=1)
            Label(itemCard, image=pic4, bg='#F2F2F2',
                  width=200).grid(row=5, column=i, sticky="ns")
            Label(itemCard, text=secondColumn[i][1], width=12).grid(
                row=6, column=i, sticky="S")
            Label(itemCard, text=secondColumn[i][0], width=12).grid(
                row=7, column=i, sticky="S")
            Button(itemCard, text="Detail", width=12).grid(row=8, column=i)

            Button(itemCard, text="Profile", bg="#A67360", fg="#F2F2F2").grid(
                row=9, column=3, sticky="e", padx=50, columnspan=2)

    renderFrame.grid(row=0, column=0)


w = 1000
h = 800
root = mainwindow()
pic = PhotoImage(file="../../images/Food1.png").subsample(3, 3)
pic2 = PhotoImage(file="../../images/book1.png").subsample(3, 3)
pic3 = PhotoImage(file="../../images/cat1.png").subsample(3, 3)
pic4 = PhotoImage(file="../../images/pen.png").subsample(3, 3)
renderItemList(root)
root.mainloop()
cursor.close()

# i = 0
# for r in range(len(FetchData)):
#  itemCard = LabelFrame(renderFrame, text="test",
#                         bg="black").grid(row=0)
#   for c in range(4):
#        Label(itemCard, text="test", image=pic,
#              bg='#F2F2F2').grid(row=((r//5)+5), column=c)
#        Label(itemCard, text=FetchData[i][1]).grid(
#            row=((r//5)+1), column=c)
#    i += 1
