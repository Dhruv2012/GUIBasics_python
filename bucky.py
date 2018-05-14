from tkinter import *
root = Tk()
topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
button1=Button(topframe,text="e,k,fbekf",fg="RED")
button2=Button(topframe,text="e,",fg="PURPLE")
button3=Button(topframe,text="ekf",fg="RED")
button4=Button(bottomframe,text="e,k,fbekf",fg="RED")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()



root.mainloop()