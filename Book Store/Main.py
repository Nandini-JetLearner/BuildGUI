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

book_title = title_entry.get()
book_author = author_entry.get()

def save():
    global book_title, book_author
    inventory.append(book_title)
    message = Label(root, text=f"Saving {book_title} by {book_author} to inventory. ", font=("Times New Roman",12), bg = "light blue")
    message.place(x=180,y=290)
    root.after(4000,lambda : message.destroy())

def show():
    global book_title
    message2 = Label(root, text=f"Your books include {book_title}", font=("Times New Roman",12), bg = "light blue")
    message2.place(x=180,y=320)
    root.after(4000,lambda : message2.destroy())
   
save=Button(root,text="Save Book",bg="black", fg="white",width = 15,command = save).place(x=300,y=210)
show=Button(root,text="Show Inventory",bg="black", fg="white",width = 15,command = show).place(x=300,y=250)

root.mainloop()