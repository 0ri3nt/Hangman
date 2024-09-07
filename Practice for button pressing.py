from tkinter import *
from tkinter.messagebox import showinfo

def reply(name,inp):
    showinfo(title="Reply", message = "Hello %s! You hit the %s key." % (name,inp))


top = Tk()
top.title("Echo")

Label(top, text="Enter your name:").pack(side=TOP)
ent = Entry(top)
ent.bind("<Return>", (lambda event: reply(ent.get(),"Enter")))
ent.pack(side=TOP)
btn = Button(top,text="Submit", command=(lambda: reply(ent.get(),"Submit")))
btn.pack(side=LEFT)

top.mainloop()
