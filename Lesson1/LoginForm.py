from tkinter import*

root = Tk()
root.title("System Login")
root.geometry("300x180")

Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)

username_entry = Entry(root, width=20)
username_entry.grid(row=0, column=1, padx=10,pady=10)

password_entry = Entry(root, width=20, show = '*')
password_entry.grid(row=1, column=1, padx=10,pady=10)

def login():
    username = username_entry.get()
    password = password_entry.get()
    print("Username: ",username)
    print("Password: ",password)

def cancel():
    root.destroy()

login_btn = Button(root,text="Login",bg="lightgreen",width=10, command = login)
login_btn.grid(row=2, column=0, padx=10, pady=20)
cancel_btn = Button (root, text="Cancel", bg="salmon", width=10, command=cancel)
cancel_btn.grid(row=2,column=1,padx=10,pady=20)

root.mainloop()