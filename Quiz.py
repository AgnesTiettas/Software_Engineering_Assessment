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
             pady=20,
             wraplength=400,
             borderwidth=0,) #Creating a label widget 
Label1.pack()

Label2=Label(root,text="Which one is a primary colour?", 
             font=("fixedsys",16,),
             bg="#fcf5c7",
             fg="black",
             padx=35,
             pady=10,
             wraplength=400,
             borderwidth=0,) #Creating a label widget 
Label2.pack()

Options1= [
    ("Yellow","Correct, Good Job!"),
    ("Orange","Orange is incorrect, Good Try!"),
    ("Purple", "Purple is incorrect, Good Try!"),
    ("Green", "Green is incorrect, Good Try!"),
]

Question_1=StringVar()
Question_1.set("Yellow")


for text, mode in Options1:
    Radiobutton(root, 
                text=text, 
                variable=Question_1,
                value=mode,
                pady=8,
                padx=15,
                font=("fixedsys",15),
                bg="#fcf5c7",).pack(anchor=W)

def disableButtons(state):
    Check_button.config(state= DISABLED)

def clicked(value):
    if Question_1=="Yellow":
        Label3=Label(root, text=value)
        Label3.pack()
    else: 
        Label4=Label(root, text=value)
        Label4.pack()
    disableButtons("disable")

Check_button=Button(root, text="Check", 
                    font=("fixedsys",15,"bold"),
                    bg="#adf7b6",
                    command=lambda:clicked(Question_1.get()))
Check_button.pack()

    

Next_button=Button(root, text="NEXT", 
                    font=("fixedsys",15,"bold"),
                    bg="#adf7b6")
Next_button.pack()



root.mainloop()

