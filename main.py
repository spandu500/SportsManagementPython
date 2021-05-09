import sqlite3
import tkinter as tk
import datetime
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
from tkinter import ttk
from tkinter import messagebox
from tkinter import Scrollbar

conn = sqlite3.connect('sports.db')
conn.cursor()
# Sidenote: your database does not have a PRIMARY KEY
# I made u_id the PRIMARY KEY
conn.execute('CREATE TABLE IF NOT EXISTS Groundbooking(Date TEXT, NAME TEXT, PHONE_NUMBER INT, TIME_SLOT VARCHAR, Ground_Location VARCHAR )')

conn.execute(
    'CREATE TABLE IF NOT EXISTS Users(Date TEXT, Name TEXT, Username TEXT, Password TEXT,ConfirmPassword TEXT ,Phone_number INTEGER, Email TEXT)')
conn.execute(
    'CREATE TABLE IF NOT EXISTS BookedGround(Date TEXT, username TEXT, password TEXT)')
insert_command = """INSERT OR IGNORE INTO login(datestamp, username, password) VALUES('%s', '%s', '%s');"""

root = tk.Tk()
root.geometry("900x600+90+50")
root.configure(bg="white")
root.title("LOGIN PAGE")
root.resizable(False, False)


same=True
n=0.25
# Adding a background image
background_image =Image.open("sports.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="WELCOME TO\nSPORTS MANAGEMENT SYSTEM", bg='black', fg='white', font=('tr',20))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

frame1 = Frame(root, bg ="white").place(x=300, y=200,height= 200, width=300)
# Label(root, text="SPORTS MANAGEMENT SYSTEM ", font="tr 20 bold",fg="BLUE", bd=1, anchor="c").place(x=250, y=200)
USER = Label(root, text="USER_NAME", fg="Blue", bg="white").place(x=340, y=250)
PASS = Label(root, text="PASSWORD", fg="Blue", bg="white").place(x=340, y=300)
user_verify = StringVar()
pass_verify = StringVar()
username = tk.Entry(root, textvariable=user_verify)
username.place(x=450, y=250)
password = tk.Entry(root, textvariable=pass_verify, show="*")
password.place(x=450, y=300)

def ecoach():
    mngteam = tk.Toplevel()
    mngteam.geometry("900x800+90+50")
    mngteam.title("Manage Team")

def Booking_History():
    hist=tk.Toplevel()
    hist.geometry("900x800+90+50")
    hist.title("BOOK")
    hist.configure(bg="white")
    frame8 = Frame(hist, bg="white").place(x=100, y=80, height=500, width=650)
    h0 = Label(hist, text="ENTER DETAILS", font="tr 20 bold", fg="#003b73", bg="white").place(x=300, y=100)
    h1 = Label(hist, text="NAME", font="tr 12 bold", fg="black", bg="white").place(x=150, y=210)
    h2 = Label(hist, text="PHONE NUMBER", font="tr 12 bold", fg="black", bg="white").place(x=400, y=210)
    h3 = Label(hist,text="Ground Location & Details", font="tr 12 bold", fg="black", bg="white" ).place(x=150,y=250)

    Booked_Location = ["SmashUp Ground : ADDRESS:- K.B. Patil School, Sector 8,Near Reena Mokal Hospital , Kandivali West, Mumbai, Maharashtra 400067, Phone:8852023645 ",
        "J.K turf : ADDRESS :- Near scientific device company, Mumbra, Thane, Maharashtra 400612, Phone: 8254682025",
        "GROUND IT UP : ADDRESS :- Near vivana mall, Thane, Maharashtra 400612, Phone : 8254682025",
        "SKYARCH GROUND : ADDRESS :- SKYARCH GROUND NEAR RAM MANDIR, DOMBIVILI , Thane, Maharashtra 400612, Phone: 8254682025",
        "PHOENIX GROUND : ADDRESS :- Near midc water tank, Kalyan-Dmbivili, Thane, Maharashtra 400612, Phone:8254682025",
        "DYANMANDIR GROUND : ADDRESS :- Near Mamta Hospital, model college, Dombivili, Thane, Maharashtra 400612, Phone: 8254682025"
        ]

    Booked_NameAddress = StringVar()
    Booked_NameAddress.set(Booked_Location[0])
    drop3 = OptionMenu(hist, Booked_NameAddress, *Booked_Location)
    drop3.place(x=490, y=250, height=15, width=20)

    name = StringVar()
    phone = IntVar()

    Booked_name=tk.Entry(hist,textvariable=name,bd=2)
    Booked_name.place(x=225,y=210)
    Booked_phonenumber=tk.Entry(hist, textvariable=phone, bd=2)
    Booked_phonenumber.place(x=550,y=210)
    Booked_address=tk.Entry(hist, textvariable=Booked_NameAddress,bd=2)
    Booked_address.place(x=350,y=250)

    def Booking_History1():
        BDatestamp = datetime.datetime.now()
        bname=Booked_name.get()
        bphone=Booked_phonenumber.get()
        baddress=Booked_address.get()

        z = conn.cursor()
        z.execute('SELECT NAME,PHONE_NUMBER,Ground_Location FROM BookedGround WHERE NAME=? AND PHONE_NUMBER=? AND Ground_Location=?',
                  (bname, bphone, baddress))
        found2 = z.fetchone()
        if found2:
            print("Booking found")
            conn.cursor()
            a=conn.execute('SELECT * FROM BookedGround')
            b=Entry(hist,a,fg="black")
            # b.place(x=130, y=290, width=600, height=100)
            # b.insert(END,)
            i=0
            for BookedGround in a:
               for j in range(len(BookedGround)):
                    b=Entry(hist,fg="black")
                    b.place(x=130,y=290, width= 600, height=100)
                    b.insert(END,BookedGround[j])
                    i=i+1
            b.place(x=150,y=290)
            conn.commit()
            conn.execute("SELECT * FROM student limit 0,10")
# i=0 
# for student in my_conn: 
#     for j in range(len(student)):
#         e = Entry(my_w, width=10, fg='blue') 
#         e.grid(row=i, column=j) 
#         e.insert(END, student[j])
#     i=i+1
# my_w.mainloop()
        else:
            messagebox.showinfo('Sorry','THERE IS NO SUCH BOOKINGS',command=logininfo)
    result=Button(hist,text="SHOW RESULTS", font="tr 10", fg="black", bd=1, bg="#c1bdfd", command=Booking_History1).place(x=370,y=500)

def Book_now():
    nw = tk.Toplevel()
    nw.geometry("900x800+100+50")
    nw.title("BOOK SLOT")
    nw.configure(bg="white")
    frame5 = Frame(nw, bg="white").place(x=100, y=80, height=500, width=650)
    lb = Label(nw, text="ENTER DETAILS", font="tr 20 bold", fg="#003b73", bg="white").place(x=320, y=150)
    lb1 = Label(nw, text="NAME", font="tr 12 bold", fg="black", bg="white").place(x=200, y=210)
    lb2 = Label(nw, text="PHONE NUMBER", font="tr 12 bold", fg="black", bg="white").place(x=200, y=250)
    lb3 = Label(nw, text="TIME SLOT", font="tr 12 bold", fg="black", bg="white").place(x=200, y=300)
    lb4 = Label(nw, text="Ground Location & Details", font="tr 12 bold", fg="black", bg="white" ).place(x=150,y=350)
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
                      "GROUND IT UP : ADDRESS :- Near vivana mall, Thane, Maharashtra 400612, Phone : 8254682025",
                      "SKYARCH GROUND : ADDRESS :- SKYARCH GROUND NEAR RAM MANDIR, DOMBIVILI , Thane, Maharashtra 400612, Phone: 8254682025",
                      "PHOENIX GROUND : ADDRESS :- Near midc water tank, Kalyan-Dmbivili, Thane, Maharashtra 400612, Phone:8254682025",
                      "DYANMANDIR GROUND : ADDRESS :- Near Mamta Hospital, model college, Dombivili, Thane, Maharashtra 400612, Phone: 8254682025"
                     ]
    NameAddress= StringVar()
    NameAddress.set(optNameAddress[0])
    drop2 = OptionMenu(nw,NameAddress,*optNameAddress)
    drop2.place(x=540,y=350,height=15,width=20)

    nmentry = tk.Entry(nw, textvariable=nme, bd=2)
    nmentry.place(x=400, y=210)
    Phnentry = tk.Entry(nw, textvariable=Phn, bd=2)
    Phnentry.place(x=400, y=250)
    Timeentry = tk.Entry(nw, textvariable=Time, bd=2)
    Timeentry.place(x=400, y=300)
    Locationentry=tk.Entry(nw, textvariable=NameAddress, bd=2)
    Locationentry.place(x=400,y=350)

    def Booked():
        BDatestamp = datetime.datetime.now()
        nmentry1= nmentry.get()
        Phnentry1= Phnentry.get()
        Timeentry1= Timeentry.get()
        Locationentry1 = Locationentry.get()
        y=conn.cursor()
        y.execute('SELECT TIME_SLOT,Ground_Location FROM BookedGround WHERE TIME_SLOT=? AND Ground_Location=?',
                  (Timeentry1,Locationentry1))
        found1=y.fetchone()
        if found1:
            messagebox.showinfo('Oops!', 'ALREADY BOOKED, PLEASE TRY OTHER GROUND SLOTS')
            Book_now()
        else:
            print("booking start")
            conn.cursor()
            conn.execute('INSERT INTO BookedGround(Datestamp , NAME , PHONE_NUMBER , TIME_SLOT, Ground_Location)'
                         'VALUES(?,?,?,?,?)', (BDatestamp, nmentry1, Phnentry1, Timeentry1,Locationentry1))
            conn.commit()
            #conn.close()
            print("booking done")
            messagebox.showinfo("BOOKED", "BOOKING SUCCEFUL!!")


    btn2 = Button(nw, text="BOOK", font="tr 10", fg="black", bd=1, bg="#c1bdfd", command=Booked).place(x=400,y=400)
    btn3 = Button(nw, text="BACK", font="tr 10", fg="black", bd=1, bg="#c1bdfd", command=bookingPage1).place(x=460,y=400)



