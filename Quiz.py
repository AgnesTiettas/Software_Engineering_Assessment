from tkinter import * 
from PIL import Image,ImageTk
root=Tk() 
root.title("Primary and Secondary Colours")
root.geometry("400x400") 
root.config(bg="#fcf5c7")
root.resizable(False,False) #Make sure that the page maintains its size at 400 by 400.

def homepage(): # Move back to the homepage. 
    root.destroy()
    import Primary_and_Secondary_Colours 


Question1=["Which one is the primary colour?","Which one is the secondary colour?","Red + Blue= __?", "Red+____=Orange?", "____+____=Green?"]
Options1= [['Yellow','Green','Orange','Purple','Yellow'],['Red','Yellow','Orange','Blue','Orange'], ['Orange','Purple','Blue','Red','Purple'], ['Yellow','Green','Blue','Orange','Yellow'],['Red, Yellow','Orange, Purple','Blue, Red','Yellow, Blue','Yellow, Blue']]


label1=Label(root, text=Question1[0], 
             font=("fixedsys",22), 
             wraplength=300,
             padx=10,
             pady=15, 
             bg="#fcf5c7")
label1.pack()

Var1=StringVar(root)
Var2=StringVar(root)
Var3=StringVar(root)
Var4=StringVar(root)


radio_btn1= Radiobutton(root,variable=Var1,
                        font=("fixedsys",18),
                        padx=10,
                        pady=10, 
                        bg="#fcf5c7",
                        wraplength=300,
                        command=lambda:Answer_Verification(radio_btn1))


radio_btn2= Radiobutton(root,variable=Var2,
                        font=("fixedsys",18), 
                        padx=15,
                        pady=5, 
                        bg="#fcf5c7",
                        wraplength=300,
                        command=lambda:Answer_Verification(radio_btn2))


radio_btn3= Radiobutton(root,
                        variable=Var3,
                        font=("fixedsys",18), 
                        padx=15,
                        pady=5, 
                        bg="#fcf5c7",
                        wraplength=300,
                        command=lambda:Answer_Verification(radio_btn3))

 
radio_btn4= Radiobutton(root,
                        variable=Var4,
                        font=("fixedsys",18),
                        padx=15,
                        pady=5, 
                        bg="#fcf5c7",
                        wraplength=300,
                        command=lambda:Answer_Verification(radio_btn4))



Next_btn=Button(root, 
                text="NEXT", 
                font=("fixedsys",22), 
                padx=10,
                pady=5, 
                bg="#adf7b6", 
                command=lambda:Next_question())

Next_btn.place(x=145, y=310)


radio_btn1.pack(anchor=W)
radio_btn2.pack(anchor=W)
radio_btn3.pack(anchor=W)
radio_btn4.pack(anchor=W) 

Question_number=0 
Correct=0 

def disable_buttons(state):
    radio_btn1['state']= state
    radio_btn2['state']= state 
    radio_btn3['state']= state 
    radio_btn4['state']= state

def Answer_Verification(radio):
    global Correct, Question_number

    if radio['text'] == Options1 [Question_number][4]:
        Correct+=1
    Question_number+=1
    disable_buttons('disable')

def Next_question():
    global Question_number,  Correct


    if Next_btn['text'] == 'Restart':
        Correct=0 
        Question_number=0  
        
    if Question_number==5:
        label1.destroy()
        radio_btn1.destroy()
        radio_btn2.destroy()
        radio_btn3.destroy()
        radio_btn4.destroy()

        label5= Label(root, 
                      text=str(Correct)+ "/" +str(len(Question1)), 
                      font=("fixedsys",68),
                      bg="#fcf5c7")
        label5.pack()
        l6=Button(root, 
                  text='HOME', 
                  font=("fixedsys",20), 
                  padx=15,
                  pady=10, 
                  bg="#adf7b6", 
                  command=homepage)
        l6.pack()
    else:
        label1['text']=Question1[Question_number]
        disable_buttons('normal')
        opts = Options1[Question_number]
        radio_btn1['text'] = opts[0]
        radio_btn2['text'] = opts[1]
        radio_btn3['text'] = opts[2]
        radio_btn4['text'] = opts[3]
        Var1.set(opts[0])
        Var2.set(opts[1])
        Var3.set(opts[2])
        Var4.set(opts[3])

        if Question_number == 4:
            Next_btn['text'] = 'SCORE' 

Next_question()


root.mainloop()

    
