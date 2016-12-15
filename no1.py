from tkinter import *
from tkinter import messagebox as tkMessageBox
import sqlite3,os,subprocess
def close_window():
    a1=e1.get()
    
    convar = sqlite3.connect('storename.db')
    query="DELETE FROM name"
    
    convar.execute(query)
   
    convar.commit()
    


    
    querya='''INSERT INTO name (kid_name) VALUES('%s');'''%(a1)
    convar.execute(querya)
    convar.commit()
    convar.close()

    tkMessageBox.showinfo("Welcome!!!!","Let us learn "+a1+" ok?")
   
    masters.destroy()
    exec(open("Choose.py").read())

global masters,back_image,e1
masters= Tk()
masters.resizable(width=False, height=False)
masters.geometry('1370x745')

masters.configure(background='red')
w1 = Label(masters, text="WHAT IS YOUR NAME,KID? ",fg="black",bg='blue',font=("Comic Sans MS", 44))
w1.grid(row=0,column=0,sticky=W,padx=(70,45),pady=(50,50))


e1 = Entry(masters,font=("Comic Sans MS", 44))
e1.grid(row=1, column=0,padx=(50,45),pady=(50,50))


submitbutton=Button(masters,text="Submit",command=close_window,fg="white",bg="blue",font=("Helvetica", 44))
submitbutton.grid(row=2,column=0,columnspan=2,padx=(70,45),sticky=W)


masters.mainloop()
