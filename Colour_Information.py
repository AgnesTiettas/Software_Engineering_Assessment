from tkinter import *  #Imports the tkinter module
from PIL import Image,ImageTk
root=Tk() 
root.title("Primary and Secondary Colours")#Title for the window
root.geometry("400x400") #Window size 
root.config(bg="#fcf5c7")
root.resizable(False,False) #Makes the window non-resizable.  

def homepage(): # Move back to the homepage. 
    root.destroy()
    import Primary_and_Secondary_Colours

def Quiz(): # Move to the Quiz page. 
    root.destroy()
    import Quiz


#Creating a label widget for the page header
Label1=Label(root,text="Let's Learn!", 
             font=("fixedsys",18,"bold"),
             bg= "#fcf5c7", 
             fg="black",
             padx=20,
             pady=10,
             relief="flat",
             wraplength=350,
             borderwidth=5,)
Label1.pack() 


# Primary Colours subheading 
label2=Label(root,text="Primary Colours", 
            font=("fixedsys",13,"underline"),
            padx=20,
            pady=15, 
            bg="#fcf5c7", 
            borderwidth=2,)
label2.place(x=100, y=40)

#Creates the labels for the different primary colours. 
ColourLabel=Label(root, text="Red", 
                  bg="Red",
                  pady=4,
                  padx=10,
                  font=("fixedsys",12),)
ColourLabel.place(x=100,y=80)


ColourLabel2=Label(root, text="Yellow",
                   bg="yellow",
                   pady=4,
                   padx=10,
                   font=("fixedsys",12),)
ColourLabel2.place(x=160, y=80)

ColourLabel3=Label(root, text="Blue",
                   bg="#0e0eff",
                   pady=4,
                   padx=10,
                   font=("fixedsys",12),)
ColourLabel3.place(x=240, y=80)

#Primary Colours information 
label4=Label(root,text="Colours which cannot be made by mixing other colours together, instead they are used to create other colours.There are three primary colours: Red, Yellow, and Blue.", 
            font=("fixedsys",9),
            padx=20,
            pady=5, 
            bg="#fcf5c7", 
            wraplength=390,
            borderwidth=0,)
label4.place(x=0,y=105)

label5=Label(root,text="Secondary Colours", 
            font=("fixedsys",13,"underline"),
            padx=20,
            pady=10, 
            bg="#fcf5c7", 
            borderwidth=2,)
label5.place(x=100, y=175)


#Creates the labels for the different primary colours. 
ColourLabe6=Label(root, text="Green", 
                  bg="green",
                  pady=4,
                  padx=10,
                  font=("fixedsys",12),)
ColourLabe6.place(x=85,y=210)


ColourLabel7=Label(root, text="Orange",
                   bg="orange",
                   pady=4,
                   padx=10,
                   font=("fixedsys",12),)
ColourLabel7.place(x=160, y=210)

ColourLabel8=Label(root, text="Purple",
                   bg="purple",
                   pady=4,
                   padx=10,
                   font=("fixedsys",12),)
ColourLabel8.place(x=240, y=210)



label9=Label(root,text="Colours created by mixing equal amounts of two primary colours. The secondary colours are orange, green and purple.", 
            font=("fixedsys",10),
            padx=20,
            pady=5, 
            bg="#fcf5c7", 
            wraplength=380,
            borderwidth=0,)
label9.place(x=0,y=235)


label10=Label(root,text="Blue + Yellow = Green", 
            font=("fixedsys",10),
            padx=5,
            pady=5, 
            bg="#fcf5c7", 
            borderwidth=0,)
label10.place(x=110,y=285)

label11=Label(root,text="Red + Blue = Purple", 
            font=("fixedsys",10),
            padx=5,
            pady=5, 
            bg="#fcf5c7", 
            borderwidth=0,)
label11.place(x=115,y=303)

label12=Label(root,text="Red + Yellow = Orange", 
            font=("fixedsys",10),
            padx=5,
            pady=5, 
            bg="#fcf5c7", 
            borderwidth=0,)
label12.place(x=110,y=321)

#Home button that goes back to the first page. 
Home_button=Button(root,text="HOME",
               font=("fixedsys",14),
               pady=8, 
               padx=25,
               bg="#adf7b6", 
               command=homepage) 
Home_button.place(x=15, y=345) 


#
Quiz_button=Button(root,text="NEXT",
               font=("fixedsys",14),
               pady=8, 
               padx=25,
               bg="#adf7b6", 
               command=Quiz) 
Quiz_button.place(x=280,y=345) 

root.mainloop()