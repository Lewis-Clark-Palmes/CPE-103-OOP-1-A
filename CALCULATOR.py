from tkinter import*

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number')
        self.lbl1.place(x=100, y=50)
        self.t1 = Entry()
        self.t1.place(x=200, y=50)

        self.lbl2=Label(win, text='Second number')
        self.lbl2.place(x=100, y=100)
        self.t2 = Entry()
        self.t2.place(x=200, y=100)

        self.lbl3=Label(win, text='Result')
        self.lbl3.place(x=100, y=150)
        self.t3 = Entry()
        self.t3.place(x=200, y=150)

        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.btn3 = Button(win, text='Multiply')
        self.btn4 = Button(win, text='Divide')
        self.btn5 = Button(win, text='Clear')
        self.b1 = Button(win, text='Add',fg="green", command=self.add)
        self.b2 = Button(win, text='Subtract',fg="red",command=self.sub)
        self.b3 = Button(win, text='Multiply', fg="dark orange",command=self.mult)
        self.b4 = Button(win, text='Divide', fg="purple",command=self.div)
        self.b5 = Button(win, text='Clear', fg="grey",command=self.clr)
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=50, y=200)
        self.b2.place(x=100, y=200)
        self.b3.place(x=170, y=200)
        self.b4.place(x=240, y=200)
        self.b5.place(x=150, y=250)
    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def mult(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def div(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 / num2
        self.t3.insert(END, str(result))

    def clr(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')


window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()
