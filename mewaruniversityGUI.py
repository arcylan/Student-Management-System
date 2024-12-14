from tkinter import *
from tkinter.ttk import *

#declare the window
win = Tk()

#set the window tittle
win.title("Mewar University Student Management System")

#set window width & height
win.geometry("700x400")

#set the background color
win.configure(bg="forestgreen")

#setting resizeable property
win.resizable(1,0)

#setting  window Background
#win.configure(color="light grey")

#cerating labels
lbl1 = Label(win,text="Roll Number: ",font=("century gothic",15))
lbl1.place(x=50,y=50)

lbl2 = Label(win,text="Student Name: ",font=("century gothic",15))
lbl2.place(x=50,y=90)

lbl3 = Label(win,text="Age: ",font=("century gothic",15))
lbl3.place(x=50,y=130)

lbl4 = Label(win,text="Sex: ",font=("century gothic",15))
lbl4.place(x=50,y=170)

lbl5 = Label(win,text="Course: ",font=("century gothic",15))
lbl5.place(x=50,y=210)

#creating Text Boxes
e1 = Entry(win)
e1.place(x=220,y=50)

e2 = Entry(win)
e2.place(x=220,y=90)

e3 = Entry(win)
e3.place(x=220,y=130)

e4 = Entry(win)
e4.place(x=220,y=170)

e5 = Entry(win)
e5.place(x=220,y=210)

#printing data
def submit():
 roll =e1.get()
 name =e1.get()
 age =e1.get()
 sex =e1.get()
 course =e1.get()

 if roll !="" and name!="" and age !="" and  sex!="" and course !="":
   print(roll,name,age,sex,course)
  
 else:
   print("Fill All The Boxes")  


#creating Button for submit
btn = Button(win,text="Submit",command=submit)
btn.place(x=250,y=250)

#creating button for Reset
btn1 = Button(win,text="Reset")
btn1.place(x=350,y=250)

#Infinite loop
win.mainloop()


