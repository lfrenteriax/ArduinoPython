from Tkinter import *
import ttk
master = Tk()


#boton led


def led():
   print 'LED'
   
def read():
   var.set(str(combo1.get()))
   print 'read '+ str(combo2.get())
   

def write():
   print 'write '+ str(combo.get())+' value '+ str(combo1.get())
def move_servo(a):
    print(a)

myWidth=10
myWidth2=5
myWidth3=3
Label(master, text="DIGITAL",width=myWidth,justify=LEFT).grid(row=0)
Label(master, text="DIGITAL",width=myWidth,justify=LEFT).grid(row=1)
Label(master, text="LED    ",width=myWidth,justify=LEFT).grid(row=2)
Label(master, text="SERVO    ",width=myWidth,justify=LEFT).grid(row=3)
led_btn = Button(master, text="off",width=myWidth, command=led)
dw_btn = Button(master, text="WRITE",width=myWidth, command=write)
dr_btn = Button(master, text="READ",width=myWidth, command=read)


dw_btn.grid(row=0, column=1)
Label(master, text="Pin",width=myWidth).grid(row=0,column=2)

values=range(2,13)
combo = ttk.Combobox(state="readonly",width=myWidth3)
combo.grid(row=0,column=3)
combo['values']=values
combo.current(0)
Label(master, text="Value",width=myWidth).grid(row=0,column=4)

values=[0,1]
combo1 = ttk.Combobox(state="readonly",width=myWidth3)
combo1.grid(row=0,column=5)
combo1['value']=values
combo1.current(0)

dr_btn.grid(row=1, column=1)
Label(master, text="Pin",width=myWidth).grid(row=1,column=2)
values=range(2,13)
combo2 = ttk.Combobox(state="readonly",width=myWidth3)
combo2.grid(row=1,column=3)
combo2['values']=values
combo2.current(0)
Label(master, text="Value",width=myWidth3).grid(row=1,column=4)
var= StringVar()
E1 = Entry(master,text=var,state="readonly",width=myWidth2)
E1.grid(row=1,column=5)

led_btn.grid(row=2, column=1)

scale = Scale(master,
    command = move_servo,
    to = 200,
    orient = HORIZONTAL,
    length = 100,)
scale.grid(row=3,column=1)
master.mainloop()
