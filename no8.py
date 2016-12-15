import subprocess
import os

from tkinter import *
from tkinter import messagebox as tkMessageBox


def submit():
    tkMessageBox.showinfo("Great","Let us begin.....")
        
    mastervideos.destroy()
    exec(open("no9.py").read())
global mastervideos,back_image,e1,variable
mastervideos= Tk()
mastervideos.resizable(width=False, height=False)
mastervideos.geometry('1370x745')

mastervideos.configure(background='red')
w1 = Label(mastervideos, text="Get ready for quiz \n Quiz will contain 10 questions. \n Let see what you have learnt?",fg="black",bg='blue',font=("Comic Sans MS", 44))
w1.grid(row=0,column=0,sticky=W,padx=(70,45),pady=(10,10))


submitbutton=Button(mastervideos,text="START QUIZ!!!!!",command=submit)
submitbutton.grid(row=11,column=0)
mastervideos.mainloop();
