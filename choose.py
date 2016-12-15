from tkinter import *
from tkinter import messagebox as tkMessageBox

import sqlite3,os,subprocess

def true_window():
    tkMessageBox.showinfo("Great!!","ok!!!Then answer these questions...")
    
    masteras.destroy()
    exec(open("no2.py").read())



def false_window():
    tkMessageBox.showinfo("No problem","Let us watch the counting video")
    
    masteras.destroy()
    exec(open("no4.py").read())


global masteras,back_image,e1
masteras= Tk()
masteras.resizable(width=False, height=False)
masteras.geometry('1370x745')

masteras.configure(background='red')
convar = sqlite3.connect('storename.db')
queryaa="SELECT kid_name FROM name ";
cursor=convar.execute(queryaa)
convar.commit()
for row in cursor:
    t=row[0];
    
convar.close()
w1 = Label(masteras, text=t+", Do you know Counting?",fg="black",bg='blue',font=("Comic Sans MS", 44))
w1.grid(row=0,column=0,sticky=W,padx=(70,45),pady=(50,50))


submitbutton=Button(masteras,text="YES",command=true_window,fg="white",bg="blue",font=("Helvetica", 44))
submitbutton.grid(row=1,column=0,columnspan=2,padx=(70,45),sticky=W)


submitbutton=Button(masteras,text="NO",command=false_window,fg="white",bg="blue",font=("Helvetica", 44))
submitbutton.grid(row=1,column=0,columnspan=2,padx=(380,45),sticky=W)
masteras.mainloop()
