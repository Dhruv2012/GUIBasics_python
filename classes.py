from  tkinter import  *


class window:
    # master is equivalent to root
    def achieved(self):
        print="success achieved"
        #return

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.printbutton = Button(frame ,text="success",command=self.achieved)
        self.printbutton.pack()

        self.quit = Button(frame, text="quit", command=frame.quit)
        self.quit.pack()
        return


root = Tk()
w = window(root)
root.mainloop()


