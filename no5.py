from tkinter import *
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


        



global masterpo,back_image,e1
masterpo= Tk()
masterpo.resizable(width=False, height=False)
masterpo.geometry('1370x745')

masterpo.configure(background='red')
convar = sqlite3.connect('storename.db')
queryaa="SELECT kid_name FROM name ";
cursor=convar.execute(queryaa)
convar.commit()
for row in cursor:
    t=row[0];
    
convar.close()
w1 = Label(masterpo, text=t+", You have completed counting \n course successfully... Let us learn \n subtraction",fg="black",bg='blue',font=("Comic Sans MS", 44))
w1.grid(row=0,column=0,sticky=W,padx=(70,45),pady=(50,50))

submitbutton=Button(masterpo,text="CLICK",command=true_window,fg="white",bg="blue",font=("Helvetica", 44))
submitbutton.grid(row=1,column=0,columnspan=2,padx=(70,45),sticky=W)
masterpo.mainloop()

