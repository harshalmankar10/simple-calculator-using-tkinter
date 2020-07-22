from tkinter import *

def btnclik(n):
   
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(n))
def clear():
    e.delete(0,END)
  
def btnequ():
 
     global f_num
   
  
     s_num=int(e.get())
     e.delete(0,END)
   
     if(math=="add"):
      e.insert(0,f_num+s_num)
     if(math=="sub"):
      e.insert(0,f_num-s_num)
     if(math=="mul"):
      e.insert(0,f_num*s_num)
     if(math=="div"):
       try:
        e.insert(0,f_num/s_num)
       except:
        e.insert(0,"ERROR")
   
  
    


def add():
    
    global f_num
    f_num=int(e.get())
    global math
    math="add"
    e.delete(0,END)
    

def sub():
    global f_num
    f_num=int(e.get())
    global math
    math="sub"
    e.delete(0,END)
    
    
def mul():
    global f_num
    f_num=int(e.get())
    global math
    math="mul"
    e.delete(0,END)
    
    
def div():
    global f_num
    f_num=int(e.get())
    global math
    math="div"
    e.delete(0,END)
    
    

                    
    
    
root=Tk()

root.title("CALCULATOR")
root.geometry("400x350")
root.resizable(0,0)
fr=Frame(root,borderwidth=5,highlightbackground="dark blue", highlightcolor="dark blue", highlightthickness=10,bg="grey",relief=GROOVE)
fr.pack()
e=Entry(fr,width=35,borderwidth=0,bg="grey",fg="white",font=(40))
e.grid(rowspan=2,column=0,columnspan=4,padx=10,pady=10)
b1=Button(fr,text="1",padx=40,pady=20,command=lambda:btnclik(1),fg="black",borderwidth=5)
b2=Button(fr,text="2",padx=40,pady=20,command=lambda:btnclik(2),fg="black",borderwidth=5)
b3=Button(fr,text="3",padx=40,pady=20,command=lambda:btnclik(3),fg="black",borderwidth=5)
b4=Button(fr,text="4",padx=40,pady=20,command=lambda:btnclik(4),fg="black",borderwidth=5)
b5=Button(fr,text="5",padx=40,pady=20,command=lambda:btnclik(5),fg="black",borderwidth=5)
b6=Button(fr,text="6",padx=40,pady=20,command=lambda:btnclik(6),fg="black",borderwidth=5)
b7=Button(fr,text="7",padx=40,pady=20,command=lambda:btnclik(7),fg="black",borderwidth=5)
b8=Button(fr,text="8",padx=40,pady=20,command=lambda:btnclik(8),fg="black",borderwidth=5)
b9=Button(fr,text="9",padx=40,pady=20,command=lambda:btnclik(9),fg="black",borderwidth=5)
b0=Button(fr,text="0",padx=40,pady=20,command=lambda:btnclik(0),fg="black",borderwidth=5)
cl=Button(fr,text="CLEAR",padx=26,pady=20,command=clear,bg="white",fg="black",borderwidth=5)
equ=Button(fr,text="=",padx=40,pady=20,command=btnequ,bg="powder blue",fg="black",borderwidth=5)

a=Button(fr,text="+",padx=20,pady=20,command=add,bg="silver",borderwidth=5)
s=Button(fr,text="-",padx=20,pady=20,command=sub,bg="silver",borderwidth=5)
m=Button(fr,text="*",padx=20,pady=20,command=mul,bg="silver",borderwidth=5)
d=Button(fr,text="/",padx=20,pady=20,command=div,bg="silver",borderwidth=5)


b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)

b1.grid(row=4,column=0)
b2.grid(row=4,column=1)
b3.grid(row=4,column=2)

b0.grid(row=5,column=1)
cl.grid(row=5,column=0)
equ.grid(row=5,column=2)

a.grid(row=2,column=3)
s.grid(row=3,column=3)
m.grid(row=4,column=3)
d.grid(row=5,column=3)


root.mainloop()
