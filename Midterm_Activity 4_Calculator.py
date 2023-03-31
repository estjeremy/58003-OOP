from tkinter import *
class MyWindow:
    def __init__(self,win,):



        self.lbl1 = Label(win,text="1st No.")
        self.lbl1.place(x=100,y=50)
        self.lbl2 = Label(win, text= "2nd No.")

        self.lbl2.place(x=100,y=100)
        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=100,y=150)

        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=200,y=50)

        self.txt2 = Entry(win,bd=1)
        self.txt2.place(x=200,y=100)

        self.txt3 = Entry(win,bd=3)
        self.txt3.place(x=200,y=150)

        self.btnadd = Button(win,text="Addition", command=self.add,  fg = "white", bg = "Black")
        self.btnadd.place(x=100,y=190)

        self.btnsub = Button(win,text="Subtraction", fg = "white", bg = "Black")
        self.btnsub.place(x=150,y=250)
        self.btnsub.bind('<Button-1>', self.sub)

        self.btnmul = Button(win,text="Multiplication", fg = "white", bg = "Black")
        self.btnmul.place(x=199,y=190)
        self.btnmul.bind('<Button-1>', self.mul)

        self.btndiv = Button(win,text="Division", fg = "white", bg = "Black")
        self.btndiv.place(x=280,y=250)
        self.btndiv.bind('<Button-1>', self.div)

        self.btnclear = Button(win,text="Clear", command=self.clear , fg = "white", bg = "Black")
        self.btnclear.place(x=400,y=100)

#add event-handling /bind () method

    def add(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END,str(result))   

    def sub(self,sub):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1-num2
        self.txt3.insert(END, str(result))


    def mul(self,mul):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1*num2
        self.txt3.insert(END, str(result))

    def div(self,div):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1/num2
        self.txt3.insert(END, str(result))

    def clear(self):
        self.txt1.delete(0,'end')
        self.txt2.delete(0,'end')
        self.txt3.delete(0,'end')


window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Calculator")
window.mainloop()