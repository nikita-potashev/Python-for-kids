from tkinter import *
import random


def getRandomDistr():
    return random.normalvariate(1, 2)

def genRandomArray(n):
    y=[]
    temp=[]
    summ=0
    for i in range(0,n):
        random=round(getRandomDistr(),2)
        temp.append(random)

    for j in range(len(temp)):
        summ+=temp[j]

    for k in range(len(temp)):
        y.append(round(temp[k] * (summ**-1 ),2) )

    return y

def outArray(value):
    output.delete("0.0","end")
    output.insert("0.0",value) 

def calc():
        a_val = int(a.get())
        outArray(genRandomArray(a_val))
   

root = Tk()
root.title("Array generator")
root.minsize(325,230)
root.resizable(width=False, height=False)


frame = Frame(root)
frame.grid()

a = Entry(frame, width=5)
a.grid(row=1,column=1,padx=(10,0))
a_lab = Label(frame, text="Enter n").grid(row=1,column=2)


but = Button(frame, text="Generate", command=calc).grid(row=1, column=7, padx=(10,0))

output = Text(frame, font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)

root.mainloop()