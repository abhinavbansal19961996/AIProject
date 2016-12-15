import subprocess
import os

from tkinter import *
from tkinter import messagebox as tkMessageBox

def true_window():
    p=subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe" , "file:///C:/Users/abhinave/Desktop/AI PROJECT/videoa.mp4",'--play-and-exit'])



def false_window():
    tkMessageBox.showinfo("No problem","Let us solve some problems")
    
    masterboy.destroy()
    exec(open("no7.py").read())

global masterboy,back_image,e1
masterboy= Tk()
masterboy.resizable(width=False, height=False)
masterboy.geometry('1370x745')

masterboy.configure(background='red')
w1 = Label(masterboy, text="Watch video again?",fg="black",bg='blue',font=("Comic Sans MS", 44))
w1.grid(row=0,column=0,sticky=W,padx=(70,45),pady=(50,50))


submitbutton=Button(masterboy,text="YES",command=true_window,fg="white",bg="blue",font=("Helvetica", 44))
submitbutton.grid(row=1,column=0,columnspan=2,padx=(70,45),sticky=W)




submitbutton=Button(masterboy,text="NO",command=false_window,fg="white",bg="blue",font=("Helvetica", 44))
submitbutton.grid(row=1,column=0,columnspan=2,padx=(380,45),sticky=W)
masterboy.mainloop()
