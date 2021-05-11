from tkinter import *

root = Tk()

def reciept():
    top = Toplevel()
    price1 = 3000
    qty1 = 3
    total1 = price1*qty1

    price2 = 5000
    qty2 = 4
    total2 = price1*qty2

    l = Label(top,text='---------DUMMY-RECIEPT----------')
    l.pack()
    heading = Label(top,text='PRICE\tQTY\tTOTAL')
    heading.pack()

    item1 = Label(top,text=f'{price1}\t{qty1}\t{total1}')
    item1.pack()

    item2 = Label(top,text=f'{price2}\t{qty2}\t{total2}')
    item2.pack()

b = Button(root,text='Print reciept',command=reciept)
b.pack(padx=10,pady=10)
root.mainloop()