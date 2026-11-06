from tkinter import *
from tkinter.ttk import Progressbar
window = Tk()
window.geometry("400x300")
window.config(bg="light blue")

menubar=Menu(window)
loginframe=Frame(window)
mealframe=Frame(window)

def login():
    mealframe.pack_forget()
    Label(loginframe, text="Email: ").pack(pady=10)
    email_entry= Entry(loginframe,width=20)
    email_entry.pack(pady=10)
    Label(loginframe, text="Password: ").pack(pady=10)
    password_entry=Entry(loginframe,width=20)
    password_entry.pack(pady=10)
    def show():
        Label(loginframe,text=f"You are now logged in, {email_entry.get()}. Your password is: {password_entry.get()}.", bg = "light blue", fg="black").pack(pady=10)
    Button(loginframe,text="Login", width = 20,bg = "black", fg = "white", command=show).pack(pady=10)

def meal():
    loginframe.pack_forget()
    Label(mealframe, text="Which food item would you like: Salad, Sandwich, or Pizza? ").pack(pady=10)
    Spinbox(mealframe,width=20, value = ("Salad","Sandwich","Pizza"), state="readonly").pack(pady=10)
    Label(mealframe, text="Which drink item would you like: Water, Lemonade, or Coke? ").pack(pady=10)
    Spinbox(mealframe,width=20, value= ("Water","Lemonade","Coke"), state="readonly").pack(pady=10)  
    def submit():
        p=Progressbar(mealframe,orient=HORIZONTAL, length=100, maximum=100, mode="determinate")
        p.pack(pady=5)
        def update(value):
            if value<=100:
                p["value"]=value
                mealframe.after(500,update,value+10)
            else:
                Label(mealframe,text=f"Your food has been ordered!").pack(pady=5)
        update(0)
    Button(mealframe,text="Submit Order",width=20,bg = "black", fg = "white",command=submit).pack(pady=10)

Order = Menu(window, bg="black", fg="white", tearoff = 0)
Order.add_command(label = "Login", command=login)
Order.add_command(label = "View Meal", command = meal)
menubar.add_cascade(label = "Order", menu=Order)
window.config(menu=menubar)

window.mainloop()