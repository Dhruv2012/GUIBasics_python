from tkinter import *
root=Tk()
def leftclick(event):
    print("left")
    return

def middleclick(event):
    print("scroll")
    return

def rightclick(event):
    print("right")
    return

frame=Frame(root,width=300,height=250)
frame.bind("<Button-1>",leftclick)
frame.bind("<Button-2>",middleclick)
frame.bind("<Button-3>",rightclick)
frame.pack()

root.mainloop()