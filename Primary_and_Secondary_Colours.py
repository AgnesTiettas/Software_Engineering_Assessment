from tkinter import * 
root=Tk() 
root.title("Simple Colour Wheel")
root.geometry("400x400")

Label1=Label(root,text="Primary and Secondary Colours", 
             font=("Arial",20),
             bg="lightgrey", 
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
             pady=40,
             relief="raised",
             borderwidth=0,) #Creating a label widget 
Label2.pack()


Label3=Label(root,text="Click to begin", 
             font=("Arial",10), 
             fg="black",
             padx=20,
             pady=30,
             relief="raised",
             borderwidth=0,) #Creating a label widget 
Label3.pack()





root.mainloop()
