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

    
def paymentPage(root,userID,itemID):
    fetchUserDetail = """
    SELECT Users.User_ID,Users.username,Users.user_Money
    FROM Users
    WHERE Users.User_ID = ?
    """
    fetchItemDetail = """
    SELECT Items.Item_ID,Items.itemName,Items.User_ID,Items.amount,Items.sell_Count,Items.img_index,Items.price,Users.username
    FROM Items
    INNER JOIN Users
    ON Users.User_ID = Items.User_ID
    WHERE Items.Item_ID = ?
    """
    cursor.execute(fetchUserDetail,[userID])
    fetchUserData = cursor.fetchall()
    cursor.execute(fetchItemDetail,[itemID])
    fetchItemData = cursor.fetchall()
    print(fetchUserData,fetchItemData[0])
    paymentFrame = Frame(root,bg="#D9BA82")
    itemImageFrame = Frame(paymentFrame)
    paymentDetail = Frame(paymentFrame,bg="#D9BA82")
    paymentFrame.columnconfigure((0, 1),weight=1)
    paymentFrame.rowconfigure((0, 1),weight=1)
    userID = fetchUserData[0][0]
    itemID = fetchItemData[0][0]
    userMoney = fetchUserData[0][2]
    itemPrice = fetchItemData[0][6]
    amount = fetchItemData[0][3]

    BackButton = Button(paymentFrame, text="Back", bd=0, width=12, bg="#A67360", fg="#F2F2F2").grid(
        row=0, column=0, sticky="NW", padx=10, pady=10)
    
    Label(itemImageFrame,image=getImg(fetchItemData[0][5])).grid(row=0, column=0,pady=10)
    Label(itemImageFrame,text=fetchItemData[0][1]).grid(row=1,column=0,pady=10)
    Label(itemImageFrame,text="Vendor : %s"%(fetchItemData[0][7])).grid(row=2,column=0,pady=10)

    Label(paymentDetail, text=("User Money : %20s" %
          userMoney), width=20, anchor="w", relief="solid").grid(row=0, column=0, pady=10)
    Label(paymentDetail, text=("Item Price : %24s" %
          itemPrice), width=20, anchor="w", relief="solid").grid(row=1, column=0, pady=10)
    Label(paymentDetail, text=("Summary : %25s" %
          summaryPrice(fetchUserData[0][2],fetchItemData[0][6])), width=20, anchor="w", relief="solid").grid(row=2, column=0, pady=10)
    Label(paymentDetail, text=("Amount : %29s" %
          amount), width=20, anchor="w", relief="solid").grid(row=3, column=0, pady=10)
    Label(paymentDetail, text="Buy :", anchor="w",bg="#D9BA82").grid(row=4, column=0, pady=10,sticky="W")
    Scale(paymentDetail,from_=0,to=fetchItemData[0][3],orient="horizontal",variable=buyAmount).grid(row=5,column=0,sticky="nesw")

    if summaryPrice(fetchUserData[0][2],fetchItemData[0][6]) <= 0:
       Button(paymentDetail,text="Buy Now",bg="#A67360", fg="#F2F2F2",state="disabled").grid(row=6, column=0,sticky="news",pady=10)
    else:
       Button(paymentDetail,text="Buy Now",bg="#A67360", fg="#F2F2F2",command=lambda : buyIt(fetchUserData[0][2],fetchItemData[0][6],amount,buyAmount,userID,itemID)).grid(row=6, column=0,sticky="news",pady=10)


    paymentFrame.place(x=0, y=0, width=w, height=h)
    itemImageFrame.grid(row=0, column=0)
    paymentDetail.grid(row=0, column=1)

def summaryPrice(userMoney,itemPrice):
    result = userMoney - itemPrice
    return result

def buyIt(userMoney,itemPrice,amount,buyAmount,userID,itemID):
    updateUser = f"""
    UPDATE Users
    SET user_Money = {summaryPrice(userMoney,itemPrice)}
    WHERE User_ID = ?

    """
    updateItem = f"""
    UPDATE Items
    SET amount = {amount - buyAmount.get()} , sell_Count = {buyAmount.get()}
    WHERE Item_ID = ?
    """
    cursor.execute(updateUser,[userID])
    cursor.execute(updateItem,[itemID])
    connect.commit()
    messagebox.showinfo("Admin : ", "Buy Success!!!")

def summaryPrice(userMoney,itemPrice):
    result = userMoney - itemPrice
    return result

    
def getImg(index):
    imageList = [pic, pic2, pic3, pic4]
    return imageList[index]

w = 1000
h = 800
root = mainwindow()
buyAmount = IntVar()
pic = PhotoImage(file="../../images/Food1.png").subsample(3, 3)
pic2 = PhotoImage(file="../../images/book1.png").subsample(3, 3)
pic3 = PhotoImage(file="../../images/cat1.png").subsample(3, 3)
pic4 = PhotoImage(file="../../images/pen.png").subsample(3, 3)
paymentPage(root,1,1)
root.mainloop() 