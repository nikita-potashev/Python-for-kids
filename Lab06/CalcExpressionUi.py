from tkinter import *
import math

def out(value):
    output.delete("0.0","end")
    output.insert("0.0",value) 



def calc():
	a_val = float(a.get())
	b_val = float(b.get())
	c_val = float(c.get())
	temp1=(math.sin(a_val)**2 + math.cos(b_val)**2)/(a_val+b_val+c_val)
	temp2=math.sqrt(1-temp1)
	temp3=temp2/(a_val+b_val+c_val)**(2/3)
	out(temp3)
	

root = Tk()
root.title("Very bad Expression calculator")
root.minsize(325,230)
root.resizable(width=False, height=False)


frame = Frame(root)
frame.grid()

a = Entry(frame, width=6)
a.grid(row=1,column=1,padx=(10,0))
a_lab = Label(frame, text="a").grid(row=1,column=2)


b = Entry(frame, width=6)
b.grid(row=1,column=3,padx=(10,0))
b_lab = Label(frame, text="b").grid(row=1,column=4)

c= Entry(frame, width=6)
c.grid(row=1,column=5,padx=(10,0))
c_lab = Label(frame, text="c").grid(row=1,column=6)

a.insert(0,3.1416)
b.insert(0,1.5708)
c.insert(0,-1.884)


but = Button(frame, text="Calc", command=calc).grid(row=1, column=7, padx=(10,0))

output = Text(frame, font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)


root.mainloop()