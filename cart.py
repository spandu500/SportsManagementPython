
from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style
import tkinter as tk
from PIL import Image, ImageTk
#Its not pretty but it add and removes from list displays the list and has a quit button

class ShoppingCart(Frame):
    def __init__(self):
        super().__init__()
        self.shoppinglist = []
        self.adding = True
        self.initUI()


    def initUI(self):
        def press():
            sc.delete("1.0", tk.END)
            sc.insert(tk.END, getList(self))
            

        def addpress():
            self.adding=not self.adding
            if self.adding==True:
                ar['text'] = "Click to Start \r Removing"
                press()
            else:
                ar['text']="Click to Start \r Adding"
                press()

        def shop(s):
            if(self.adding==True):
                self.shoppinglist.append(s)
            else:
                if s in self.shoppinglist:
                    self.shoppinglist.remove(s)
                    

        self.master.title("Shop Items")

        spike = tk.Button(self, command=lambda:[shop("Spike Shoes"),press()])
        image = ImageTk.PhotoImage(file="shop/spike.jpg")
        spike.config(image=image, width=200, height=200, bg="white")
        spike.image = image
        spike.grid(row=2, column=1)

        ball = tk.Button(self, command=lambda:[shop("Ball 1"),press()])
        image = ImageTk.PhotoImage(file="shop/ball.jpg")
        ball.config(image=image, width=200, height=200, bg="white")
        ball.image = image
        ball.grid(row=2, column=2)

        bat = tk.Button(self, command=lambda: [shop("Bat"),press()])
        image = ImageTk.PhotoImage(file="shop/bat.jpg")
        bat.config(image=image, width=200, height=200, bg="white")
        bat.image = image
        bat.grid(row=2, column=3)

        cones = tk.Button(self, command=lambda:[shop("Cones"),press()])
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

        ar = tk.Button(self, text="Click to start \r Removing", bg="darkblue", fg="white", font='Helvetica 18 bold', width=15, height=5, command=lambda: [addpress()])
        ar.grid(row=3, column=5)

        quit = tk.Button(self, text="QUIT", fg="white", bg="red", font='Helvetica 18 bold', command=self.master.destroy, width=10, height=5)
        quit.grid(row=4, column=5)

        self.pack()


def getList(self):
    items='Your Shopping Cart Contains: \n'
    for item in self.shoppinglist:
        items+= item + "\n"
    return items

def mainshop():
    root = Tk()
    app = ShoppingCart()
    root.configure(background="white")
    bitem = tk.Button(root, text="Buy items", font="tr", fg="black",bd=4, bg="#E8A87C", activebackground="#C38D9E", activeforeground="PURPLE", command=print('items')) 
    bitem.place(x=865, y=400, width=160)
    root.mainloop()

if __name__ == '__main__':
    mainshop()
