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
        
    masterkatt.destroy()
    exec(open("result.py").read())

def false():
    tkMessageBox.showinfo("ohooo!!","Wrong Answer!!!")
        
    masterkatt.destroy()
    exec(open("result.py").read())
    
global masterkatt,back_image,e1,variable,photo1,photo2

masterkatt= Tk()
masterkatt.resizable(width=False, height=False)
masterkatt.geometry('1370x745')

masterkatt.configure(background='red')

w1 = Label(masterkatt, text="Q10. is 0 equal to ZERO?",fg="black",bg='yellow',font=("Comic Sans MS", 44))
w1.grid(row=0,column=0,sticky=W,padx=(70,45),pady=(10,100),columnspan=2,)
photo1=PhotoImage(file="true.gif")
photo2=PhotoImage(file="false.gif")

submitbutton=Button(masterkatt,image=photo1,command=true)
submitbutton.grid(row=1,column=0,sticky=W,padx=(60,30))



submitbutton1=Button(masterkatt,image=photo2,command=false)
submitbutton1.grid(row=1,column=1,sticky=W,padx=(250,30))
