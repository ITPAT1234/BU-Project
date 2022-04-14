from tkinter import *
from tkinter import messagebox
import sqlite3


def mainwindow() :
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#A67360')
    root.title("Welcome to User Registration")
    root.option_add('*font',"calibri 24 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root


def regisclick() :
    global newuser
    global newpwd
    global cfpwd
    global regisframe
    
    root.title("Welcome to User Registration : ")
    root.config(bg='lightblue')
    
    regisframe = Frame(root,bg='#F2CB9B')
    regisframe.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    regisframe.columnconfigure((0,1),weight=1)
    
    
    Label(regisframe,image=img2,bg='#F2CB9B').grid(row=1,column=0,columnspan=2)
   
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
    newyear = Spinbox(regisframe, from_=1, to=4,width=5, justify=CENTER, fg='#6FB2D2', bd=0, textvariable=yearinfo).grid(row=5,column=1,sticky='w',padx=10)

    Label(regisframe,text="Gender : ",bg='#f6f5f5',fg='#A67360').grid(row=7,column=0,sticky='e',padx=10)
    
    Radiobutton(regisframe,text='Male',bg='#f6f5f5',fg='#A67360',bd=0,variable=genderinfo,value='Male').grid(row=6,column=1,sticky='w')
    Radiobutton(regisframe,text='Female',bg='#f6f5f5',fg='#A67360',bd=0,variable=genderinfo,value='Female').grid(row=7,column=1,sticky='w')
    Radiobutton(regisframe,text='Other',bg='#f6f5f5',fg='#A67360',bd=0,variable=genderinfo,value='Other').grid(row=8,column=1,sticky='w')
    genderinfo.set('Male')
    

    Button(regisframe,text="Cancel", activebackground='#F2CB9B',bg='#D9BA82',command=regisframe.destroy).grid(row=11,column=0,columnspan=2,ipady=5,ipadx=5,pady=5,padx=10,sticky='s')
    Button(regisframe,text="Register",command=lambda:registration()).grid(row=11,column=1,columnspan=2,ipady=5,ipadx=5,pady=5,padx=10,sticky='s')
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

        sql = '''INSERT into student values(?,?,)'''
        
        cursor.execute(sql,[newuserinfo.get(),newpwdinfo.get()])
        conn.commit()
        
        messagebox.showinfo("Admin : ","Registration successfully")
            
w = 1000
h = 800
    
conn = sqlite3.connect('school11.db')
cursor = conn.cursor()
print("Connection Succesfully")

root = mainwindow()
regisframe = Frame(root)
profileframe = Frame(root,bg='#F2CB9B')

img2 = PhotoImage(file='LOGO.png').subsample(5,5)

newuserinfo = StringVar()
newpwdinfo = StringVar()
cfinfo = StringVar()
yearinfo = StringVar()
genderinfo = StringVar()
regisclick()
root.mainloop()