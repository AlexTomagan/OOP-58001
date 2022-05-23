from tkinter import *

window= Tk()
window.geometry("400x300+20+10")
window.title("Tomagan Final Exam")
class MyWindow:
    def __init__(self,window):
        self.lbl1 = Label(window,text="Input 1st Number:")
        self.lbl1.place(x=50,y=80)
        self.txtfld1 = Entry(window,bd=3)
        self.txtfld1.place(x=180,y=80)
        self.lbl2=Label(window,text="Input 2nd Number:")
        self.lbl2.place(x=50,y=120)
        self.txtfld2 = Entry(window,bd=3)
        self.txtfld2.place(x=180,y=120)
        self.lbl3 = Label(window, text="Input 3rd Number:")
        self.lbl3.place(x=50, y=140)
        self.txtfld3 = Entry(window, bd=3)
        self.txtfld3.place(x=180, y=140)
mywin=MyWindow(window)
window.mainloop()