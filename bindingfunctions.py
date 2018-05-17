from tkinter import  *
root=Tk()
def clickevent(event):
    print ("mouse click occured")
    return

button=Button(root,text="dhruv")
#command=clickevent)
button.bind("<Button-1>",clickevent)
button.pack()
root.mainloop()