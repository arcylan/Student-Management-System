from tkinter import *
from PIL import Image,ImageTk #this is for Jpg images
root = Tk()

root.geometry("1244x1000")

# image = PhotoImage(file=r"C:\Users\Arcylan Reyaz\Downloads\water-2748670_1280.png")
img = Image.open(r"C:\Users\Arcylan Reyaz\Downloads\beautiful-scenery-summit-mount-everest-covered-with-snow-white-clouds.jpg")
image = ImageTk.PhotoImage(img)

label = Label(image=image)
label.pack()



root.mainloop()