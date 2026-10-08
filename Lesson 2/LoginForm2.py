from tkinter import*

root=Tk()
root.title("Greeting App")
root.geometry("400x400")
root.config(bg="light blue")

Label(root, text="Greeting App", font = ("Arial",18,"bold"),bg="light blue").grid(row=0, column=1,padx=80,pady=30)

Label(root, text="Enter your name:", font=("Times New Roman",8), bg="light blue").grid(row=1, column=1,padx=75)

name_entry = Entry(root, width=40)
name_entry.grid(row=2, column=1,padx=80,pady = 10)

def greet():
    Label(root, text=f"Hello {name_entry.get()}. Welcome to Python!", font=("Times New Roman",8), bg = "light blue").grid(row=4, column=1,padx=80,pady=30)


greetbutton=Button(root,text="Greet Me!",bg="dark blue", fg="white",width = 15,command = greet)
greetbutton.grid(row = 3,column=1,padx=80,pady=10)

root.mainloop()