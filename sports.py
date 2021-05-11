import sqlite3
import tkinter as tk
import datetime
from tkinter import *
import SchoolTeam
import shop
from PIL import ImageTk, Image  # PIL -> Pillow
from tkinter import ttk
from tkinter import messagebox
from tkinter import Scrollbar
import sports

connect = sqlite3.connect('sports.db')
connect.cursor()
connect.execute('CREATE TABLE IF NOT EXISTS Groundbooking(Date TEXT, NAME TEXT, PHONE_NUMBER INT, TIME_SLOT VARCHAR, Ground_Location VARCHAR )')

connect.execute(
    'CREATE TABLE IF NOT EXISTS Users(Date TEXT, Name TEXT, Username TEXT, Password TEXT,ConfirmPassword TEXT ,Phone_number INTEGER, Email TEXT, Type TEXT)')
connect.execute(
    'CREATE TABLE IF NOT EXISTS BookedGround(Date TEXT, NAME TEXT, Phone_number INTEGER, Ground_Location TEXT)')
connect.execute('CREATE TABLE IF NOT EXISTS equipment(eid varchar(30), title varchar(30), Manufacturer varchar(30), status varchar(30))')
connect.execute('CREATE TABLE IF NOT EXISTS equipment_issued(eid varchar(30), title varchar(30), Manufacturer varchar(30), status varchar(30))')

insert_command = """INSERT OR IGNORE INTO Users(date, username, password) VALUES('%s', '%s', '%s');"""

connect.execute(
    'CREATE TABLE IF NOT EXISTS ShopStonks(Date TEXT, ItemName TEXT, ItemDesc TEXT, Stocks INTEGER)')

# Enter Table Names here
equipmentTable = "equipent"  # equipment Table
issueTable = "equipment_issued"

root = tk.Tk()
root.geometry("900x600")
root.configure(bg="white")
root.title("LOGIN PAGE")
root.resizable(False, False)

# List To store all Equipment IDs
alleid = []

same = True
n = 0.25
# Adding a background image
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
Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="WELCOME TO\nSPORTS MANAGEMENT SYSTEM",
                     bg='black', fg='white', font=('tr', 20))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

frame1 = Frame(root, bg="white").place(x=300, y=200, height=200, width=300)
Label(root, text="By Anuj, Mitesh, Kunal & Anushka", font="tr 13 bold",
      fg="BLACK", bd=1, anchor="c").place(x=300, y=450)
USER = Label(root, text="USER_NAME", fg="Black",
             bg="white").place(x=340, y=250)
PASS = Label(root, text="PASSWORD", fg="Black", bg="white").place(x=340, y=300)
user_verify = StringVar()
pass_verify = StringVar()
username = tk.Entry(root, textvariable=user_verify)
username.place(x=450, y=250)
password = tk.Entry(root, textvariable=pass_verify, show="*")
password.place(x=450, y=300)


def Back_page():
    messagebox.showinfo("BACK", "Proceeding to Home Page")
    back = logininfo()


def logininfo():

    datestamp = datetime.datetime.now()
    username1 = username.get()
    password1 = password.get()
    x = connect.cursor()
    y =connect.cursor()
    # Find user If there is any take proper action
    x.execute('SELECT Username,Password,Type FROM Users WHERE Username=? AND Password=?',
              (username1, password1))
    y.execute('SELECT Type FROM Users WHERE Username=? AND Password=?',
              (username1, password1))
    found = x.fetchone()
    if found:
        connect.execute(insert_command % (datestamp, username1, password1))
        Type = y.fetchone()
        connect.commit()
        # connect.close()
        loggedin(Type)
    else:
        messagebox.showerror('Oops!', 'Username or Password is incorrect.')


