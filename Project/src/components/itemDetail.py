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


def itemDetailPage(root, itemID):
    fetch = f"""
	SELECT Items.User_ID,Items.Item_ID,Users.username,Items.itemName,Items.amount,Items.img_index, Items.price
	FROM Items
	INNER JOIN Users
	ON Users.User_ID = Items.Item_ID
	WHERE Items.Item_ID = ?
 	"""
    cursor.execute(fetch, [itemID])
    FetchData = cursor.fetchall()
    print(FetchData)
    itemDetailFrame = Frame(root, bg="#D9BA82")
    itemDetailFrame.columnconfigure((0, 1), weight=1)
    itemDetailFrame.rowconfigure((0, 1), weight=1)
    itemImageFrame = Frame(itemDetailFrame)
    itemInformationFrame = Frame(itemDetailFrame, bg="#D9BA82")
    BackButton = Button(itemDetailFrame, text="Back", bd=0, width=12, bg="#A67360", fg="#F2F2F2").grid(
        row=0, column=0, sticky="NW", padx=10, pady=10)

    Label(itemImageFrame, image=getImg(FetchData[0][5])).grid(row=0, column=0)

    Label(itemInformationFrame, text=("Item Name : %s" %
          FetchData[0][3]), width=20, height=2, anchor="w", relief="solid").grid(row=0, column=0, pady=10)
    Label(itemInformationFrame, text=("Vendor Name : %s" %
          FetchData[0][2]), width=20, height=2, anchor="w", relief="solid").grid(row=1, column=0, pady=10)
    Label(itemInformationFrame, text=("Price (Bath) : %s" %
          FetchData[0][6]), width=20, height=2, anchor="w", relief="solid").grid(row=2, column=0, pady=10)
    Label(itemInformationFrame, text=("Item Amount : %s" %
          FetchData[0][4]), width=20, height=2, anchor="w", relief="solid").grid(row=3, column=0, pady=10)

    Button(itemDetailFrame, text="Add To Cart", bd=0, width=12,
           bg="#A67360", fg="#F2F2F2", command=lambda: addToCart(FetchData)).grid(row=1, column=0)
    Button(itemDetailFrame, text="Buy Now!", bd=0, width=12,
           bg="#A67360", fg="#F2F2F2").grid(row=1, column=1)

    itemDetailFrame.place(x=0, y=0, width=w, height=h)
    itemImageFrame.grid(row=0, column=0)
    itemInformationFrame.grid(row=0, column=1)


def addToCart(FetchData):
    userID = FetchData[0][0]
    itemID = FetchData[0][1]
    insert = """
    INSERT INTO Carts(User_ID,Item_ID)
    VALUES (?,?)
    """
    cursor.execute(insert, [userID, itemID])
    connect.commit()
    messagebox.showinfo("Admin : ", "Add To Carts Success!!!")


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
itemDetailPage(root, 4)
root.mainloop()