def Back_page():
    messagebox.showinfo("BACK","Proceeding to Home Page")
    back=logininfo()
def Back_page1():
    messagebox.showinfo("BACK","Procceding to page 1")
    back1= bookingPage1()

def bookingPage2():
    nextlvl = tk.Toplevel()
    nextlvl.geometry("900x900+100+100")
    nextlvl.title("AVAILABLE GROUNDS")
    nextlvl.configure(bg="white")
    frame7 = Frame(nextlvl, bg="white").place(x=100, y=50, height=700, width=750)

    # 4th Ground
    d1 = Label(nextlvl, text="SKYARCH GROUND", font="tr 15", fg="black", bg="white").place(x=200, y=120, width=300)
    d2 = Label(nextlvl, text="ADDRESS:", font="tr 10", fg="black", bg="white").place(x=120, y=150)
    d3 = Label(nextlvl, text="SKYARCH GROUND NEAR RAM MANDIR ", font="tr 10", fg="black", bg="white").place(x=190, y=150)
    d4 = Label(nextlvl, text="DOMBIVILI , Thane, Maharashtra 400612", font="tr 10", fg="black", bg="white").place(x=190, y=170)
    d5 = Label(nextlvl, text="Phone:", font="tr 10", fg="black", bg="White").place(x=120, y=200)
    d6 = Label(nextlvl, text="8254682025", font="tr 10 ", fg="black", bg="White").place(x=180, y=200)
    b4 = Button(nextlvl, text="Book Now", font="tr 10", fg="black", bd=1, bg="#41B3A3", command=Book_now)
    b4.place(x=300, y=220)

    # 5th turf
    e1 = Label(nextlvl, text="PHOENIX GROUND", font="tr 15", fg="black", bg="white").place(x=200, y=300, width=300)
    e2 = Label(nextlvl, text="ADDRESS:", font="tr 10", fg="black", bg="white").place(x=120, y=350)
    e3 = Label(nextlvl, text="J.K turf, near midc water tank", font="tr 10", fg="black", bg="white").place(x=190, y=350)
    e4 = Label(nextlvl, text="Kalyan-Dmbivili, Thane, Maharashtra 400612", font="tr 10", fg="black", bg="white").place(x=190, y=370)
    e5 = Label(nextlvl, text="Phone:", font="tr 10", fg="black", bg="White").place(x=120, y=390)
    e6 = Label(nextlvl, text="8254682025", font="tr 10 ", fg="black", bg="White").place(x=180, y=390)
    b5 = Button(nextlvl, text="Book Now", font="tr 10", fg="black", bd=1, bg="#41B3A3", command=Book_now)
    b5.place(x=300, y=420)

    # 6th Ground
    f1 = Label(nextlvl, text="DYANMANDIR GROUND", font="tr 15", fg="black", bg="white").place(x=200, y=500, width=300)
    f2 = Label(nextlvl, text="ADDRESS:", font="tr 10", fg="black", bg="white").place(x=120, y=550)
    f3 = Label(nextlvl, text="DYANMANDIR GROUND, near Mamta Hospital, model college", font="tr 10", fg="black",bg="white").place(x=190, y=550)
    f4 = Label(nextlvl, text="Dombivili, Thane, Maharashtra 400612", font="tr 10", fg="black", bg="white").place(x=190,y=570)
    f5 = Label(nextlvl, text="Phone:", font="tr 10", fg="black", bg="White").place(x=120, y=600)
    f6 = Label(nextlvl, text="8254682025", font="tr 10 ", fg="black", bg="White").place(x=180, y=600)
    b3 = Button(nextlvl, text="Book Now", font="tr 10", fg="black", bd=1, bg="#41B3A3", command=Book_now)
    b3.place(x=300, y=620)

    Back1 = Button(nextlvl, text="Back", font="tr 10", fg="black", bg="#41B3A3", command=Back_page1).place(x=700, y=620)

