from tkinter import *

def out(value):
    output.delete(1.0,END)
    output.insert("0.0",value) 



def convert():
	string= a.get("1.0","end")
	string1=string[0:10]
	string2=string[10:].replace("е","Е").replace("о","О")

	out(string1+string2)
	
	

root = Tk()
root.title("Very bad text converter")
root.minsize(400,230)
root.resizable(width=False, height=False)


frame = Frame(root)
frame.grid()

a_lab = Label(frame, text="Input text").grid(row=0,sticky = W)
a = Text(frame, font="Arial 12", width=40, height=5)
a.grid(row=2,sticky=W)
but = Button(frame, text="Convert", command=convert).grid(row=2,column=1)

b_lab = Label(frame, text="Output").grid(row=3,sticky = W)
output = Text(frame, font="Arial 12", width=40, height=10)
output.grid(row=4,sticky = W)




root.mainloop()