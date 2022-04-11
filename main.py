from tkinter import *
window = Tk()

def click():
    print("Alexander A Tomagan")

window.geometry("400x150+10+20")
window.title("Program 2")

label=Label(window,text = "Enter your fullname:",  fg = "red")
label.place(x=90,y=170)

txtfld = Entry(window,text = "Alexander A Tomagan", bd = 5)
txtfld.place(x=210,y=170)

button=Button(window,text = "click to display your full name", fg = "red")
button.config(command=click) #perform call back of function
button.place(x=40,y=200)

txtfld = Entry(window,text = "Alexander A Tomagan", bd = 5)
txtfld.place(x=210,y=200)
window.mainloop()



