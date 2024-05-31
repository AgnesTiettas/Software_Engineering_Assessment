from tkinter import *  #Imports the tkinter module
root=Tk() 
root.title("Primary and Secondary Colours")#Title for the window
root.geometry("410x410") #Window size 
root.config(bg="#fcf5c7")
root.resizable(False,False) #Makes the window non-resizable.  

def homepage(): # Move back to the homepage. 
    root.destroy()
    import Primary_and_Secondary_Colours

def Quiz(): # Move to the Quiz page. 
    root.destroy()
    import Quiz


#Creating a label widget for the page header
Page_header=Label(root,text="Let's Learn!", 
             font=("fixedsys",18,"bold"),
             bg= "#fcf5c7", 
             fg="black",
             padx=20,
             pady=10,
             relief="flat",
             wraplength=350,
             borderwidth=5,)
Page_header.pack() 


# Primary Colours subheading 
Primary_colours_subheading=Label(root,text="Primary Colours", 
            font=("fixedsys",13,"underline"),
            padx=20,
            pady=15, 
            bg="#fcf5c7", 
            borderwidth=2,)
Primary_colours_subheading.place(x=100, y=40)

#Creates the labels for the different primary colours. 
ColourLabel_red=Label(root, text="Red", 
                  bg="Red",
                  pady=4,
                  padx=10,
                  font=("fixedsys",12),)
ColourLabel_red.place(x=100,y=80)


ColourLabel_yellow=Label(root, text="Yellow",
                   bg="yellow",
                   pady=4,
                   padx=10,
                   font=("fixedsys",12),)
ColourLabel_yellow.place(x=160, y=80)

ColourLabel_blue=Label(root, text="Blue",
                   bg="#0e0eff",
                   pady=4,
                   padx=10,
                   font=("fixedsys",12),)
ColourLabel_blue.place(x=240, y=80)

#Primary Colours information 
Primary_colours_information=Label(root,text="Colours which cannot be made by mixing other colours together, instead they are used to create other colours.There are three primary colours: Red, Yellow, and Blue.", 
            font=("fixedsys",9),
            padx=20,
            pady=5, 
            bg="#fcf5c7", 
            wraplength=390,
            borderwidth=0,)
Primary_colours_information.place(x=0,y=105)


# Subheading for the information on secondary colours. 
Secondary_colours_subheading=Label(root,text="Secondary Colours", 
            font=("fixedsys",13,"underline"),
            padx=20,
            pady=10, 
            bg="#fcf5c7", 
            borderwidth=2,)
Secondary_colours_subheading.place(x=100, y=175)


#Creates the labels for the different secondary colours. 
ColourLabel_green=Label(root, text="Green", 
                  bg="green",
                  pady=4,
                  padx=10,
                  font=("fixedsys",12),)
ColourLabel_green.place(x=85,y=210)


ColourLabel_orange=Label(root, text="Orange",
                   bg="orange",
                   pady=4,
                   padx=10,
                   font=("fixedsys",12),)
ColourLabel_orange.place(x=160, y=210)

ColourLabel_purple=Label(root, text="Purple",
                   bg="purple",
                   pady=4,
                   padx=10,
                   font=("fixedsys",12),)
ColourLabel_purple.place(x=240, y=210)


#Creates label for information on Secondary Colours
Secondary_colours_information=Label(root,text="Colours created by mixing equal amounts of two primary colours. The secondary colours are orange, green and purple.", 
            font=("fixedsys",10),
            padx=20,
            pady=5, 
            bg="#fcf5c7", 
            wraplength=380,
            borderwidth=0,)
Secondary_colours_information.place(x=0,y=235)

#Labels that display the colour combinations for secondary colours.
Colour_equation1=Label(root,text="Blue + Yellow = Green", 
            font=("fixedsys",10),
            padx=5,
            pady=5, 
            bg="#fcf5c7", 
            borderwidth=0,)
Colour_equation1.place(x=110,y=285)

Colour_equation2=Label(root,text="Red + Blue = Purple", 
            font=("fixedsys",10),
            padx=5,
            pady=5, 
            bg="#fcf5c7", 
            borderwidth=0,)
Colour_equation2.place(x=115,y=303)

Colour_equation3=Label(root,text="Red + Yellow = Orange", 
            font=("fixedsys",10),
            padx=5,
            pady=5, 
            bg="#fcf5c7", 
            borderwidth=0,)
Colour_equation3.place(x=110,y=321)

#Home button that goes back to the first page. 
Home_button=Button(root,text="HOME",
               font=("fixedsys",14),
               pady=8, 
               padx=25,
               bg="#adf7b6", 
               command=homepage) 
Home_button.place(x=15, y=345) 


#Button that goes to the quiz page. 
Quiz_button=Button(root,text="QUIZ",
               font=("fixedsys",14),
               pady=8, 
               padx=25,
               bg="#adf7b6", 
               command=Quiz) 
Quiz_button.place(x=280,y=345) 

root.mainloop()