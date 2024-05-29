from tkinter import * 
from PIL import Image,ImageTk
root=Tk() 
root.title("Primary and Secondary Colours")
root.geometry("450x450") 
root.config(bg="#fcf5c7")
root.resizable(False,False) #Make sure that the page maintains its size at 400 by 400. 


def page2(): # Move to the colour_information page. 
    root.destroy()
    import Colour_Information
    


Label1=Label(root,text="Primary and Secondary Colours", 
             font=("fixedsys",24,"bold"),
             bg="#fcf5c7",
             fg="black",
             padx=35,
             pady=30,
             wraplength=400,
             borderwidth=0,) #Creating a label widget 
Label1.pack() 


Label2=Label(root,text="Let's Learn about Primary and Secondary Colours!", 
             font=("fixedsys",16), 
             bg="#fcf5c7",
             fg="black",
             wraplength=300,# Makes the text stay within the window 
             padx=0,
             pady=30,
             borderwidth=0,) #Creating a label widget 
Label2.pack()



button1=Button(root,text="START",
               font=("fixedsys",20),
               pady=20, 
               padx=60,
               bg="#adf7b6", 
               command=page2) 
button1.pack() 


Label3=Label(root,text="Click to begin", 
             font=("fixedsys",12,"italic"), 
             bg="#fcf5c7",
             fg="black",
             padx=20,
             pady=10,
             relief="flat",
             borderwidth=0,) #Creating a label widget 
Label3.pack()  



root.mainloop()
