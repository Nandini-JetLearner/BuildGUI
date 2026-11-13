from tkinter import *
from tkinter.ttk import Progressbar
import random
window = Tk()
window.geometry("400x300")
window.config(bg="light blue")
menubar=Menu(window)

def login():
    Label(window, text="Email: ").pack(pady=10)
    email_entry= Entry(window,width=20)
    email_entry.pack(pady=10)
    Label(window, text="Password: ").pack(pady=10)
    password_entry=Entry(window,width=20)
    password_entry.pack(pady=10)
    def show():
        Label(window,text=f"You are now logged in, {email_entry.get()}. Your password is: {password_entry.get()}.", bg = "light blue", fg="black").pack(pady=10)
    Button(window,text="Login", width = 20,bg = "black", fg = "white", command=show).pack(pady=10)

def meal():
    Label(window, text="Which food item would you like: Salad, Sandwich, or Pizza? ").pack(pady=10)
    Spinbox(window,width=20, value = ("Salad","Sandwich","Pizza"), state="readonly").pack(pady=10)
    Label(window, text="Which drink item would you like: Water, Lemonade, or Coke? ").pack(pady=10)
    Spinbox(window,width=20, value= ("Water","Lemonade","Coke"), state="readonly").pack(pady=10)  
    def submit():
        p=Progressbar(window,orient=HORIZONTAL, length=100, maximum=100, mode="determinate")
        p.pack(pady=5)
        def update(value):
            if value<=100:
                p["value"]=value
                window.after(500,update,value+10)
            else:
                Label(window,text=f"Your food has been ordered!").pack(pady=5)
        update(0)
    Button(window,text="Submit Order",width=20,bg = "black", fg = "white",command=submit).pack(pady=10)

def deliver():
    x=random.randint(10,60)
    Label(window, text="Delivery Details ").pack(pady=10)
    Label(window, text="Name for the order:").pack(pady=10)
    y=Entry(window,width=20)
    y.pack(pady=10)
    Label(window, text="What neighborhood do you live in?").pack(pady=10)
    Spinbox(window,width=20, value= ("Glenmoor","Caney Creek","Brookwood"), state="readonly").pack(pady=10)  
    def submit():
        Label(window,text=f"Your food is on its way {y.get()}! It will take {str(x)} minutes").pack(pady=5)
    Button(window,text="Deliver Now",width=20,bg = "black", fg = "white",command=submit).pack(pady=10)

Order = Menu(window, bg="black", fg="white", tearoff = 0)
Order.add_command(label = "Login", command=login)
Order.add_command(label = "View Meal", command = meal)
Order.add_command(label="Delivery", command=deliver)
menubar.add_cascade(label = "Order", menu=Order)
window.config(menu=menubar)

window.mainloop()