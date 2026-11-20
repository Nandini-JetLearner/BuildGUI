from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("300x200")
Label(root, text = "I am a message box rawr rawr rawr",font="50").pack(pady=10)
messagebox.showinfo("Show Info", "Pretend this is some important information.")
messagebox.showwarning("Show Warning", "Pretend this is some important warning.")
messagebox.showerror("Show Error", "Pretend this is some important error and something went wrong.")
messagebox.askquestion("Ask Question", "Are you sure you were properly pretending for the previous questions?")
messagebox.askokcancel("Ask, Ok, Cancel", "Pretend you want to continue. Like actually.")
messagebox.askyesno("Yes or No, Be Honest!", "Are you really interested in doing this?")
messagebox.askretrycancel("Try Again?", "Do you want to try this whole thing again?")
root.mainloop()