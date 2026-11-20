from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Music Player")
root.config(bg="sky blue")
songslist=Frame(root, bg="light yellow")
songslist.pack(pady=10)

Label(songslist, text="Now Playing", font=("Times New Roman", 40,"bold")).pack(pady=20)
a=Listbox(songslist, height=2, width=60)
a.pack(side= LEFT, pady=10)
a.insert(END,"Song A - The Intro","Song B - Cool Beats","Song C - Python Rap","Song D - Coding LoFi","Song E - The Outro")
scroll=Scrollbar(songslist,orient=VERTICAL)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=a.yview)
a.config(yscrollcommand=scroll.set)
a.selection_set(0)

def pause():
    Label(root, text="Your music has been paused.").pack(pady=5)

def play():
    Label(root, text="Your music is playing.").pack(pady=5)
    
def next():
    current = a.curselection()
    if current:
        next_song = current[0] + 1
        if next_song < a.size():
            a.selection_clear(0, END)
            a.selection_set(next_song)
            a.activate(next_song) 
            a.see(next_song)
    Label(root, text="Next song playing.").pack(pady=5)

def back():
    current = a.curselection()
    if current:
        next_song = current[0] - 1
        if next_song < a.size():
            a.selection_clear(0, END)
            a.selection_set(next_song)
            a.activate(next_song) 
            a.see(next_song)
        if next_song < current[0]:
            a.selection_clear(0, END)
            a.selection_set(0)
            a.activate(0) 
            a.see(0)
    Label(root, text="Previous song playing.").pack(pady=5)

Button(root,text="Play", font= ("Times New Roman", 20), bg="gold", fg="black", command=play).pack(pady=20)
Button(root,text="Pause", font= ("Times New Roman", 20), bg="gold", fg="black", command=pause).pack(pady=20)
Button(root,text="Next", font= ("Times New Roman", 20), bg="gold", fg="black", command=next).pack(pady=20)
Button(root,text="Back", font= ("Times New Roman", 20), bg="gold", fg="black", command=back).pack(pady=20)
root.mainloop()