def equipmentShop():
    equip = tk.Toplevel()
    equip.geometry("900x900+100+100")
    equip.title("BROWSE SHOPS")
    frame2 = Frame(equip, bg="white").place(x=100, y=50, height=700, width=750)

    # 1st Shop
    a1 = Label(equip, text="Prestige Sports ", font="tr 15", fg="black", bg="white").place(x=200, y=120,width=300)
    a2 = Label(equip, text="ADDRESS:", font="tr 10", fg="black", bg="white").place(x=120, y=150)
    a3 = Label(equip, text="Manek Complex, Shop No 9", font="tr 10", fg="black",bg="white").place(x=190, y=150)
    a4 = Label(equip, text="Sector-29, Vashi, Navi Mumbai, Maharashtra 400703", font="tr 10", fg="black", bg="white").place(x=190, y=170)
    a5 = Label(equip, text="Phone:", font="tr 10", fg="black", bg="White").place(x=120, y=200)
    a6 = Label(equip, text="8852023645", font="tr 10 ", fg="black", bg="White").place(x=180, y=200)
    b1 = Button(equip, text="Shop Now", font="tr 10", fg="black", bd=1, bg="#41B3A3", command=Book_now)
    b1.place(x=300, y=250)

    # 2nd Shop
    b11 = Label(equip, text="Total Sports And Fitness", font="tr 15", fg="black", bg="white").place(x=200, y=300, width=300)
    b12= Label(equip, text="ADDRESS:", font="tr 10", fg="black", bg="white").place(x=120, y=350)
    b13 = Label(equip, text="Shop 9, Plot-26,  opp Sai Udyaan", font="tr 10", fg="black", bg="white").place(x=190, y=350)
    b14 = Label(equip, text="Kausa, Mumbra, Thane, Maharashtra 400612", font="tr 10", fg="black", bg="white").place(x=190,y=370)
    b15= Label(equip, text="Phone:", font="tr 10", fg="black", bg="White").place(x=120, y=390)
    b16= Label(equip, text="8254682025", font="tr 10 ", fg="black", bg="White").place(x=180, y=390)
    b2 = Button(equip, text="Shop Now", font="tr 10", fg="black", bd=1, bg="#41B3A3", command=Book_now)
    b2.place(x=300, y=420)
    


