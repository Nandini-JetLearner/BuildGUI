from tkinter import*

root=Tk()
root.title("Bank Account")
root.geometry("600x400")
root.config(bg="dark blue")

Label(root, text="Bank Account Login", font = ("Arial",18,"bold"),bg="white").place(x=195,y=40)
Label(root, text="Type in your information:", font=("Arial",12), bg="white").place(x=230,y=85)

Label(root, text="Username: ", font=("Arial",8,"bold")).place(x=155,y=120)
Label(root, text="Password:", font=("Arial",8,"bold")).place(x=155,y=150)

username_entry = Entry(root, width=40)
username_entry.place(x=230,y=120)
password_entry = Entry(root, width=40, show = "#")
password_entry.place(x=230,y=150)

def login():
    message = Label(root, text=f"You are now logged into your account, {username_entry.get()}. ", font=("Arial",12), bg = "light blue")
    message.place(x=180,y=255)
def show():
    message2 = Label(root, text=f"Your password is {password_entry.get()}.", font=("Arial",12), bg = "light blue")
    message2.place(x=180,y=290)
    root.after(4000,lambda : message2.destroy())
   
login=Button(root,text="Login",bg="black", fg="gold",width = 15,command = login).place(x=260,y=190)
show=Button(root,text="Show Password",bg="black", fg="gold",width = 15,command = show).place(x=260,y=220)

root.mainloop()