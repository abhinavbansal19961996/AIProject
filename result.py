import subprocess
import os,sqlite3

from tkinter import *
from tkinter import messagebox as tkMessageBox


def true_window():
    p=subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe" , "file:///C:/Users/abhinave/Desktop/AI PROJECT/numbers.mp4",'--play-and-exit'])

def trues_window():
    p=subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe" , "file:///C:/Users/abhinave/Desktop/AI PROJECT/videoa.mp4",'--play-and-exit'])
def tru_window():
    rootd.destroy()
def retake():
    rootd.destroy()
    exec(open("no9.py").read())
        
    
global rootd,back_image,e1,variable,photo1,photo2

rootd= Tk()
rootd.resizable(width=False, height=False)
rootd.geometry('1370x745')

rootd.configure(background='red')
convar = sqlite3.connect('quiz.db')
querys="SELECT count_true,sub_true FROM quizno ;"
cursor = convar.execute(querys)
convar.commit()
photo1=PhotoImage(file="true.gif")
photo2=PhotoImage(file="false.gif")

for row in cursor:
    a1=row[0];
    a2=row[1];

if a1<3 and a2<3:
    w1 = Label(rootd, text="Poor Performance. \n Watch counting and subtraction video agan.",fg="black",bg='yellow',font=("Comic Sans MS", 44))
    w1.grid(row=1,column=0,sticky=W,padx=(70,45),pady=(5,5),columnspan=2,)

    submitbutton=Button(rootd,text="PLAY SUBTRACTION VIDEO",command=trues_window,fg="white",bg="blue",font=("Helvetica", 34))
    submitbutton.grid(row=2,column=0,columnspan=2,padx=(0,0),sticky=W)
    submitbutton=Button(rootd,text="PLAY COUNTING VIDEO",command=true_window,fg="white",bg="blue",font=("Helvetica", 34))
    submitbutton.grid(row=2,column=1,columnspan=2,padx=(70,45),sticky=W)
    submitbutton=Button(rootd,text="Retake quiz",command=retake,fg="white",bg="blue",font=("Helvetica", 34))
    submitbutton.grid(row=3,column=0,columnspan=1,padx=(70,45),sticky=E,pady=(10,0))

if a1<3 and a2>=3:
    w1 = Label(rootd, text="Watch counting video again...",fg="black",bg='yellow',font=("Comic Sans MS", 44))
    w1.grid(row=1,column=0,sticky=W,padx=(70,45),pady=(10,100),columnspan=2,)
    
    submitbutton=Button(rootd,text="PLAY COUNTING VIDEO",command=true_window,fg="white",bg="blue",font=("Helvetica", 44))
    submitbutton.grid(row=2,column=0,columnspan=2,padx=(70,45),sticky=W)
    submitbutton=Button(rootd,text="Retake quiz",command=retake,fg="white",bg="blue",font=("Helvetica", 34))
    submitbutton.grid(row=3,column=0,columnspan=1,padx=(70,45),sticky=E,pady=(10,0))
if a1>=3 and a2<3:
    w1 = Label(rootd, text="Watch subtraction video again...",fg="black",bg='yellow',font=("Comic Sans MS", 44))
    w1.grid(row=1,column=0,sticky=W,padx=(70,45),pady=(10,100),columnspan=2,)
    submitbutton=Button(rootd,text="PLAY SUBTRACTION VIDEO",command=trues_window,fg="white",bg="blue",font=("Helvetica", 44))
    submitbutton.grid(row=2,column=0,columnspan=2,padx=(70,45),sticky=W)
    submitbutton=Button(rootd,text="Retake quiz",command=retake,fg="white",bg="blue",font=("Helvetica", 34))
    submitbutton.grid(row=3,column=0,columnspan=1,padx=(70,45),sticky=E,pady=(10,0))
if a1>=3 and a2>=3:
    w1 = Label(rootd, text="Good score!!",fg="black",bg='yellow',font=("Comic Sans MS", 44))
    w1.grid(row=1,column=0,sticky=W,padx=(70,45),pady=(10,100),columnspan=2,)
    submitbutton=Button(rootd,text="CLOSE",command=tru_window,fg="white",bg="blue",font=("Helvetica", 44))
    submitbutton.grid(row=2,column=0,columnspan=2,padx=(70,45),sticky=W,pady=(10,0))


        

convar.close()
w1 = Label(rootd, text="RESULT \n CORRECT COUNTING :"+str(a1)+"/5"+"\n CORRECT SUBRACTION :"+ str(a2)+"/5",fg="black",bg='yellow',font=("Comic Sans MS", 44))
w1.grid(row=0,column=0,sticky=W,padx=(70,45),pady=(10,10),columnspan=2,)
rootd.mainloop()
