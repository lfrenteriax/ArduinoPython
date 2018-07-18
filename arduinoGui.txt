from Tkinter import *
import ttk
import pyfirmata

master = Tk()




# don't forget to change the serial port to suit
board = pyfirmata.Arduino('com4')
 
# start an iterator thread so
# serial buffer doesn't overflow
iter8 = pyfirmata.util.Iterator(board)
iter8.start()
 
# set up pin D9 as Servo Output
pin9 = board.get_pin('d:9:s')
pin13 = board.get_pin('d:13:o')



def led(tog=[0]):
	print 'LED'
	tog[0] = not tog[0]
	if tog[0]:
		led_btn.config(text='On')
		pin13.write(0)
	else:
		led_btn.config(text='Off')
		pin13.write(1)
  
var= StringVar()  
def read():
	print str(board.digital[int(combo2.get())].read())
	var.set( str(board.digital[int(combo2.get())].read()))
	print 'read '+ str(combo2.get())
   

def write():
   board.digital[int(combo.get())].write(int(combo1.get()))
   #board.digital[12].write(1)
   print 'write '+ str(combo.get())+' value '+ str(combo1.get())
def move_servo(a):
	print(a)
	pin9.write(a)

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
E1 = Entry(master,text=var, state="readonly",width=myWidth2)
E1.grid(row=1,column=5)

led_btn.grid(row=2, column=1)

scale = Scale(master,
    command = move_servo,
    to = 200,
    orient = HORIZONTAL,
    length = 100,)
scale.grid(row=3,column=1)
master.mainloop()
