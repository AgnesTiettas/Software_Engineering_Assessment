from tkinter import * #imports all symbols from tkinter module into the current namespace 
from PIL import Image,ImageTk
root=Tk() 
root.title("Primary and Secondary Colours")
root.geometry("410x410") #Make sure that the page maintains its size at 410 by 450. 
root.config(bg="#fcf5c7") # Sets the background colour of the page. 
root.resizable(False,False) #Make sure that the page is not resizable.  


def page2(): # Move to the colour_information page. 
     root.destroy()#Destroys the current window.
     import Colour_Information #Imports the colour information page.

    

#Header of the page 
Header=Label(root,text="Primary and Secondary Colours", 
             font=("fixedsys",24,"bold"),
             bg="#fcf5c7",
             fg="black",
             padx=35,
             pady=30,
             wraplength=400,
             borderwidth=0,) #Creating a label widget 
Header.pack() 

#Subheading for page
Subheading=Label(root,text="Let's Learn about Primary and Secondary Colours!", 
             font=("fixedsys",16), 
             bg="#fcf5c7",
             fg="black",
             wraplength=300,# Makes the text stay within the window 
             padx=0,
             pady=30,
             borderwidth=0,) #Creating a label widget 
Subheading.pack()



#Creates a start button that moves user to the Colour_Information page. 
Start_button=Button(root,text="START",
               font=("fixedsys",20),
               pady=20, 
               padx=60,
               bg="#adf7b6", 
               command=page2) 
Start_button.pack() 

#Start button subheading providing instructions.
Button_Subheading=Label(root,text="Click to begin", 
             font=("fixedsys",12,"italic"), 
             bg="#fcf5c7",
             fg="black",
             padx=20,
             pady=10,
             relief="flat",
             borderwidth=0,) #Creating a label widget 
Button_Subheading.pack()  


root.mainloop()
