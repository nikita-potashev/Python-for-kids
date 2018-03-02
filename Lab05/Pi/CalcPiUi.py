import time
from tkinter import *


def calcPi(n):
  return ( (4*n*n) / ( (2*n-1) * (2*n+1) ) )



def out(value):
    output.delete("0.0","end")
    output.insert("0.0",value) 

def outTime(value):
    outt.delete("0.0","end")
    outt.insert("0.0",value) 

def calc():
	a_val = float(a.get())
	start_time = time.time() #start 
	n=1
	pi1=1
	pi2=1
	pi=1
	while True:
	  pi1=calcPi(n)
	  pi2=calcPi(n+1)
	  pi*=calcPi(n)
	  n+=1
	  if (abs(pi2-pi1)<=a_val):
	    break
	out(pi*2)
	outTime("%s :Worked time" % (time.time() - start_time))


root = Tk()
root.title("Bad pi calculator")
root.minsize(325,230)
root.resizable(width=False, height=False)


frame = Frame(root)
frame.grid()

a = Entry(frame, width=10)
a.grid(row=1,column=1,padx=(10,0))
a_lab = Label(frame, text="Enter epsilon").grid(row=1,column=2)


but = Button(frame, text="Start", command=calc).grid(row=1, column=7, padx=(10,0))

output = Text(frame, font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)
outt = Text(frame, font="Arial 12", width=35, height=10)
outt.grid(row=3, columnspan=8)
root.mainloop()