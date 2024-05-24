from tkinter import * 
from PIL import Image,ImageTk
root=Tk() 
root.title("Primary and Secondary Colours")
root.geometry("400x400") 
root.config(bg="#fcf5c7")
root.resizable(False,False) #Make sure that the page maintains its size at 400 by 400. 

 #Creating a label widget 
Label1=Label(root,text="Question 1", 
             font=("fixedsys",22,"bold"),
             bg="#fcf5c7",
             fg="black",
             padx=35,
             pady=30,
             wraplength=400,
             borderwidth=0,) #Creating a label widget 
Label1.pack()


