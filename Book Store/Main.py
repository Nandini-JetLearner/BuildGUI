import time
from tkinter import*

root=Tk()
root.title("Book Store Inventory")
root.geometry("640x400")
root.config(bg="light pink")

inventory = []

Label(root, text="Book Store Inventory", font = ("Arial",18,"bold"),bg="light green").place(x=195,y=40)
Label(root, text="Type in the following:", font=("Times New Roman",8), bg="light green").place(x=270,y=85)


Label(root, text="Title:", font=("Times New Roman",8)).place(x=170,y=120)
Label(root, text="Author:", font=("Times New Roman",8)).place(x=170,y=150)
Label(root, text="Price:", font=("Times New Roman",8)).place(x=170,y=180)



title_entry = Entry(root, width=40)
title_entry.place(x=230,y=120)
author_entry = Entry(root, width=40)
author_entry.place(x=230,y=150)
price_entry = Entry(root, width=40).place(x=230,y=180)


def save():
    inventory.append(str(title_entry.get()))
    message = Label(root, text=f"Saving {title_entry.get()} by {author_entry.get()} to inventory. ", font=("Times New Roman",12), bg = "light blue").place(x=180,y=290)
    root.after(5000,Label.place_forget())

def show():
    message2 = Label(root, text=f"Your books include {inventory}", font=("Times New Roman",12), bg = "light blue").place(x=180,y=320)
    root.after(5000,message2.destroy())


save=Button(root,text="Save Book",bg="black", fg="white",width = 15,command = save).place(x=300,y=210)
show=Button(root,text="Show Inventory",bg="black", fg="white",width = 15,command = show).place(x=300,y=250)

root.mainloop()