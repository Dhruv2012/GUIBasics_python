from tkinter import *
root=Tk()
label1=Label(root,text="one",fg="red",bg="white")
label1.pack()
label2=Label(root,text="two",fg="green",bg="BLACK")
label2.pack(fill=X)
label3=Label(root,text="THREE",fg="BLUE",bg="white")
label3.pack(side=LEFT,fill=Y)







root.mainloop()

