from tkinter import *
import datetime

def out(value):
    output.delete("0.0","end")
    output.insert("0.0",str(value)) 



def calc():
	Sunday = datetime.date(2018,3, 4).weekday()
	Monday = datetime.date(2018,3, 5).weekday()  #year, month, day
	Tuesday = datetime.date(2018,3, 6).weekday()
	out(Sunday==1 and Monday==2 and Tuesday==3)
	


	
	

root = Tk()
root.title("Worst task")
root.minsize(325,230)
root.resizable(width=False, height=False)


frame = Frame(root)
frame.grid()


a_lab = Label(frame, text="vbSunday==1").grid(row=1,column=2)


b_lab = Label(frame, text="vbMonday==2").grid(row=1,column=4)

c_lab = Label(frame, text="vbTuesday==3").grid(row=1,column=6)



but = Button(frame, text="Calculate", command=calc).grid(row=1, column=7, padx=(10,0))

output = Text(frame, font="Arial 12", width=35, height=10)
output.grid(row=3, columnspan=8)


root.mainloop()