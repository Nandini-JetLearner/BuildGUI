from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("Shopping Cart")
root.config(bg="grey")
cart=Frame(root, bg="light pink").pack()

Label(cart, text="Your Items", font=("Times New Roman", 40,"bold")).pack(pady=20)
Shop = Listbox(cart, height=50, width=60).pack(side= LEFT, pady=10)
for i in range(1,100):
    Shop.insert(END,"Grocery Item "+ str(i))
scroll=Scrollbar(cart,Orient=VERTICAL).pack(side=RIGHT, fill=Y)
scroll.config(command=Shop.yview)
Shop.config(yscrollcommand=scroll.set)

def button():
    Label(root, text="You have been checked out. Have a good day!").pack(pady=5)
Button(root,text="CHECKOUT", font= ("Times New Roman", 20), bg="gold", fg="black", command=button).pack(pady=20)
root.mainloop()