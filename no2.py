from tkinter import *
from tkinter import messagebox as tkMessageBox
import sqlite3,os,subprocess
def true_window():
    tkMessageBox.showinfo("Congrats!!","Good!! you have nice counting skills.....")
    
    masterk.destroy()
    exec(open("no3.py").read())



def false_window():
    tkMessageBox.showinfo("Ohoooo!!!","Answer again Son...Count properly!!!")
    
    masterk.destroy()
    exec(open("no2.py").read())

global masterk,back_image,e1
masterk= Tk()
masterk.resizable(width=False, height=False)
masterk.geometry('1370x745')

masterk.configure(background='red')

myImagess = PhotoImage(file='6apple.gif')
w = Label(masterk, image=myImagess)
w.grid(row=0,column=0,padx=20)

convar = sqlite3.connect('storename.db')
queryaa="SELECT kid_name FROM name ";
cursor=convar.execute(queryaa)
convar.commit()
for row in cursor:
    t=row[0];
    
convar.close()



w1 = Label(masterk, text=t+", Count the number of \n apples.Are there 6 apples??  ",fg="black",bg='blue',font=("Comic Sans MS", 44))
w1.grid(row=0,column=1,sticky=W,padx=(70,45),pady=(50,50))



submitbutton=Button(masterk,text="TRUE",command=true_window,fg="white",bg="blue",font=("Helvetica", 44))
submitbutton.grid(row=1,column=1,columnspan=2,padx=(70,45),sticky=W)


submitbutton=Button(masterk,text="FALSE",command=false_window,fg="white",bg="blue",font=("Helvetica", 44))
submitbutton.grid(row=1,column=1,columnspan=2,padx=(380,45),sticky=W)

masterk.mainloop()
