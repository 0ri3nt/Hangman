from tkinter import *

global rw;rw = 0
def changed():
    global rw;rw += 1;
    if rw == 2:rw=0
    label.grid(row=rw,column=0)
root = Tk()
root.config(bg="pink")
frame = Frame(root, bg="sky blue")
frame.pack()

label = Label(frame,text="Hello")
label.grid(row=0,column=0)
b = Button(frame, text='Press me!', command=changed)
b.grid(row=0, column=1)

root.mainloop()