from tkinter import *
root=Tk()
root.geometry("1000x800")
root.configure(bg="dark green")

def add():
    print("clicked")
def addd():
    print("again clicked")    
f1 = Frame(root)
f1.place(x=10,y=50)
b1 = Button(f1,text="click",fg="black",command=add)
b1.pack(side=LEFT,anchor="nw")
b1 = Button(f1,text="click again",fg="black",command=addd)
b1.pack(side=LEFT,anchor="nw")





root.mainloop()