def bookingPage1():
    book = tk.Toplevel()
    book.geometry("900x900+100+100")
    book.title("AVAILABLE GROUNDS")
    book.configure(bg="white")
    frame2 = Frame(book, bg="white").place(x=100, y=50, height=700, width=750)

    # 1st turf
    a1 = Label(book, text="SmashUp Ground ", font="tr 15", fg="black", bg="white").place(x=200, y=120,width=300)
    a2 = Label(book, text="ADDRESS:", font="tr 10", fg="black", bg="white").place(x=120, y=150)
    a3 = Label(book, text="K.B. Patil School, Sector 8,", font="tr 10", fg="black",bg="white").place(x=190, y=150)
    a4 = Label(book, text="Near Reena Mokal Hospital, Kandivali West, Mumbai, Maharashtra 400067", font="tr 10", fg="black", bg="white").place(x=190, y=170)
    a5 = Label(book, text="Phone:", font="tr 10", fg="black", bg="White").place(x=120, y=200)
    a6 = Label(book, text="8852023645", font="tr 10 ", fg="black", bg="White").place(x=180, y=200)
    b1 = Button(book, text="Book Now", font="tr 10", fg="black", bd=1, bg="#41B3A3", command=Book_now)
    b1.place(x=300, y=250)

    # 2nd turf
    b11 = Label(book, text="J.K turf", font="tr 15", fg="black", bg="white").place(x=200, y=300, width=300)
    b12= Label(book, text="ADDRESS:", font="tr 10", fg="black", bg="white").place(x=120, y=350)
    b13 = Label(book, text="J.K turf, near scientific device company", font="tr 10", fg="black", bg="white").place(x=190, y=350)
    b14 = Label(book, text="Kausa, Mumbra, Thane, Maharashtra 400612", font="tr 10", fg="black", bg="white").place(x=190,y=370)
    b15= Label(book, text="Phone:", font="tr 10", fg="black", bg="White").place(x=120, y=390)
    b16= Label(book, text="8254682025", font="tr 10 ", fg="black", bg="White").place(x=180, y=390)
    b2 = Button(book, text="Book Now", font="tr 10", fg="black", bd=1, bg="#41B3A3", command=Book_now)
    b2.place(x=300, y=420)

    # 3rd Ground
    c1 = Label(book, text="GROUND IT UP", font="tr 15", fg="black", bg="white").place(x=200, y=500, width=300)
    c2 = Label(book, text="ADDRESS:", font="tr 10", fg="black", bg="white").place(x=120, y=550)
    c3 = Label(book, text="J.K turf, near viviana mall", font="tr 10", fg="black", bg="white").place(x=190, y=550)
    c4 = Label(book, text="Thane, Maharashtra 400612", font="tr 10", fg="black", bg="white").place(x=190,y=570)
    c5 = Label(book, text="Phone:", font="tr 10", fg="black", bg="White").place(x=120, y=600)
    c6 = Label(book, text="8254682025", font="tr 10 ", fg="black", bg="White").place(x=180, y=600)
    b3 = Button(book, text="Book Now", font="tr 10", fg="black", bd=1, bg="#41B3A3", command=Book_now)
    b3.place(x=300, y=620)

    Back1 = Button(book, text="Back", font="tr 10", fg="black", bg="#41B3A3", command=Back_page).place(x=650, y=620)
    Next = Button(book, text="Next", font="tr 10", fg="black", bg="#41B3A3", command=bookingPage2).place(x=700, y=620)

