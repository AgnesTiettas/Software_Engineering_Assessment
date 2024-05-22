from tkinter import * 
from PIL import Image,ImageTk
root=Tk() 
root.title("Simple Colour Wheel")
root.geometry("400x400") 
root.resizable(False,False) #Make sure that the page maintains its size at 400 by 400.  

Label1=Label(root,text="Primary and Secondary Colours", 
             font=("Veranda",20),
             bg= "#d5bdaf", 
             fg="black",
             padx=20,
             pady=10,
             relief="raised",
             borderwidth=0,) #Creating a label widget 
Label1.pack() 

root.mainloop()