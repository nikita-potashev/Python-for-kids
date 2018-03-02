# import datetime
 

# aa = datetime.date(2010,1,1)
# bb = datetime.date(2010,10,30)
# cc = int(bb-aa)
# week = int(cc.days) #кол-во недель
# week=week//7
# fivedayweek=cc-week*5
# sixdayweek=cc-week*6

# print(week)
# print(fivedayweek)
# print(sixdayweek)

from tkinter import *
import datetime

def out(value):
    output.delete("0.0","end")
    output.insert("0.0",value) 



def calc():
	firstDate = datetime.date(int(y1.get()),int(d1.get()),int(m1.get()))
	secondDate = datetime.date(int(y2.get()),int(d2.get()),int(m2.get()))
	delta =secondDate-firstDate
	days=int(delta.days)
	weeks=days//7
	fivedw=days-weeks*5
	sixdw=days-weeks*6


	out("Days:%s \nWeeks:%s \nHolidays 5 day week:%s \nHolidays 6 day week:%s" % (days,weeks,fivedw,sixdw))
	

root = Tk()
root.title("Very bad holidays calculator")
root.minsize(325,230)
root.resizable(width=False, height=False)


frame = Frame(root)
frame.grid()

y1 = Entry(frame, width=6)
y1.grid(row=1,column=1,padx=(10,0))
a_lab = Label(frame, text="year").grid(row=1,column=2)


d1 = Entry(frame, width=6)
d1.grid(row=1,column=3,padx=(10,0))
b_lab = Label(frame, text="day").grid(row=1,column=4)

m1= Entry(frame, width=6)
m1.grid(row=1,column=5,padx=(10,0))
c_lab = Label(frame, text="month").grid(row=1,column=6)

y1.insert(0,2010)
d1.insert(0,1)
m1.insert(0,1)

y2 = Entry(frame, width=6)
y2.grid(row=2,column=1,padx=(10,0))
aa_lab = Label(frame, text="year").grid(row=2,column=2)


d2 = Entry(frame, width=6)
d2.grid(row=2,column=3,padx=(10,0))
bb_lab = Label(frame, text="day").grid(row=2,column=4)

m2= Entry(frame, width=6)
m2.grid(row=2,column=5,padx=(10,0))
cc_lab = Label(frame, text="month").grid(row=2,column=6)

y2.insert(0,2010)
d2.insert(0,10)
m2.insert(0,30)


but = Button(frame, text="Calculate", command=calc).grid(row=1, column=7, padx=(10,0))

output = Text(frame, font="Arial 12", width=35, height=10)
output.grid(row=3, columnspan=8)


root.mainloop()