def loggedin(Type):
    messagebox.showinfo("LOGIN!!", "LOGIN SUCCEFUL!! Welcome to The Club")
    window2 = Toplevel()
    window2.geometry("1000x1000")
    window2.configure(bg="orange")
    window2.title("HOME PAGE")
    window2.resizable(False, False)
    headingFrame1 = Frame(window2, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = Label(headingFrame1, text= f"Hello {Type} SELECT AN OPTION",
                         bg='black', fg='white', font=('tr', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(window2, text="Add Equipment Details",
                  bg='black', fg='white', command=addequipment)
    btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

    btn2 = Button(window2, text="Remove Equipment from Inventory",
                  bg='black', fg='white', command=delete)
    btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn3 = Button(window2, text="View Inventory",
                  bg='black', fg='white', command=View)
    btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn4 = Button(window2, text="Issue Items to Students",
                  bg='black', fg='white', command=issueBook)
    btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)



    if Type !="('Student',)":   #not working
        btn5 = Button(window2, text="Return Equipment", bg='black',
                  fg='white', command=returnBook)
        btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

        # coach = tk.Button(window2, text="MANAGE TEAMS", font="tr 20 bold", fg="black", bd=4, command=ecoach)
        # coach.place(x=150, y=100, width=600)

        btn6 = Button(window2, text="Book Turf/PlayGround",
                    bg='black', fg="white", bd=4, command=bookingPage1)
        btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)
        btn7 = Button(window2, text="Shop Equipments",
                    bg="black", fg = 'white', bd=4, command=equipmentShop)
        btn7.place(relx=0.28, rely=0.9, relwidth=0.45, relheight=0.1)
        btn8 = Button(window2, text="Ground Booking History",
                    bg="black", fg='white', bd=4, command=Booking_History)
        btn8.place(relx=0.28, rely=1.0, relwidth=0.45, relheight=0.1)


def match_info():
    # object of tkinter
    # and background set for light grey
    master = Tk()
    master.configure(bg='light grey')

    def cricket_info():

        try:
            match = sports.get_match(sports.CRICKET, e1.get(), e2.get())
            date.set(match.match_date)
            time.set(match.match_time)
            league.set(match.league)
            team1.set(match.home_team)
            team2.set(match.away_team)
            team1_score.set(match.away_score)
            team2_score.set(match.home_score)
            link.set(match.match_link)
        except:
            messagebox.showerror("showerror", "No match found")

    # Variable Classes in tkinter
    date = StringVar()
    time = StringVar()
    league = StringVar()
    team1 = StringVar()
    team2 = StringVar()
    team1_score = StringVar()
    team2_score = StringVar()
    link = StringVar()

    # Creating label for each information
    # name using widget Label
    Label(master, text="Team 1 :", bg="light grey").grid(row=0, sticky=W)
    Label(master, text="Team 2 :", bg="light grey").grid(row=1, sticky=W)
    Label(master, text="Date :", bg="light grey").grid(row=2, sticky=W)
    Label(master, text="Time :", bg="light grey").grid(row=3, sticky=W)
    Label(master, text="League :", bg="light grey").grid(row=4, sticky=W)
    Label(master, text="Team 1 :", bg="light grey").grid(row=5, sticky=W)
    Label(master, text="Team 2 :", bg="light grey").grid(row=6, sticky=W)
    Label(master, text="Team 1 score :", bg="light grey").grid(row=7, sticky=W)
    Label(master, text="Team 2 score :", bg="light grey").grid(row=8, sticky=W)
    Label(master, text="Link :", bg="light grey").grid(row=9, sticky=W)

    # Creating lebel for class variable
    # name using widget Entry
    Label(master, text="", textvariable=date,
          bg="light grey").grid(row=2, column=1, sticky=W)
    Label(master, text="", textvariable=time,
          bg="light grey").grid(row=3, column=1, sticky=W)
    Label(master, text="", textvariable=league,
          bg="light grey").grid(row=4, column=1, sticky=W)
    Label(master, text="", textvariable=team1,
          bg="light grey").grid(row=5, column=1, sticky=W)
    Label(master, text="", textvariable=team2,
          bg="light grey").grid(row=6, column=1, sticky=W)
    Label(master, text="", textvariable=team1_score,
          bg="light grey").grid(row=7, column=1, sticky=W)
    Label(master, text="", textvariable=team2_score,
          bg="light grey").grid(row=8, column=1, sticky=W)
    Label(master, text="", textvariable=link,
          bg="light grey").grid(row=9, column=1, sticky=W)

    e1 = Entry(master)
    e1.grid(row=0, column=1)

    e2 = Entry(master)
    e2.grid(row=1, column=1)

    # creating a button using the widget
    # Button that will call the submit function
    b = Button(master, text="Show", command=cricket_info)
    b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

    mainloop()


def Booking_History():
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

        z = connect.cursor()
        z.execute('SELECT NAME,PHONE_NUMBER,Ground_Location FROM BookedGround WHERE NAME=? AND PHONE_NUMBER=? AND Ground_Location=?',
                  (bname, bphone, baddress))
        found2 = z.fetchone()
        if found2:
            print("Booking found")
            connect.cursor()
            a = connect.execute('SELECT * FROM BookedGround')
            b = Entry(hist, a, fg="black")
            # b.place(x=130, y=290, width=600, height=100)
            # b.insert(END,)
            i = 0
            for BookedGround in a:
                for j in range(len(BookedGround)):
                    b = Entry(hist, fg="black")
                    b.place(x=130, y=290, width=600, height=100)
                    b.insert(END, BookedGround[j])
                    i = i+1
            b.place(x=150, y=290)
            connect.commit()
            connect.execute("SELECT * FROM student limit 0,10")
        else:
            messagebox.showinfo(
                'Sorry', 'THERE IS NO SUCH BOOKINGS', command=logininfo)
            result = Button(hist, text="SHOW RESULTS", font="tr 10", fg="black",
                            bd=1, bg="#c1bdfd", command=Booking_History1).place(x=370, y=500)


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
        y = connect.cursor()
        y.execute('SELECT TIME_SLOT,Ground_Location FROM BookedGround WHERE TIME_SLOT=? AND Ground_Location=?',
                  (Timeentry1, Locationentry1))
        found1 = y.fetchone()
        if found1:
            messagebox.showinfo(
                'Oops!', 'ALREADY BOOKED, PLEASE TRY OTHER GROUND SLOTS')
            Book_now()
        else:
            print("booking start")
            connect.cursor()
            connect.execute('INSERT INTO BookedGround(Datestamp , NAME , PHONE_NUMBER , TIME_SLOT, Ground_Location)'
                         'VALUES(?,?,?,?,?)', (BDatestamp, nmentry1, Phnentry1, Timeentry1, Locationentry1))
            connect.commit()
            # connect.close()
            print("booking done")
            messagebox.showinfo("BOOKED", "BOOKING SUCCEFUL!!")

    btn2 = Button(nw, text="BOOK", font="tr 10", fg="black", bd=1,
                  bg="#c1bdfd", command=Booked).place(x=400, y=400)
    btn3 = Button(nw, text="BACK", font="tr 10", fg="black", bd=1,
                  bg="#c1bdfd", command=bookingPage1).place(x=460, y=400)


def bookingPage1():
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
    # Next = Button(book, text="Next", font="tr 10", fg="black",
    #               bg="#41B3A3", command=bookingPage2).place(x=700, y=620)

def view_registered():
    book = tk.Toplevel()
    book.geometry("600x650")
    book.title("Registered Users")
    book.configure(bg="white")
    frame2 = Frame(book, bg="white").place(x=100, y=50, height=600, width=650)


def equipmentShop():
    equip = tk.Toplevel()
    equip.geometry("700x700")
    equip.title("BROWSE SHOPS")
    frame2 = Frame(equip, bg="white").place(x=100, y=50, height=600, width=650)

    # 1st Shop
    a1 = Label(equip, text="Prestige Sports ", font="tr 15",
               fg="black", bg="white").place(x=200, y=120, width=300)
    a2 = Label(equip, text="ADDRESS:", font="tr 10",
               fg="black", bg="white").place(x=120, y=150)
    a3 = Label(equip, text="Manek Complex, Shop No 9", font="tr 10",
               fg="black", bg="white").place(x=190, y=150)
    a4 = Label(equip, text="Sector-29, Vashi, Navi Mumbai, Maharashtra 400703",
               font="tr 10", fg="black", bg="white").place(x=190, y=170)
    a5 = Label(equip, text="Phone:", font="tr 10",
               fg="black", bg="White").place(x=120, y=200)
    a6 = Label(equip, text="8852023645", font="tr 10 ",
               fg="black", bg="White").place(x=180, y=200)
    b1 = Button(equip, text="Shop Now", font="tr 10",
                fg="black", bd=1, bg="#41B3A3", command=shop.cart())
    b1.place(x=300, y=250)

    # 2nd Shop
    b11 = Label(equip, text="Total Sports And Fitness", font="tr 15",
                fg="black", bg="white").place(x=200, y=300, width=300)
    b12 = Label(equip, text="ADDRESS:", font="tr 20",
                fg="black", bg="white").place(x=120, y=350)
    b13 = Label(equip, text="Shop 9, Plot-26,  opp Sai Udyaan",
                font="tr 10", fg="black", bg="white").place(x=190, y=350)
    b14 = Label(equip, text="Kausa, Mumbra, Thane, Maharashtra 400612",
                font="tr 10", fg="black", bg="white").place(x=190, y=370)
    b15 = Label(equip, text="Phone:", font="tr 10",
                fg="black", bg="White").place(x=120, y=390)
    b16 = Label(equip, text="8254682025", font="tr 10 ",
                fg="black", bg="White").place(x=180, y=390)
    b2 = Button(equip, text="Shop Now", font="tr 10",
                fg="black", bd=1, bg="#41B3A3", command=shop.cart())
    b2.place(x=300, y=420)


    # 3rd Shop
    b11 = Label(equip, text="Shakti Sports And Fitness", font="tr 15",
                fg="black", bg="white").place(x=200, y=300, width=300)
    b12 = Label(equip, text="ADDRESS:", font="tr 10",
                fg="black", bg="white").place(x=120, y=350)
    b13 = Label(equip, text="Shop 91, Plot-6,  opp Rk Colony",
                font="tr 10", fg="black", bg="white").place(x=190, y=350)
    b14 = Label(equip, text="Kharghar, Raigad, Maharashtra 400612",
                font="tr 10", fg="black", bg="white").place(x=190, y=370)
    b15 = Label(equip, text="Phone:", font="tr 10",
                fg="black", bg="White").place(x=120, y=390)
    b16 = Label(equip, text="825468545", font="tr 10 ",
                fg="black", bg="White").place(x=180, y=390)
    b2 = Button(equip, text="Shop Now", font="tr 10",
                fg="black", bd=1, bg="#41B3A3", command=shop.cart())
    b2.place(x=300, y=420)


def cartx(self):
    def press():
        sc.delete("1.0", tk.END)
        sc.insert(tk.END, getList(self))

    def addpress():
        self.adding = not self.adding
        if self.adding == True:
            ar['text'] = "Click to Start \r Removing"
            press()
        else:
            ar['text'] = "Click to Start \r Adding"
            press()

    def shop(s):
        if(self.adding == True):
            self.shoppinglist.append(s)
        else:
            if s in self.shoppinglist:
                self.shoppinglist.remove(s)

    self.master.title("Shop Items")

    spike = tk.Button(self, command=lambda: [shop("Spike Shoes"), press()])
    image = ImageTk.PhotoImage(file="shop/spike.jpg")
    spike.config(image=image, width=200, height=200, bg="white")
    spike.image = image
    spike.grid(row=2, column=1)

    ball = tk.Button(self, command=lambda: [shop("Ball 1"), press()])
    image = ImageTk.PhotoImage(file="shop/ball.jpg")
    ball.config(image=image, width=200, height=200, bg="white")
    ball.image = image
    ball.grid(row=2, column=2)

    bat = tk.Button(self, command=lambda: [shop("Bat"), press()])
    image = ImageTk.PhotoImage(file="shop/bat.jpg")
    bat.config(image=image, width=200, height=200, bg="white")
    bat.image = image
    bat.grid(row=2, column=3)

    cones = tk.Button(self, command=lambda: [shop("Cones"), press()])
    image = ImageTk.PhotoImage(file="shop/cones.jpg")
    cones.config(image=image, width=200, height=200, bg="white")
    cones.image = image
    cones.grid(row=2, column=4)

    gloves = tk.Button(self, command=lambda: [shop("Gloves"), press()])
    image = ImageTk.PhotoImage(file="shop/gloves.jpg")
    gloves.config(image=image, width=200, height=200, bg="white")
    gloves.image = image
    gloves.grid(row=3, column=1)

    football = tk.Button(self, command=lambda: [shop("Football"), press()])
    image = ImageTk.PhotoImage(file="shop/football.jpg")
    football.config(image=image, width=200, height=200, bg="white")
    football.image = image
    football.grid(row=3, column=2)

    raquet = tk.Button(self, command=lambda: [shop("Tennis Raquet"), press()])
    image = ImageTk.PhotoImage(file="shop/raquet.jpg")
    raquet.config(image=image, width=200, height=200, bg="white")
    raquet.image = image
    raquet.grid(row=3, column=3)

    jersey1 = tk.Button(self, command=lambda: [shop("Orange Jersey"), press()])
    image = ImageTk.PhotoImage(file="shop/jersey1.jpg")
    jersey1.config(image=image, width=200, height=200, bg="white")
    jersey1.image = image
    jersey1.grid(row=3, column=4)

    ball2 = tk.Button(self, command=lambda: [shop("Season Ball"), press()])
    image = ImageTk.PhotoImage(file="shop/ball2.jpg")
    ball2.config(image=image, width=200, height=200, bg="white")
    ball2.image = image
    ball2.grid(row=4, column=1)

    shorts = tk.Button(self, command=lambda: [shop("Outer Shorts"), press()])
    image = ImageTk.PhotoImage(file="shop/shorts.jpg")
    shorts.config(image=image, width=200, height=200, bg="white")
    shorts.image = image
    shorts.grid(row=4, column=2)

    jersey2 = tk.Button(self, command=lambda: [shop("Yellow Jersey"), press()])
    image = ImageTk.PhotoImage(file="shop/jersey2.jpg")
    jersey2.config(image=image, width=200, height=200, bg="white")
    jersey2.image = image
    jersey2.grid(row=4, column=3)

    socks = tk.Button(self, command=lambda: [shop("Long Socks"), press()])
    image = ImageTk.PhotoImage(file="shop/socks.jpg")
    socks.config(image=image, width=200, height=200, bg="white")
    socks.image = image
    socks.grid(row=4, column=4)

    sc = tk.Text(self, height=13, width=30)
    sc.insert(tk.END, getList(self))
    sc.grid(row=2, column=5)

    ar = tk.Button(self, text="Click to start \r Removing", bg="darkblue", fg="white",
                   font='Helvetica 18 bold', width=15, height=5, command=lambda: [addpress()])
    ar.grid(row=3, column=5)

    quit = tk.Button(self, text="QUIT", fg="white", bg="red",
                     font='Helvetica 18 bold', command=self.master.destroy, width=10, height=5)
    quit.grid(row=4, column=5)

    self.pack()


def getList(self):
    items = 'Your Shopping Cart Contains: \n'
    for item in self.shoppinglist:
        items += item + "\n"
    return items


def equipmentRegister():

    eid = equipmentInfo1.get()
    title = equipmentInfo2.get()
    Manufacturer = equipmentInfo3.get()
    status = equipmentInfo4.get()
    status = status.lower()

    insertequipments = "insert into "+equipmentTable + \
        " values('"+eid+"','"+title+"','"+Manufacturer+"','"+status+"')"
    try:
        connect.execute(insertequipments)
        connect.commit()
        messagebox.showinfo('Success', "equipment added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(eid)
    print(title)
    print(Manufacturer)
    print(status)

    root.destroy()


def addequipment():

    global equipmentInfo1, equipmentInfo2, equipmentInfo3, equipmentInfo4, Canvas1, equipmentTable, root

    root = Tk()
    root.title("Inventory")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add equipments",
                         bg='black', fg='white', font=('tr', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # equipment ID
    lb1 = Label(labelFrame, text="equipment ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    equipmentInfo1 = Entry(labelFrame)
    equipmentInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    equipmentInfo2 = Entry(labelFrame)
    equipmentInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # equipment Manufacturer
    lb3 = Label(labelFrame, text="Manufacturer : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    equipmentInfo3 = Entry(labelFrame)
    equipmentInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # equipment Status
    lb4 = Label(labelFrame, text="Status(Avail/issued) : ",
                bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    equipmentInfo4 = Entry(labelFrame)
    equipmentInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0',
                       fg='black', command=equipmentRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def deleteBook():

    eid = bookInfo1.get()

    deleteSql = "delete from "+equipmentTable+" where eid = '"+eid+"'"
    deleteIssue = "delete from "+issueTable+" where eid = '"+eid+"'"
    try:
        connect.execute(deleteSql)
        connect.commit()
        connect.execute(deleteIssue)
        connect.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")

    print(eid)

    bookInfo1.delete(0, END)
    root.destroy()


def delete():

    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Sports Equipment")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book",
                         bg='black', fg='white', font=('tr', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0',
                       fg='black', command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def issue():

    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    eid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extracteid = "select eid from "+equipmentTable
    try:
        connect.execute(extracteid)
        connect.commit()
        for i in connect:
            alleid.append(i[0])

        if eid in alleid:
            checkAvail = "select status from "+equipmentTable+" where eid = '"+eid+"'"
            connect.execute(checkAvail)
            connect.commit()
            for i in connect:
                check = i[0]

            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "insert into "+issueTable+" values ('"+eid+"','"+issueto+"')"
    show = "select * from "+issueTable

    updateStatus = "update "+equipmentTable + \
        " set status = 'issued' where eid = '"+eid+"'"
    try:
        if eid in alleid and status == True:
            connect.execute(issueSql)
            connect.commit()
            connect.execute(updateStatus)
            connect.commit()
            messagebox.showinfo('Success', "Book Issued Successfully")
            root.destroy()
        else:
            alleid.clear()
            messagebox.showinfo('Message', "Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo(
            "Search Error", "The value entered is wrong, Try again")

    print(eid)
    print(issueto)

    alleid.clear()


def issueBook():

    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    root = Tk()
    root.title("Issue Equipment")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book",
                         bg='black', fg='white', font=('tr', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0',
                      fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def returnn():

    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status

    eid = bookInfo1.get()

    extracteid = "select eid from "+issueTable
    try:
        connect.execute(extracteid)
        connect.commit()
        for i in connect:
            alleid.append(i[0])

        if eid in alleid:
            checkAvail = "select status from "+equipmentTable+" where eid = '"+eid+"'"
            connect.execute(checkAvail)
            connect.commit()
            for i in connect:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "delete from "+issueTable+" where eid = '"+eid+"'"

    print(eid in alleid)
    print(status)
    updateStatus = "update "+equipmentTable + \
        " set status = 'avail' where eid = '"+eid+"'"
    try:
        if eid in alleid and status == True:
            connect.execute(issueSql)
            connect.commit()
            connect.execute(updateStatus)
            connect.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            alleid.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo(
            "Search Error", "The value entered is wrong, Try again")

    alleid.clear()
    root.destroy()


def returnBook():

    global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1

    root = Tk()
    root.title("Return Equipment")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book",
                         bg='black', fg='white', font=('tr', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="Return", bg='#d1ccc0',
                       fg='black', command=returnn)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def View():

    root = Tk()
    root.title("Equipment")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Equipment",
                         bg='black', fg='white', font=('tr', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-40s%-30s%-20s" % ('eid', 'Title',
          'Manufacturer', 'Status'), bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)
    getEquipment = "select * from "+equipmentTable
    try:
        connect.execute(getEquipment)
        connect.commit()
        for i in connect:
            Label(labelFrame, text="%-10s%-30s%-30s%-20s" %
                  (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3',
                     fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def registerinfo():
    reg = tk.Toplevel()
    reg.geometry("900x700")
    reg.configure(bg="grey")
    reg.title("REGISTERATION")
    reg.resizable(False, False)

    # # Adding a background image
    # background_image = Image.open("sports.jpg")
    # [imageSizeWidth, imageSizeHeight] = background_image.size
    # newImageSizeWidth = int(imageSizeWidth*n)
    # if same:
    #     newImageSizeHeight = int(imageSizeHeight*n)
    # else:
    #     newImageSizeHeight = int(imageSizeHeight/n)

    # background_image = background_image.resize(
    #     (newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(background_image)
    # reg = Canvas(root)
    # reg.create_image(300, 340, image=img)
    # reg.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    # reg.pack(expand=True, fill=BOTH)

    # frame2 = Frame(reg, bg="white").place(x=180, y=80, height=600, width=600)
    # Label(reg, text="REGISTRATION", font="tr 20 bold",
    #       fg="Blue", anchor="c").place(x=350, y=150)

    headingFrame2 = Frame(reg, bg="#FFBB00", bd=5)
    headingFrame2.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabelr = Label(headingFrame2, text="ADD NEW USER",
                          bg='black', fg='white', font=('tr', 20))
    # ye idhar change kiya fir bhi main window me change hota hai
    headingLabelr.place(relx=0, rely=0, relwidth=1, relheight=1)
    # window close nahi hote automatically

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
        connect.execute("INSERT INTO Users(Date, Name, Username, Password, ConfirmPassword ,Phone_number , Email ,Type) "
                     "VALUES (?,?,?,?,?,?,?,?)", (RDatestamp, RName1, RUname1, RPas1, RCpas1, RPhn1, REmail1, RType1))
        # connect.execute(insert_command1 % (RDatestamp, RName1, RUname1, RPas1,RCpas1, RPhn1, REmail1))
        print("done")
        messagebox.showinfo("REGISTRATION SUCCESFUL!", "BACK TO LOGIN!")
        connect.commit()
        # connect.close()
    b = Button(reg, text="REGISTER", bg="white", fg="black",
               command=registerinfo1, bd=2).place(x=400, y=550)


B1 = tk.Button(root, text="LOGIN", command=logininfo).place(x=370, y=360)
B2 = tk.Button(root, text="REGISTER", command=registerinfo).place(x=470, y=360)

root.mainloop()
