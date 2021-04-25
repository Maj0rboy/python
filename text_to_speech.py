from tkinter import *
from gtts import gTTS 
from playsound import playsound

root = Tk()
root.title("convert text to speech")
root.config(bg="ghost white")
root.geometry("400x400")

mylabel1 = Label(root,text="TEXT TO SPEECH")
mylabel1.place(x=100,y=0)

mylabel2 = Label(root,text="Enter text")
mylabel2.place(x=30,y=50)

texttospeech = StringVar()
mylabel3 = Entry(root,textvariable=texttospeech,width="30",fg="blue")
mylabel3.place(x=30,y=100)

# functions
def play():
    message = texttospeech.get()
    speech = gTTS(text=message)
    speech.save("converted.mp3")
    playsound("converted.mp3")
def reset():
    texttospeech.set("")
def exit():
    root.destroy()
    
btn_play = Button(root,text="PLAY",width="5",relief="solid",command=play,font="Arial 15 bold")
btn_play.place(x=50,y=150)

btn_reset = Button(root,text="RESET",width="5",relief="solid",command=reset,font="Arial 15 bold")
btn_reset.place(x=250,y=150)

btn_exit = Button(root,text="EXIT",width="5",relief="solid",bg="orange",command=exit,font="Arial 15 bold")
btn_exit.place(x=150,y=150)
root.mainloop()