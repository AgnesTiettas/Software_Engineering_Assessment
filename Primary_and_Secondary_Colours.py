from tkinter import * 
root=Tk() 
root.title("Simple Colour Wheel")
root.geometry("400x400") 
root.resizable(False,False) #Make sure that the page maintains its size at 400 by 400. 

Label1=Label(root,text="Primary and Secondary Colours", 
             font=("Arial",20),
             bg= "#d5bdaf", 
             fg="black",
             padx=20,
             pady=10,
             relief="raised",
             borderwidth=0,) #Creating a label widget 
Label1.pack() 

Label2=Label(root,text="Let's Learn about Primary and Secondary Colours!", 
             font=("Arial",12), 
             fg="black",
             padx=0,
             pady=60,
             relief="raised",
             borderwidth=0,) #Creating a label widget 
Label2.pack()

button1=Button(root,text="START",
               pady=20, 
               padx=80,)
button1.pack() 

Label3=Label(root,text="Click to begin", 
             font=("Arial",10), 
             fg="black",
             padx=20,
             pady=100,
             relief="raised",
             borderwidth=0,) #Creating a label widget 
Label3.pack() 










root.mainloop()