def logininfo():

    datestamp = datetime.datetime.now()
    username1 = username.get()
    password1 = password.get()
    x = conn.cursor()
    # Find user If there is any take proper action
    x.execute('SELECT Username,Password FROM Users WHERE Username=? AND Password=?',
              (username1, password1))
    found = x.fetchone()
    if found:
        conn.execute(insert_command % (datestamp, username1, password1))
        conn.commit()
        #conn.close()
        messagebox.showinfo("LOGIN!!", "LOGIN SUCCEFUL!!")
        window2 = Toplevel()
        window2.geometry("900x600+100+50")
        window2.configure(bg="orange")
        window2.title("HOME PAGE")
        window2.resizable(False, False)
        headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        headingLabel = Label(headingFrame1, text="SELECT AN OPTION", bg='black', fg='white', font=('tr',20))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        coach = tk.Button(window2, text="MANAGE TEAMS", font="tr 20 bold", fg="black",bd=4, command=ecoach)
        coach.place(x=150, y=100, width=600)
        booking = tk.Button(window2, text="BOOK GROUND", font="tr 20 bold", fg="black",bd=4, command=bookingPage1)
        booking.place(x=150, y=200, width=600)
        equipment = tk.Button(window2, text="SHOP EQUIPMENTS", font="tr 20 bold", fg="black",bd=4, command=equipmentShop)
        equipment.place(x=150, y=300, width=600)
        booking_history = Button(window2, text="BOOKING HISTORY", font="tr 20 bold", fg="black", bd=4, command= Booking_History)
        booking_history.place(x=150, y=400, width=600)

    else:
        messagebox.showerror('Oops!', 'Username or Password is incorrect.')


