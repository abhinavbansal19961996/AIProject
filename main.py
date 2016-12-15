from tkinter import *;
from tkinter import messagebox as tkMessageBox
import sqlite3,os,subprocess
def truesss_window():
    p=subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe" , "file:///C:/Users/abhinave/Desktop/AI PROJECT/videoa.mp4",'--play-and-exit'])
    
    masterpo.destroy()
    exec(open("no6.py").read())

def truess_window():
    
    
    submitbuttons=Button(masterpo,text="WELL DONE!! Click last time to watch video",command=truesss_window,fg="white",bg="blue",font=("Helvetica", 44))
    submitbuttons.grid(row=1,column=0,columnspan=2,padx=(70,45),sticky=W)
def trues_window():
    
    
    submitbuttonss=Button(masterpo,text="CLICK AGAIN WITH BIG SMILE",command=truess_window,fg="white",bg="blue",font=("Helvetica", 44))
    submitbuttonss.grid(row=1,column=0,columnspan=2,padx=(70,45),sticky=W)

def true_window():
    
    
    submitbuttonsss=Button(masterpo,text="CLICK AGAIN",command=trues_window,fg="white",bg="blue",font=("Helvetica", 44))
    submitbuttonsss.grid(row=1,column=0,columnspan=2,padx=(70,45),sticky=W)
def newcase():
    master.destroy()
    exec(open("no1.py").read())
    
global master,back_image
master= Tk()
master.resizable(width=False, height=False)
master.geometry('1370x745')
back_image=PhotoImage(file="background.gif")
label=Label(master,image=back_image)
label.place(x=0, y=0, relwidth=1, relheight=1)

playButton = Button(master, text='CLICK ME',fg="white",bg="brown",font=("Comic Sans MS", 36),command=newcase)
playButton.grid(row=0,column=0,padx=(670, 100),pady=(0,10))


master.mainloop()
