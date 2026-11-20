from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("Music Player")
root.config(bg="blue")
songslist=Frame(root, bg="light yellow").pack()

Label(songslist, text="Now Playing", font=("Times New Roman", 40,"bold")).pack(pady=20)
a=Listbox(songslist, height=50, width=60).pack(side= LEFT, pady=10)
a.insert(END,"Song A - The Intro","Song B - Cool Beats","Song C - Python Rap","Song D - Coding LoFi","Song E - The Outro")
scroll=Scrollbar(songslist,Orient=VERTICAL).pack(side=RIGHT, fill=Y)
scroll.config(command=a.yview)
a.config(yscrollcommand=scroll.set)

def play():
    Label(root, text="Your music has been paused.").pack(pady=5)
def pause():
    Label(root, text="Your music is playing.").pack(pady=5)
def next():
    Label(root, text="Next song playing.").pack(pady=5)

play=Button(root,text="Play", font= ("Times New Roman", 20), bg="gold", fg="black", command=play).pack(pady=20)
pause=Button(root,text="Pause", font= ("Times New Roman", 20), bg="gold", fg="black", command=pause).pack(pady=20)
next=Button(root,text="Next", font= ("Times New Roman", 20), bg="gold", fg="black", command=next).pack(pady=20)
root.mainloop()