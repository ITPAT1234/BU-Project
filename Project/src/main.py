from tkinter import *
from tkinter import messagebox
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

# ShopMainPage
def shopMainPage(root):
    Fetch = """
        SELECT Users.username,Items.itemName,Items.img_index,Users.User_ID,Items.Item_ID
        FROM Items
        INNER JOIN Users
        ON Items.User_ID = Users.User_ID
    """
    global renderFrame

    cursor.execute(Fetch)
    FetchData = cursor.fetchall()
    renderFrame = Frame(root)
    renderFrame.rowconfigure((0, 1, 4, 5, 9), weight=1)
    renderFrame.columnconfigure((0, 1, 2, 3), weight=1)
    firstColumn = FetchData[:4]
    secondColumn = FetchData[4:8]
    thirdColumn = FetchData[8:]
    for i in range(len(firstColumn)):
        itemCard = LabelFrame(renderFrame).grid(row=1)
        Label(renderFrame, image=getImg(firstColumn[i][2]), bg='#F2F2F2',
              width=200).grid(row=1, column=i, sticky="ns")
        Label(renderFrame, text=firstColumn[i][1], width=11).grid(
            row=2, column=i, sticky="S")
        Label(renderFrame, text=("Vendor : %s" % firstColumn[i][0]), width=12).grid(
            row=3, column=i, sticky="S")
        Button(renderFrame, text="Detail", width=12,command=lambda i=i : redirectToItemDetail(firstColumn[i][4]) ,
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
            Button(renderFrame, text="Detail", width=12, bd=0,command=lambda i=i :redirectToItemDetail(secondColumn[i][4]),
                   bg="#A67360").grid(row=9, column=i, padx=10)

            Button(itemCard, text="Profile", bg="#A67360", fg="#F2F2F2").grid(
                row=3, column=3, sticky="e", padx=50, columnspan=2)

    renderFrame.grid(row=1, column=0, columnspan=4)


def redirectToItemDetail(itemID):
    itemDetailPage(root,itemID)

# UserOwnItemPage
def mutiCount(FetchData, index):
    summary = 0
    for i in range(len(FetchData)):
        summary += FetchData[i][index]
    return summary

def userOwnItem(root):

    global userOwnItemFrame
    global BackButton
    global AddItemPageButton

    userID = 1
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
    renderItemListFrame = Frame(userOwnItemFrame, bg="#F2F2F2")
    userOwnItemFrame.columnconfigure((1, 2, 3), weight=1)
    userOwnItemFrame.rowconfigure((0, 1, 2, 3), weight=1)
    BackButton = Button(userOwnItemFrame, text="Back", bd=0, width=12, bg="#A67360", fg="#F2F2F2").grid(
        row=0, column=0, sticky="NW", padx=10, pady=10)
    AddItemPageButton = Button(userOwnItemFrame, text="Add Item Page", bd=0, bg="#A67360", fg="#F2F2F2", command=lambda: redirecToAddItemPage(userOwnItemFrame, userAddItemPage, userID)).grid(
        row=0, column=3, sticky="NE", padx=10, pady=10)

    Label(userOwnItemFrame, image=LOGO,  bg="#D9BA82").grid(
        row=1, column=0, columnspan=4)
    Label(userOwnItemFrame, text=("Username : %s" % FetchData[0][0]), width=15, bg="#F2CB9B", relief="solid").grid(
        row=2, column=0, columnspan=4)
    Label(userOwnItemFrame, text=("Sold : %s" % (summarySell)), width=10, bg="#F2CB9B", relief="solid").grid(
        row=3, column=0, columnspan=4, sticky="W", padx=200)
    Label(userOwnItemFrame, text=("Supplies : %s" % (summaryAmount)), width=10, bg="#F2CB9B", relief="solid").grid(
        row=3, column=3, columnspan=4, sticky="E", padx=200)

    for i in range(len(FetchData)):
        Label(renderItemListFrame, image=getImg(FetchData[i][3])).grid(
            row=0, column=i, padx=30)
        Label(renderItemListFrame, text=FetchData[i][1]).grid(
            row=1, column=i, padx=30)
        Label(renderItemListFrame, text=("Supplies : %s" % FetchData[i][2])).grid(
            row=2, column=i, padx=30)

    userOwnItemFrame.place(x=0, y=0, width=w, height=h)
    renderItemListFrame.grid(row=4, column=0, columnspan=4, pady=50)

# UserAddItemPage
def userAddItemPage(root,userID):
	
    userAddItemPageFrame = Frame(root)
    userAddItemPageFrame.columnconfigure((0, 1), weight=1)
    itemPicListFrame = Frame(userAddItemPageFrame, bg="#F2F2F2")
    userInputFrame = Frame(userAddItemPageFrame)

    Button(root, text="Back", bd=0, width=12, bg="#A67360", fg="#F2F2F2", command=lambda : redirectTo(userAddItemPageFrame,userOwnItem)).grid(
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

# ITEMDetailPage
def itemDetailPage(root, itemID):
    fetch = f"""
	SELECT Items.User_ID,Items.Item_ID,Users.username,Items.itemName,Items.amount,Items.img_index, Items.price
	FROM Items
	INNER JOIN Users
	ON Users.User_ID = Items.User_ID
	WHERE Items.Item_ID = ?
 	"""
    global itemDetailFrame

    cursor.execute(fetch, [itemID])
    FetchData = cursor.fetchall()
    itemDetailFrame = Frame(root, bg="#D9BA82")
    itemDetailFrame.columnconfigure((0, 1), weight=1)
    itemDetailFrame.rowconfigure((0, 1), weight=1)
    itemImageFrame = Frame(itemDetailFrame)
    itemInformationFrame = Frame(itemDetailFrame, bg="#D9BA82")
    BackButton = Button(itemDetailFrame, text="Back", bd=0, width=12, bg="#A67360", fg="#F2F2F2",command=lambda :redirectTo(itemDetailFrame,shopMainPage)).grid(
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
    itemDetailFrame.destroy()
    shopMainPage(root)

    
# Cart Page 

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

# Register Page 

def registerPage() :
    global newuser
    global newpwd
    global cfpwd
    global regisframe
    
    regisframe = Frame(root,bg='#F2CB9B')
    regisframe.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    regisframe.columnconfigure((0,1),weight=1)
    
    
    Label(regisframe,image=LOGO,bg='#F2CB9B').grid(row=1,column=0,columnspan=2)
   
    Label(regisframe,text='Username : ',bg='#A67360',fg='#f6f5f5').grid(row=2,column=0,sticky='e',padx=10)
    newuser = Entry(regisframe,width=20,bg='#f6f5f5',textvariable=newuserinfo)
    newuser.grid(row=2,column=1,sticky='w',padx=10)
    
    Label(regisframe,text='Password : ',bg='#A67360',fg='#f6f5f5').grid(row=3,column=0,sticky='e',padx=10)
    newpwd = Entry(regisframe,width=20,bg='#f6f5f5',textvariable=newpwdinfo,show='*')
    newpwd.grid(row=3,column=1,sticky='w',padx=10)
    
    Label(regisframe,text="Confirm Password : ",bg='#A67360',fg='#f6f5f5').grid(row=4,column=0,sticky='e',padx=10)
    cfpwd = Entry(regisframe,width=20,bg='#f6f5f5',textvariable=cfinfo,show='*')
    cfpwd.grid(row=4,column=1,sticky='w',padx=10)

    Label(regisframe,text="Year : ",bg='#f6f5f5',fg='#6FB2D2').grid(row=5,column=0,sticky='e',padx=10)
    newyear = Entry(regisframe, width=20, textvariable=yearinfo).grid(row=5,column=1,sticky='w',padx=10)

    Label(regisframe,text="Gender : ",bg='#f6f5f5',fg='#A67360').grid(row=7,column=0,sticky='e',padx=10)
    
    Radiobutton(regisframe,text='Male',bg='#f6f5f5',fg='#A67360',bd=0,variable=genderinfo,value='Male').grid(row=6,column=1,sticky='w')
    Radiobutton(regisframe,text='Female',bg='#f6f5f5',fg='#A67360',bd=0,variable=genderinfo,value='Female').grid(row=7,column=1,sticky='w')
    Radiobutton(regisframe,text='Other',bg='#f6f5f5',fg='#A67360',bd=0,variable=genderinfo,value='Other').grid(row=8,column=1,sticky='w')
    genderinfo.set('Male')
    

    Button(regisframe,text="Cancel", activebackground='#F2CB9B',bg='#D9BA82',command=regisframe.destroy,bd=0).grid(row=11,column=0,columnspan=2,ipady=5,ipadx=5,pady=5,padx=10,sticky='s')
    Button(regisframe,text="Register",bd=0,command=lambda:registration()).grid(row=11,column=1,columnspan=2,ipady=5,ipadx=5,pady=5,padx=10,sticky='s')
    #fullname.focus_force()
    regisframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def registration() :
    if  newuserinfo.get() == "" :
        messagebox.showwarning("Admin : ","Enter New Username first")
        newuser.focus_force()
    elif newpwdinfo.get() == "" :
        messagebox.showwarning("Admin : ","Enter Password first")
        newpwd.focus_force()   
    elif cfinfo.get() == "" :
        messagebox.showwarning("Admin : ","Enter Confirm Password first")
        cfpwd.focus_force()
    elif cfinfo.get() != newpwdinfo.get() :
        messagebox.showwarning("Admin : ","ReEnter password and Confirm Password first")
        cfpwd.focus_force()
    else :

        sql = '''INSERT into Users(username,password,gender,year) values(?,?,?,?)'''
        
        cursor.execute(sql,[newuserinfo.get(),newpwdinfo.get(),genderinfo.get(),yearinfo.get()])
        connect.commit()
        
        messagebox.showinfo("Admin : ","Registration successfully")
        

def getImg(index):
    imageList = [pic, pic2, pic3, pic4]
    return imageList[index]


def redirectTo(currentFrame, goto):
    currentFrame.destroy()
    goto(root)


def redirecToAddItemPage(currentFrame, goto, userID):
    currentFrame.destroy()
    goto(root, userID)


w = 1000
h = 800
connectDB()
root = mainwindow()
LOGO = PhotoImage(file="../images/LOGO.png").subsample(4, 4)
pic = PhotoImage(file="../images/Food1.png").subsample(3, 3)
pic2 = PhotoImage(file="../images/book1.png").subsample(3, 3)
pic3 = PhotoImage(file="../images/cat1.png").subsample(3, 3)
pic4 = PhotoImage(file="../images/pen.png").subsample(3, 3)
getItemName = StringVar()
getAmount = IntVar()
imageIndex = StringVar()
getPrice = StringVar()
newuserinfo = StringVar()
newpwdinfo = StringVar()
cfinfo = StringVar()
yearinfo = StringVar()
genderinfo = StringVar()
#itemDetailPage(root,4)
#userAddItemPage(root)
#userOwnItem(root)
#shopMainPage(root)
#cartPage(root,1)
registerPage()
root.mainloop()
