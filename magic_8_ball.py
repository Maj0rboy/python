from tkinter import *
import random
root = Tk()
root.title("MAGIC 8 BALL")
root.geometry("400x400")

mylabel1 = Label(root,text="YOUR QUESTION")
mylabel1.place(x=30,y=50)

question = StringVar()
result = StringVar()

responses = ["yes","no","negative","yes","yes","negative","yes","yes","no","negative","yes","no","yes","negative","no","yes","no","yes","yes","negative",]

mylabel2 = Entry(root,textvariable=question, width=30)
mylabel2.place(x=150,y=50)

mylabel3 = Entry(root,textvariable=result, width=30)
mylabel3.place(x=150,y=150)

# functions
def RESULT():
    choosen = random.choice(responses)
    result.set(choosen)

    
def exit():
    root.destroy()

def reset():
    question.set("")
    result.set("")
    
btn_result = Button(root,text="RESULT",width=5,relief="solid",command=RESULT)
btn_result.place(x=30,y=150)

btn_reset = Button(root,text="RESET",width=5,relief="solid",command=reset)
btn_reset.place(x=150,y=250)

btn_exit = Button(root,text="EXIT",width=5,relief="solid",command=exit)
btn_exit.place(x=250,y=250)
root.mainloop()