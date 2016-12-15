import subprocess
import os,sqlite3

from tkinter import *
from tkinter import messagebox as tkMessageBox


def true():
    
    convar = sqlite3.connect('quiz.db')
    querys="SELECT count_true,sub_true FROM quizno ;"
    cursor = convar.execute(querys)
    convar.commit()
    for row in cursor:
        a1=row[0];
        a2=row[1];

    queryi="DELETE FROM quizno"
    cursor = convar.execute(queryi)
    convar.commit()
    
    a1=a1+1;
    query='''INSERT INTO quizno (count_true,sub_true) VALUES('%d','%d');'''%(a1,a2)
    convar.execute(query)
    convar.commit()
    convar.close()
    tkMessageBox.showinfo("Congrats","Correct Answer!!!")
        
    masterkatters.destroy()
    exec(open("no16.py").read())

def false():
    tkMessageBox.showinfo("ohooo!!","Wrong Answer!!!")
        
    masterkatters.destroy()
    exec(open("no16.py").read())
    
global masterkatters,back_image,e1,variable,photo1,photo2

masterkatters= Tk()
masterkatters.resizable(width=False, height=False)
masterkatters.geometry('1370x745')

masterkatters.configure(background='red')

w1 = Label(masterkatters, text="Q7. 9 (nine) comes after 8(eight).",fg="black",bg='yellow',font=("Comic Sans MS", 44))
w1.grid(row=0,column=0,sticky=W,padx=(70,45),pady=(10,100),columnspan=2,)
photo1=PhotoImage(file="true.gif")
photo2=PhotoImage(file="false.gif")

submitbutton=Button(masterkatters,image=photo1,command=true)
submitbutton.grid(row=1,column=0,sticky=W,padx=(60,30))



submitbutton1=Button(masterkatters,image=photo2,command=false)
submitbutton1.grid(row=1,column=1,sticky=W,padx=(250,30))