def registerinfo():
    reg = tk.Toplevel()
    reg.geometry("900x600+100+50")
    reg.configure(bg="white")
    reg.title("REGISTERATION")
    reg.resizable(False, False)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="ADD NEW USER", bg='black', fg='white', font=('tr',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    frame2 = Frame(reg, bg="white").place(x=180, y=80, height=600, width=600)
    Label(reg, text="REGISTRATION", font="tr 20 bold",fg="Blue", anchor="c").place(x=350, y=150)
    Name = Label(reg, text="NAME", fg="black", bg="white",font="Bold 10").place(x=250, y=200)
    Uname = Label(reg, text="USERNAME", fg="black", bg="white",font="Bold 10").place(x=250, y=250)
    Pas = Label(reg, text="PASSWORD", fg="black", bg="white",font="Bold 10").place(x=250, y=300)
    Cpas = Label(reg, text=" CONFIRM PASSWORD", fg="black",bg="white", font="Bold 10").place(x=250, y=350)
    Phn = Label(reg, text="PHONE NUMBER", fg="black",bg="white", font="Bold 10").place(x=250, y=400)
    Email = Label(reg, text="EMAIL_ID", fg="black", bg="white",font="Bold 10").place(x=250, y=450)
    print("registerinfo_start")
    RName = tk.Entry(reg)
    RName.place(x=400, y=200)
    RUname = tk.Entry(reg)
    RUname.place(x=400, y=250)
    RPas = tk.Entry(reg,show="*")
    RPas.place(x=400, y=300)
    RCpas = tk.Entry(reg,show="*")
    RCpas.place(x=400, y=350)
    RPhn = tk.Entry(reg)
    RPhn.place(x=400, y=400)
    REmail = tk.Entry(reg)
    REmail.place(x=400, y=450)

    def registerinfo1():
        print("registerinfo1")
        RDatestamp = datetime.datetime.now()
        RName1 = RName.get()
        RUname1 = RUname.get()
        RPas1 = RPas.get()
        RCpas1 = RPas.get()
        RPhn1 = RPhn.get()
        REmail1 = REmail.get()
        print("start")
        conn.execute("INSERT INTO Users(Date, Name, Username, Password, ConfirmPassword ,Phone_number , Email ) "
                     "VALUES (?,?,?,?,?,?,?)", (RDatestamp, RName1, RUname1, RPas1, RCpas1, RPhn1, REmail1))
        # conn.execute(insert_command1 % (RDatestamp, RName1, RUname1, RPas1,RCpas1, RPhn1, REmail1))
        print("done")
        messagebox.showinfo("REGISTRATION SUCCESFUL!", "BACK TO LOGIN!")
        conn.commit()
        # conn.close()
    b = Button(reg, text="REGISTER", bg="white", fg="black",command=registerinfo1, bd=2).place(x=400, y=550)

B1 = tk.Button(root, text="LOGIN", command=logininfo).place(x=370, y=360)
B2 = tk.Button(root, text="REGISTER", command=registerinfo).place(x=470, y=360)

root.mainloop()
