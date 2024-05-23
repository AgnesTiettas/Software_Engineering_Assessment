from tkinter import * 
from PIL import Image,ImageTk
root=Tk() 
root.title("Primary and Secondary Colours")#Title for the window
root.geometry("400x400") #Window size 
root.config(bg="#fcf5c7")
root.resizable(False,False) #Make sure that the page maintains its size at 400 by 400.  

def homepage(): # Move to the colour_information page. 
    root.destroy()
    import Primary_and_Secondary_Colours

def Quiz(): # Move to the colour_information page. 
    root.destroy()
    import Quiz


 #Creating a label widget 
Label1=Label(root,text="Let's Learn about Primary and Secondary Colours", 
             font=("fixedsys",13),
             bg= "#fcf5c7", 
             fg="black",
             padx=20,
             pady=10,
             relief="flat",
             wraplength=300,
             borderwidth=10,)
Label1.pack() 



label2=Label(root,text="Primary Colours", 
            font=("fixedsys",12),
            padx=20,
            pady=25, 
            bg="#fcf5c7", 
            borderwidth=2,)
label2.pack()

label3=Label(root,text="", 
            font=("fixedsys",11),
            padx=20,
            pady=25, 
            bg="#fcf5c7", 
            borderwidth=2,)
label3.pack()


Quiz_button=Button(root,text="Quiz",
               font=("fixedsys",16),
               pady=20, 
               padx=80,
               bg="#adf7b6", 
               command=Quiz) 
Quiz_button.pack() 

Home_button=Button(root,text="HOME",
               font=("fixedsys",14),
               pady=10, 
               padx=40,
               justify=RIGHT,
               bg="#adf7b6", 
               command=homepage) 
Home_button.pack(side=BOTTOM) 

root.mainloop()