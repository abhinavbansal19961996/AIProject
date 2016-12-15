import subprocess
import os

from tkinter import *
from tkinter import messagebox as tkMessageBox

def submit():
    region=variable.get()
    print(region)
    if region=="4":
        tkMessageBox.showinfo("Great","Correct Answer.....")
        
        mastervideo.destroy()
        exec(open("no8.py").read())
    else:
        tkMessageBox.showinfo("No problem","Try Again.....Look carefully")
        


global mastervideo,back_image,e1,variable
mastervideo= Tk()
mastervideo.resizable(width=False, height=False)
mastervideo.geometry('1370x745')

mastervideo.configure(background='red')
w1 = Label(mastervideo, text="Suppose you have 6 apple .... i take 2 apple \n from you  how many apples will you have?.. ",fg="black",bg='blue',font=("Comic Sans MS", 44))
w1.grid(row=1,column=0,sticky=W,padx=(70,45),pady=(10,10))




myImagess = PhotoImage(file='6applemod.gif')
w = Label(mastervideo, image=myImagess)
w.grid(row=0,column=0,padx=20)

selectedregion=StringVar()
selectedregion.set("D")
variable=selectedregion


radiodayscholar=Radiobutton(mastervideo,text="1 apple",variable=selectedregion,value="1")
radiodayscholar.grid(row=2,column=0,padx=(10,10))
radiohosteller=Radiobutton(mastervideo,text="2 apple",variable=selectedregion,value="2")
radiohosteller.grid(row=3,column=0,padx=(100,100))
radiohosteller=Radiobutton(mastervideo,text="3 apple",variable=selectedregion,value="3")
radiohosteller.grid(row=4,column=0,padx=(100,100))
radiohosteller=Radiobutton(mastervideo,text="4 apple",variable=selectedregion,value="4")
radiohosteller.grid(row=5,column=0,padx=(100,100))
radiohosteller=Radiobutton(mastervideo,text="5 apple",variable=selectedregion,value="5")
radiohosteller.grid(row=6,column=0,padx=(100,100))
radiohosteller=Radiobutton(mastervideo,text="6 apple",variable=selectedregion,value="6")
radiohosteller.grid(row=7,column=0,padx=(100,100))
radiohosteller=Radiobutton(mastervideo,text="7 apple",variable=selectedregion,value="7")
radiohosteller.grid(row=8,column=0,padx=(100,100))
radiohosteller=Radiobutton(mastervideo,text="8 apple",variable=selectedregion,value="8")
radiohosteller.grid(row=9,column=0,padx=(100,100))
radiohosteller=Radiobutton(mastervideo,text="9 apple",variable=selectedregion,value="9")
radiohosteller.grid(row=10,column=0,padx=(100,100))

submitbutton=Button(mastervideo,text="Submit data",command=submit)
submitbutton.grid(row=11,column=0)
mastervideo.mainloop();

