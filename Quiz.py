from tkinter import * #imports all symbols from tkinter module into the current namespace 
root=Tk() 
root.title("Primary and Secondary Colours")
root.geometry("410x410") 
root.config(bg="#fcf5c7")
root.resizable(False,False) #Make sure that the page maintains its size at 400 by 400.

def homepage(): # Move back to the homepage. 
    root.destroy()
    import Primary_and_Secondary_Colours 

#List that stores the questions to be displayed
Question1=["Which one is the primary colour?","Which one is the secondary colour?","Red + Blue= __?", "Red+____=Orange?", "____+____=Green?"]

#List that stores the options for each of the radiobuttons, with the last being the answer. 
Options1= [['Yellow','Green','Orange','Purple','Yellow'],['Red','Yellow','Orange','Blue','Orange'], ['Orange','Purple','Blue','Red','Purple'], ['Yellow','Green','Blue','Orange','Yellow'],['Red, Yellow','Orange, Purple','Blue, Red','Yellow, Blue','Yellow, Blue']]

#Creates and displays the label for the questions. 
Question=Label(root, text=Question1[0], 
             font=("fixedsys",22,"bold"), 
             wraplength=300,
             padx=10,
             pady=15, 
             bg="#fcf5c7")
Question.pack()

#Creates a instance of value holders for string variables.
Variable_1=StringVar(root)
Variable_2=StringVar(root)
Variable_3=StringVar(root)
Variable_4=StringVar(root)

#Radio buttons for the 4 options that the user can select.
radio_btn1= Radiobutton(root,variable=Variable_1,
                        font=("fixedsys",18),
                        padx=15,
                        pady=10, 
                        bg="#fcf5c7",
                        wraplength=300,
                        command=lambda:Answer_Verification(radio_btn1))


radio_btn2= Radiobutton(root,variable=Variable_2,
                        font=("fixedsys",18), 
                        padx=15,
                        pady=5, 
                        bg="#fcf5c7",
                        wraplength=300,
                        command=lambda:Answer_Verification(radio_btn2))


radio_btn3= Radiobutton(root,
                        variable=Variable_3,
                        font=("fixedsys",18), 
                        padx=15,
                        pady=5, 
                        bg="#fcf5c7",
                        wraplength=300,
                        command=lambda:Answer_Verification(radio_btn3))

 
radio_btn4= Radiobutton(root,
                        variable=Variable_4,
                        font=("fixedsys",18),
                        padx=15,
                        pady=5, 
                        bg="#fcf5c7",
                        wraplength=300,
                        command=lambda:Answer_Verification(radio_btn4))


#Creates and displays the next button which allows users to move to the next question. 
Next_btn=Button(root, 
                text="NEXT", 
                font=("fixedsys",22), 
                padx=10,
                pady=5, 
                bg="#adf7b6", 
                command=lambda:Next_question())

Next_btn.place(x=145, y=310)

#Displays all the radiobuttons on the screen and anchors it to the left. 
radio_btn1.pack(anchor=W)
radio_btn2.pack(anchor=W)
radio_btn3.pack(anchor=W)
radio_btn4.pack(anchor=W) 

#Sets the Question number and number of correct questions as 0. 
Question_number=0 
Correct=0 
Question_feedback=Label(text="",
                        bg="#fcf5c7",
                        font=("fixedsys",15,"italic"),
                        wraplength=200)
Question_feedback.place(x=200, y=190)



#Function that sets the state of the radiobuttons once the user has selected an option. 
def disable_buttons(state):
    radio_btn1['state']= state
    radio_btn2['state']= state 
    radio_btn3['state']= state 
    radio_btn4['state']= state
    
 


#Function for the verification of the answer selected by the user. 
def Answer_Verification(radio):
    global Correct, Question_number #Create a variable that is global (does not just apply to just the one function)
    
    if radio['text'] == Options1 [Question_number][4]: # IF statement for if the selected option is correct.
        Correct+=1 #Increases the value of the correct answers by 1 if the option selected is correct. 
        Question_feedback.config(text="Correct, Good Job!", fg="green")
    else:
        Question_feedback.config(text="Incorrect, Great Effort!", fg="red")
        

    Question_number+=1 #Increases the value of the Question number by 1 whether or not the the answer selected is correct. 
    disable_buttons('disable') # Disables the radiobuttons and calls upon the function. 
  
def Next_question(): # Function for moving to the next question. 
    global Question_number,  Correct #Create a variable that is global (does not just apply to just the one function)

    if Question_number==5: # IF statment for if the question number is equal to 5 (the last question). 

        Question.destroy() #Gets rid of the question on the page.
        radio_btn1.destroy() #Gets rid of the first radiobutton on the page. 
        radio_btn2.destroy() #Gets rid of the second radiobutton on the page. 
        radio_btn3.destroy() #Gets rid of the third radiobutton on the page. 
        radio_btn4.destroy() #Gets rid of the fourth radiobutton on the page.
        Next_btn.destroy() 
        Question_feedback.destroy()

        
        #Label that displays the score at the end of the quiz. 
        Final_Score= Label(root, 
                      text="Your Final Score is:"+ str(Correct)+ "/5", 
                      font=("fixedsys",38),
                      bg="#fcf5c7",
                      wraplength=380)
        Final_Score.place(x=40, y=80)

        #Button that 
        Home_Button=Button(root, 
                  text='HOME', 
                  font=("fixedsys",20), 
                  padx=15,
                  pady=10, 
                  bg="#adf7b6", 
                  command=homepage)
        Home_Button.place(x=20, y=300)

        Quit_Button=Button(root, 
                           text="EXIT",
                           font=("fixedsys",20),
                           padx=15,
                           pady=10, 
                           bg="#adf7b6", 
                           command=quit) 
        Quit_Button.place(x=262, y=300)
        

    else:
        Question['text']=Question1[Question_number]
        disable_buttons('normal') # Initialises state of next buttons

        #Shows each radiobutton option for the relavent question based on the
        Options= Options1[Question_number]
        radio_btn1['text'] = Options[0] 
        radio_btn2['text'] = Options[1]
        radio_btn3['text'] = Options[2]
        radio_btn4['text'] = Options[3]

        #Sets the default value 
        Variable_1.set(Options[0])
        Variable_2.set(Options[1])
        Variable_3.set(Options[2])
        Variable_4.set(Options[3])

        Question_feedback.config(text="")

        # Show score button once the question number reaches 4.
        if Question_number == 4:
            Next_btn['text'] = 'SCORE' # Changes the text NEXT to SCORE. 
            
#Calls upon the function Next_question
Next_question()


root.mainloop()

    
