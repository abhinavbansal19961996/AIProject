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

def truel_window():
    convar = sqlite3.connect('storename.db')
    queryaa="SELECT kid_name FROM name ";
    cursor=convar.execute(queryaa)
    convar.commit()
    for row in cursor:
        t=row[0];
    
    convar.close()

    tkMessageBox.showinfo("Congrats!!","Well done "+t+" !! you are just superb in counting.....")
    
    masterke.destroy()
    exec(open("no5.py").read())



def false_window():
   convar = sqlite3.connect('storename.db')
   queryaa="SELECT kid_name FROM name ";
   cursor=convar.execute(queryaa)
   convar.commit()
   for row in cursor:
       t=row[0];
   convar.close()
   tkMessageBox.showinfo("Ohoooo!!!","Answer again "+t+" Son...Count properly!!!")
    
   masterke.destroy()
   exec(open("no2.py").read())

global masterke,back_image,e1
masterke= Tk()
masterke.resizable(width=False, height=False)
masterke.geometry('1370x745')

masterke.configure(background='red')

myImagess = PhotoImage(file='4apple.gif')
w = Label(masterke, image=myImagess)
w.grid(row=0,column=0,padx=20)

w1 = Label(masterke, text="Count the number of \n apples.Are there 4 apples??  ",fg="black",bg='blue',font=("Comic Sans MS", 44))
w1.grid(row=0,column=1,sticky=W,padx=(70,45),pady=(50,50))



submitbutton=Button(masterke,text="TRUE",command=truel_window,fg="white",bg="blue",font=("Helvetica", 44))
submitbutton.grid(row=1,column=1,columnspan=2,padx=(70,45),sticky=W)


submitbutton=Button(masterke,text="FALSE",command=false_window,fg="white",bg="blue",font=("Helvetica", 44))
submitbutton.grid(row=1,column=1,columnspan=2,padx=(380,45),sticky=W)

masterke.mainloop()
