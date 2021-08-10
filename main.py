import rstools
from tkinter import *
from functools import partial
class mainWindow:

    def __init__(self,master) -> None:
        self.master = master
        self.constraint = IntVar()
        self.constring = []
        Label(self.master , text="Revised Simplex Method", font=("Arial",25)).pack()
        Label(self.master,text="select number of constraint").pack()
        Scale(self.master,variable=self.constraint,from_=2,to=4,orient=HORIZONTAL).pack()
        Button(self.master,text="Submit",command=self.next).pack()
    
    def next(self):
        level1 = Toplevel()
        level1.geometry("400x300")
        a = self.constraint.get()
        yy1 = 5
        for i in range(a+1):
            if i==0:
                l1 = Label(level1,text="Z")
                l1.place(x=120,y=yy1)
            else:
                l2 = Label(level1,text="Constraint"+str(i))
                l2.place(x=70,y=yy1)
            yy1+=20
        
        yy = 5
        for i in range(a+1):
            va = StringVar()
            e = Entry(level1,textvariable=va)
            e.place(x=135,y=yy)
            self.constring.append(va)
            yy+=20
        finalanswer = partial(self.finalanswer,level1)
        Button(level1,text="calculate",command=finalanswer).place(x=225,y=20*(a+2))
        
        level1.mainloop()
    
    def finalanswer(self,level1):
        Decodedstring = []
        for i in self.constring:
            Decodedstring.append(i.get())
        a = len(Decodedstring)

        cj = rstools.optimizationFunction(Decodedstring[0])
        A = []
        b = []
        for i in range(1,a):
            A.append(rstools.constraintsFunction(Decodedstring[i])[:-1])
            b.append([rstools.constraintsFunction(Decodedstring[i])[-1]])

        cb = [[0]*(a-1)]
        cb = rstools.transpose(cb)
        B = rstools.B(a-1)

        print(A,B,b,cb,cj)
        fans = rstools.answer(A,B,b,cb,cj)
        
        fans0 = fans[0]
        fans1 = fans[1]
        yy = 150
        a = rstools.variables(Decodedstring[0])
        for i in range(len(fans0)):
            Label(level1,text=a[fans1[i]]+" ="+str(fans0[i][0])).place(x=200,y=yy)
            yy+=20

if __name__ == "__main__":
    app = Tk()
    app.title("Linear Programming Problem")
    app.geometry("500x400")
    win = mainWindow(app)

    app.mainloop()