
from tkinter import *
import sqlite3

class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        a=StringVar()
        b=StringVar()
        a1=StringVar()
        b1=StringVar()
        c=StringVar()

        self.button=Button(frame, text='Open Db', fg='red', command=self.ouvrir)        #ouvrir method called by command on mouse click
        self.button.pack(side=LEFT)

        self.button2=Button(frame, text='Create Table',fg='green', command=self.tabluh)   #tabluh method called by command on click
        self.button2.pack(side=LEFT)

        self.button3=Button(frame,text='Close Db',fg='blue',command=self.ferver)        #ferver method called on click
        self.button3.pack(side=LEFT)

        self.button4=Button(frame,text='Insert Rec',command=self.insertar)
        self.button4.pack(side=LEFT)

        self.button5=Button(frame,text='List Recs',command=self.listar)
        self.button5.pack(side=LEFT)

        self.a=Entry(frame)
        self.a.pack(side=BOTTOM)

        self.b=Entry(frame)
        self.b.pack(side=BOTTOM)

        self.c=Entry(frame)
        self.c.pack(side=BOTTOM)

    def ouvrir(self):
        #method which makes database.Its name may change
        self.con=sqlite3.connect('footballdb')
        self.cur=self.con.cursor()

    def tabluh(self):
        #method for creating table.Name may vary
        #self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE team(
        team_id INTEGER,
        team_name stringvar(20),
        team_players INTEGER)''')

    def ferver(self):
        self.con.close()

    def insertar(self):
        #self.con=sqlite3.connect('footballdb')          #doubt=why these 2 lines 
        #self.cur=self.con.cursor()                      #are again needed? not in original code
        a1=self.a.get()
        b1=self.b.get()
        c1=int(self.c.get())
        self.cur.execute('''insert into team(team_id,team_name,team_players) values(?,?,?)''',(c1,a1,b1))
        self.con.commit()

    def listar(self):
        self.cur.execute('SELECT * FROM team')
        print(self.cur.fetchall())


root = Tk()
root.title('Dbase R/W')
root.geometry('700x300')
app = App(root)
root.mainloop()