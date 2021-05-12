"""
Author: Hello (World)
Untitled-1 (c) 2021
Desc: Tkinter Program to Manage Sports Club
Created:  2021-05-11T14:19:42.784Z
Modified: !date!
"""

import sqlite3
import tkinter as tk
import datetime
import os
from tkinter import *
from PIL import ImageTk, Image  # PIL -> Pillow
from tkinter import ttk
from tkinter import messagebox
from tkinter import Scrollbar

dbcon=sqlite3.connect('spm.db')
dbcon.cursor()
dbcon.execute('Create table if not exists Users(Date TEXT, Name TEXT, Username TEXT, Password TEXT, ConfirmPassword TEXT, Phone_number INTEGER, Email TEXT, Type TEXT)')
dbcon.execute('Create table if not exists GroundBooking(Date TEXT , NAME TEXT, PHONE_NUMBER INTEGER, TIME_SLOT TEXT, Ground_Location TEXT)')
LoginPage = Tk()
LoginPage.title('Login Page')
LoginPage.wm_resizable(False, False)
LoginPage.geometry('900x600')
# Adding a background image
same = True
n = 0.25
background_image = Image.open("sports.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

background_image = background_image.resize(
    (newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(LoginPage)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(LoginPage, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="WELCOME TO\nSPORTS MANAGEMENT SYSTEM",
                     bg='black', fg='white', font=('tr', 20))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

frame1 = Frame(LoginPage, bg="white").place(x=300, y=200, height=200, width=300)
Label(LoginPage, text="By Anuj,  Mitesh,  Kunal & Anushka", font="tr 14",
      fg="BLACK", bd=1, anchor="c").place(x=300, y=450)
USER = Label(LoginPage, text="USER_NAME", fg="Black",
             bg="white").place(x=340, y=250)
PASS = Label(LoginPage, text="PASSWORD", fg="Black", bg="white").place(x=340, y=300)
user_verify = StringVar()
pass_verify = StringVar()
username = tk.Entry(LoginPage, textvariable=user_verify)
username.place(x=450, y=250)
password = tk.Entry(LoginPage, textvariable=pass_verify, show="*")
password.place(x=450, y=300)

def Back_page():
    messagebox.showinfo("BACK", "Proceeding to Home Page")
    back = logininfo()

def logininfo():

    insert_command = """INSERT OR IGNORE INTO Users(date, username, password) VALUES('%s', '%s', '%s');"""
    datestamp = datetime.datetime.now()
    username1 = username.get()
    password1 = password.get()
    x = dbcon.cursor()
    # Find user If there is any take proper action
    x.execute('SELECT Username,Password,Type FROM Users WHERE Username=? AND Password=?',
              (username1, password1))
    found = x.fetchone()
    if found:
        dbcon.execute(insert_command % (datestamp, username1, password1))
        dbcon.commit()
        # connect.close()
        loggedin(username1)
    else:
        messagebox.showerror('Oops!', 'Username or Password is incorrect.')

def loggedin(user):
    messagebox.showinfo("LOGIN!!", "LOGIN SUCCEFUL!! Welcome to The Club")
    window2 = Toplevel()
    window2.geometry("900x900")
    window2.configure(bg="orange")
    window2.title("HOME PAGE")
    window2.resizable(False, False)
    headingFrame1 = Frame(window2, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = Label(headingFrame1, text= f"Hello {user} Select an Option",
                         bg='black', fg='white', font=('tr', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    coach = tk.Button(window2, text="MANAGE TEAM", font="tr 20 bold", fg="black", bd=4, command=Team)
    coach.place(x=200, y=250, width=500)
    bturf = tk.Button(window2, text="BOOK TURF", font="tr 20 bold", fg="black", bd=4, command=BookingPage)
    bturf.place(x=200, y=350, width=500)
    bookturf = tk.Button(window2, text="VIEW BOOKED TURF", font="tr 20 bold", fg="black", bd=4, command=BookingHistory)
    bookturf.place(x=200, y=450, width=500)
    shopeq = tk.Button(window2, text="SHOP EQUIPMENT", font="tr 20 bold", fg="black", bd=4, command=shopequip)
    shopeq.place(x=200, y=550, width=500)

def BookingPage():
    book = tk.Toplevel()
    book.geometry("600x650")
    book.title("AVAILABLE GROUNDS")
    book.configure(bg="white")
    frame2 = Frame(book, bg="white").place(x=100, y=50, height=600, width=650)

    # 1st turf
    a1 = Label(book, text="D.S Sports Ground ", font="tr 15",
               fg="black", bg="white").place(x=200, y=120, width=300)
    a2 = Label(book, text="ADDRESS:", font="tr 10",
               fg="black", bg="white").place(x=120, y=150)
    a3 = Label(book, text="A.C. Patil School, Sector 8,",
               font="tr 10", fg="black", bg="white").place(x=190, y=150)
    a4 = Label(book, text="Near Reena Mokal Hospital, Kandivali West, Mumbai, Maharashtra 400067",
               font="tr 10", fg="black", bg="white").place(x=190, y=170)
    a5 = Label(book, text="Phone:", font="tr 10",
               fg="black", bg="White").place(x=120, y=200)
    a6 = Label(book, text="8852023645", font="tr 10 ",
               fg="black", bg="White").place(x=180, y=200)
    b1 = Button(book, text="Book Now", font="tr 10", fg="black",
                bd=1, bg="#41B3A3", command=Book_now)
    b1.place(x=300, y=250)

    # 2nd turf
    b11 = Label(book, text="J.K turf", font="tr 15", fg="black",
                bg="white").place(x=200, y=300, width=300)
    b12 = Label(book, text="ADDRESS:", font="tr 10",
                fg="black", bg="white").place(x=120, y=350)
    b13 = Label(book, text="J.K turf, near scientific device company",
                font="tr 10", fg="black", bg="white").place(x=190, y=350)
    b14 = Label(book, text="Kausa, Mumbra, Thane, Maharashtra 400612",
                font="tr 10", fg="black", bg="white").place(x=190, y=370)
    b15 = Label(book, text="Phone:", font="tr 10",
                fg="black", bg="White").place(x=120, y=390)
    b16 = Label(book, text="8254682025", font="tr 10 ",
                fg="black", bg="White").place(x=180, y=390)
    b2 = Button(book, text="Book Now", font="tr 10", fg="black",
                bd=1, bg="#41B3A3", command=Book_now)
    b2.place(x=300, y=420)

    # 3rd Ground
    c1 = Label(book, text="Dribble Football Turf", font="tr 15", fg="black",
               bg="white").place(x=200, y=500, width=300)
    c2 = Label(book, text="ADDRESS:", font="tr 10",
               fg="black", bg="white").place(x=120, y=550)
    c3 = Label(book, text="J.K turf, near viviana mall",
               font="tr 10", fg="black", bg="white").place(x=190, y=550)
    c4 = Label(book, text="Thane, Maharashtra 400612", font="tr 10",
               fg="black", bg="white").place(x=190, y=570)
    c5 = Label(book, text="Phone:", font="tr 10",
               fg="black", bg="White").place(x=120, y=600)
    c6 = Label(book, text="8254682025", font="tr 10 ",
               fg="black", bg="White").place(x=180, y=600)
    b3 = Button(book, text="Book Now", font="tr 10", fg="black",
                bd=1, bg="#41B3A3", command=Book_now)
    b3.place(x=300, y=620)

    Back1 = Button(book, text="Back", font="tr 10", fg="black",
                   bg="#41B3A3", command=Back_page).place(x=650, y=620)

def Book_now():
    nw = tk.Toplevel()
    nw.geometry("900x800+100+50")
    nw.title("BOOK SLOT")
    nw.configure(bg="white")
    frame5 = Frame(nw, bg="white").place(x=100, y=80, height=500, width=650)
    lb = Label(nw, text="ENTER DETAILS", font="tr 20 bold",
               fg="#003b73", bg="white").place(x=320, y=150)
    lb1 = Label(nw, text="NAME", font="tr 12 bold",
                fg="black", bg="white").place(x=200, y=210)
    lb2 = Label(nw, text="PHONE NUMBER", font="tr 12 bold",
                fg="black", bg="white").place(x=200, y=250)
    lb3 = Label(nw, text="TIME SLOT", font="tr 12 bold",
                fg="black", bg="white").place(x=200, y=300)
    lb4 = Label(nw, text="Ground Location & Details",
                font="tr 12 bold", fg="black", bg="white").place(x=150, y=350)
    nme = StringVar
    Phn = IntVar
    optTime = ["11AM- 01PM",
               "02PM- 04PM",
               "05PM- 07PM",
               "08PM- 10PM", ]
    global Time
    Time = IntVar()
    Time.set(optTime[0])
    drop1 = OptionMenu(nw, Time, *optTime)
    drop1.place(x=540, y=300, height=15, width=20)
    optNameAddress = ["SmashUp Ground : ADDRESS:- K.B. Patil School, Sector 8,Near Reena Mokal Hospital , Kandivali West, Mumbai, Maharashtra 400067, Phone:8852023645 ",
                      "J.K turf : ADDRESS :- Near scientific device company, Mumbra, Thane, Maharashtra 400612, Phone: 8254682025",
                      "Dribble Football Turf : ADDRESS :- Near vivana mall, Thane, Maharashtra 400612, Phone : 8254682025",
                      "Bhumiputra Maidan : ADDRESS :- Bhumiputra Maidan NEAR RAM MANDIR, DOMBIVILI , Thane, Maharashtra 400612, Phone: 8254682025",
                      "PHOENIX GROUND : ADDRESS :- Near midc water tank, Kalyan-Dmbivili, Thane, Maharashtra 400612, Phone:8254682025",
                      "DYANMANDIR GROUND : ADDRESS :- Near Mamta Hospital, model college, Dombivili, Thane, Maharashtra 400612, Phone: 8254682025"
                      ]
    NameAddress = StringVar()
    NameAddress.set(optNameAddress[0])
    drop2 = OptionMenu(nw, NameAddress, *optNameAddress)
    drop2.place(x=540, y=350, height=15, width=20)

    nmentry = tk.Entry(nw, textvariable=nme, bd=2)
    nmentry.place(x=400, y=210)
    Phnentry = tk.Entry(nw, textvariable=Phn, bd=2)
    Phnentry.place(x=400, y=250)
    Timeentry = tk.Entry(nw, textvariable=Time, bd=2)
    Timeentry.place(x=400, y=300)
    Locationentry = tk.Entry(nw, textvariable=NameAddress, bd=2)
    Locationentry.place(x=400, y=350)

    def Booked():
        BDatestamp = datetime.datetime.now()
        nmentry1 = nmentry.get()
        Phnentry1 = Phnentry.get()
        Timeentry1 = Timeentry.get()
        Locationentry1 = Locationentry.get()
        y = dbcon.cursor()
        y.execute('SELECT Date,Ground_Location FROM GroundBooking WHERE Date=? AND Ground_Location=?',
                  (Timeentry1, Locationentry1))
        found1 = y.fetchone()
        if found1:
            messagebox.showinfo(
                'Oops!', 'ALREADY BOOKED, PLEASE TRY OTHER GROUND SLOTS')
            Book_now()
        else:
            print("booking start")
            dbcon.cursor()
            dbcon.execute('INSERT INTO GroundBooking(Date , NAME , PHONE_NUMBER , TIME_SLOT, Ground_Location)'
                         'VALUES(?,?,?,?,?)', (BDatestamp, nmentry1, Phnentry1, Timeentry1, Locationentry1))
            dbcon.commit()
            # connect.close()
            print("booking done")
            messagebox.showinfo("BOOKED", "BOOKING SUCCEFUL!!")

    btn2 = Button(nw, text="BOOK", font="tr 10", fg="black", bd=1,
                  bg="#c1bdfd", command=Booked).place(x=400, y=400)
    btn3 = Button(nw, text="BACK", font="tr 10", fg="black", bd=1,
                  bg="#c1bdfd", command=BookingPage).place(x=460, y=400)

def BookingHistory():
    hist = tk.Toplevel()
    hist.geometry("900x800+90+50")
    hist.title("BOOK")
    hist.configure(bg="white")
    frame8 = Frame(hist, bg="white").place(x=100, y=80, height=500, width=650)
    h0 = Label(hist, text="ENTER DETAILS", font="tr 20 bold",
               fg="#003b73", bg="white").place(x=300, y=100)
    h1 = Label(hist, text="NAME", font="tr 12 bold",
               fg="black", bg="white").place(x=150, y=210)
    h2 = Label(hist, text="PHONE NUMBER", font="tr 12 bold",
               fg="black", bg="white").place(x=400, y=210)
    h3 = Label(hist, text="Ground Location & Details",
               font="tr 12 bold", fg="black", bg="white").place(x=150, y=250)

    Booked_Location = ["SmashUp Ground : ADDRESS:- K.B. Patil School, Sector 8,Near Reena Mokal Hospital , Kandivali West, Mumbai, Maharashtra 400067, Phone:8852023645 ",
                       "J.K turf : ADDRESS :- Near scientific device company, Mumbra, Thane, Maharashtra 400612, Phone: 8254682025",
                       "Dribble Football Turf : ADDRESS :- Near vivana mall, Thane, Maharashtra 400612, Phone : 8254682025",
                       "Bhumiputra Maidan : ADDRESS :- Bhumiputra Maidan NEAR RAM MANDIR, DOMBIVILI , Thane, Maharashtra 400612, Phone: 8254682025",
                       "PHOENIX GROUND : ADDRESS :- Near midc water tank, Kalyan-Dmbivili, Thane, Maharashtra 400612, Phone:8254682025",
                       "DYANMANDIR GROUND : ADDRESS :- Near Mamta Hospital, model college, Dombivili, Thane, Maharashtra 400612, Phone: 8254682025"
                       ]  # Idhar locations change kar...

    Booked_NameAddress = StringVar()
    Booked_NameAddress.set(Booked_Location[0])
    drop3 = OptionMenu(hist, Booked_NameAddress, *Booked_Location)
    drop3.place(x=490, y=250, height=15, width=20)

    name = StringVar()
    phone = IntVar()

    Booked_name = tk.Entry(hist, textvariable=name, bd=2)
    Booked_name.place(x=225, y=210)
    Booked_phonenumber = tk.Entry(hist, textvariable=phone, bd=2)
    Booked_phonenumber.place(x=550, y=210)
    Booked_address = tk.Entry(hist, textvariable=Booked_NameAddress, bd=2)
    Booked_address.place(x=350, y=250)

    def Booking_History1():
        BDatestamp = datetime.datetime.now()
        bname = Booked_name.get()
        bphone = Booked_phonenumber.get()
        baddress = Booked_address.get()

        z = dbcon.cursor()
        z.execute('SELECT NAME,PHONE_NUMBER,Ground_Location FROM GroundBooking WHERE NAME=? AND PHONE_NUMBER=? AND Ground_Location=?',
                  (bname, bphone, baddress))
        found2 = z.fetchone()
        if found2:
            print("Booking found")
            dbcon.cursor()
            a = dbcon.execute('SELECT * FROM GroundBooking')
            b = Entry(hist, a, fg="black")
            # b.place(x=130, y=290, width=600, height=100)
            # b.insert(END,)
            i = 0
            for GroundBooking in a:
                for j in range(len(GroundBooking)):
                    b = Entry(hist, fg="black")
                    b.place(x=130, y=290, width=600, height=100)
                    b.insert(END, GroundBooking[j])
                    i = i+1
            b.place(x=150, y=290)
            dbcon.commit()
            dbcon.execute("SELECT * FROM student limit 0,10")
        else:
            messagebox.showinfo(
                'Sorry', 'THERE IS NO SUCH BOOKINGS', command=logininfo)
            result = Button(hist, text="SHOW RESULTS", font="tr 10", fg="black",
                            bd=1, bg="#c1bdfd", command=Booking_History1).place(x=370, y=500)




def shopequip():
    os.system('python cart.py')

def Team():
    os.system('python SchoolTeam.py')

def registerinfo():
    reg = tk.Toplevel()
    reg.geometry("900x700")
    reg.configure(bg="grey")
    reg.title("REGISTERATION")
    reg.resizable(False, False)

    headingFrame2 = Frame(reg, bg="#FFBB00", bd=5)
    headingFrame2.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabelr = Label(headingFrame2, text="ADD NEW USER",
                          bg='black', fg='white', font=('tr', 20))
    headingLabelr.place(relx=0, rely=0, relwidth=1, relheight=1)ijp

    Name = Label(reg, text="NAME", fg="black", bg="white",
                 font="Bold 10").place(x=250, y=200)
    Uname = Label(reg, text="USERNAME", fg="black", bg="white",
                  font="Bold 10").place(x=250, y=250)
    Pas = Label(reg, text="PASSWORD", fg="black", bg="white",
                font="Bold 10").place(x=250, y=300)
    Cpas = Label(reg, text=" CONFIRM PASSWORD", fg="black",
                 bg="white", font="Bold 10").place(x=250, y=350)
    Phn = Label(reg, text="PHONE NUMBER", fg="black",
                bg="white", font="Bold 10").place(x=250, y=400)
    Email = Label(reg, text="EMAIL_ID", fg="black", bg="white",
                  font="Bold 10").place(x=250, y=450)
    Type = Label(reg, text="Account Type", fg="black", bg="white",
                  font="Bold 10").place(x=250, y=500)
    print("registerinfo_start")
    RName = tk.Entry(reg)
    RName.place(x=450, y=200)
    RUname = tk.Entry(reg)
    RUname.place(x=450, y=250)
    RPas = tk.Entry(reg, show="*")
    RPas.place(x=450, y=300)
    RCpas = tk.Entry(reg, show="*")
    RCpas.place(x=450, y=350)
    RPhn = tk.Entry(reg)
    RPhn.place(x=450, y=400)
    REmail = tk.Entry(reg)
    REmail.place(x=450, y=450)
    RType = tk.Entry(reg)
    RType.place(x=450, y=500)

    Back1 = Button(reg, text="Back", font="tr 10", fg="black",
                   bg="#41B3A3", command=Back_page).place(x=650, y=620)

    def registerinfo1():
        print("registerinfo1")
        RDatestamp = datetime.datetime.now()
        RName1 = RName.get()
        RUname1 = RUname.get()
        RPas1 = RPas.get()
        RCpas1 = RPas.get()
        RPhn1 = RPhn.get()
        REmail1 = REmail.get()
        RType1 = RType.get()
        print("start")
        dbcon.execute("INSERT INTO Users(Date, Name, Username, Password, ConfirmPassword ,Phone_number , Email ,Type) "
                     "VALUES (?,?,?,?,?,?,?,?)", (RDatestamp, RName1, RUname1, RPas1, RCpas1, RPhn1, REmail1, RType1))
        # connect.execute(insert_command1 % (RDatestamp, RName1, RUname1, RPas1,RCpas1, RPhn1, REmail1))
        print("done")
        messagebox.showinfo("REGISTRATION SUCCESFUL!", "BACK TO LOGIN!")
        dbcon.commit()
        # connect.close()
    b = Button(reg, text="REGISTER", bg="white", fg="black",
               command=registerinfo1, bd=2).place(x=400, y=550)


B1 = tk.Button(LoginPage, text="LOGIN", command=logininfo).place(x=370, y=360)
B2 = tk.Button(LoginPage, text="REGISTER", command=registerinfo).place(x=470, y=360)

LoginPage.mainloop()