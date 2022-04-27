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

    
def addMoneyPage(root,userID):
	fetch = """
	SELECT *
	FROM Users
	WHERE Users.user_ID = ?
	"""
	cursor.execute(fetch,[userID])
	fetchData = cursor.fetchall()
	userCurrentMoney = fetchData[0][5]
	addMoneyFrame = Frame(root,bg="#D9BA82")
	addMoneyFrame.columnconfigure((0, 1), weight=1)
	addMoneyFrame.rowconfigure((0,1), weight=1)
	userDetailFrame = Frame(addMoneyFrame,bg="#D9BA82")
	BackButton = Button(addMoneyFrame, text="Back", bd=0, width=12, bg="#A67360", fg="#F2F2F2",command="").grid(
		row=0, column=0, sticky="NW", padx=10, pady=10)
	AddMoneyButton = Button(addMoneyFrame, text="Add Money", bd=0, width=12, bg="#A67360", fg="#F2F2F2",command=lambda : addMoney(userID,userCurrentMoney,userAddMoney)).grid(
		row=0, column=1, sticky="NE", padx=10, pady=10)

	Label(userDetailFrame,image=LOGO, bg="#D9BA82").grid(row=0, column=0)
	Label(userDetailFrame,text="Username : %s"%(fetchData[0][2]),relief="solid",bg="#D9BA82",width=20).grid(row=1,column=0,pady=30)
	Label(userDetailFrame,text="User Current Money : %s"%(userCurrentMoney),relief="solid",bg="#D9BA82",width=20).grid(row=2,column=0,pady=30)
	Label(userDetailFrame,text="Add Money :",bg="#D9BA82").grid(row=3,column=0,sticky="w")
	Entry(userDetailFrame,textvariable=userAddMoney).grid(row=4,column=0,sticky="news")
	
	addMoneyFrame.place(x=0, y=0, width=w, height=h)
	userDetailFrame.grid(row=0, column=0, columnspan=2,pady=100)

def addMoney(userID,userCurrentMoney,userAddMoney):
	update = f"""
	 UPDATE Users
	 SET user_Money = {userCurrentMoney + userAddMoney.get()}
	 WHERE Users.user_ID = ?
 	"""
	cursor.execute(update,[userID])
	connect.commit()
	messagebox.showinfo("Admin : ", "Add Money Success !!!")
	

w = 1000
h = 800
root = mainwindow()
LOGO = PhotoImage(file="../../images/LOGO.png").subsample(4, 4)
userAddMoney = IntVar()
addMoneyPage(root,1)
root.mainloop()
