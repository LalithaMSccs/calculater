from tkinter import Tk,Entry,Button,StringVar,ttk
from PIL import Image


###Create a class for calculator
class calculator:
    def __init__(self,master):
        master.title("CALCULATOR")
        master.geometry('358x420+0+0')
        master.config(bg="gray")
        master.resizable(False,False)
        
        self.equation=StringVar()
        self.entry_value=''
        ##Value entrying felid
        Entry(width=17,bg="black",fg='white',font=('arial bold',28),textvariable=self.equation).place(x=0,y=0)
        #### Buttons
       
        Button(width=24,height=4,text='C',relief='flat',bg='blue',fg='white',command=self.clear).place(x=0,y=50)
        Button(width=11,height=4,text='%',relief='flat',bg='black',fg='white',command=lambda:self.show('%')).place(x=180,y=50)
        Button(width=11,height=4,text='1',relief='flat',bg='black',fg='white',command=lambda:self.show(1)).place(x=0,y=125)
        Button(width=11,height=4,text='2',relief='flat',bg='black',fg='white',command=lambda:self.show(2)).place(x=90,y=125)
        Button(width=11,height=4,text='3',relief='flat',bg='black',fg='white',command=lambda:self.show(3)).place(x=180,y=125)
        Button(width=11,height=4,text='4',relief='flat',bg='black',fg='white',command=lambda:self.show(4)).place(x=0,y=200)
        Button(width=11,height=4,text='5',relief='flat',bg='black',fg='white',command=lambda:self.show(5)).place(x=90,y=200)
        Button(width=11,height=4,text='6',relief='flat',bg='black',fg='white',command=lambda:self.show(6)).place(x=180,y=200)
        Button(width=11,height=4,text='7',relief='flat',bg='black',fg='white',command=lambda:self.show(7)).place(x=0,y=275)
        Button(width=11,height=4,text='8',relief='flat',bg='black',fg='white',command=lambda:self.show(8)).place(x=180,y=275)
        Button(width=11,height=4,text='9',relief='flat',bg='black',fg='white',command=lambda:self.show(9)).place(x=90,y=275)
        Button(width=11,height=4,text='0',relief='flat',bg='black',fg='white',command=lambda:self.show(0)).place(x=90,y=350)
        Button(width=11,height=4,text='00',relief='flat',bg='black',fg='white',command=lambda:self.show('00')).place(x=0,y=350)
        Button(width=11,height=4,text='.',relief='flat',bg='black',fg='white',command=lambda:self.show('.')).place(x=180,y=350)
        Button(width=11,height=4,text='+',relief='flat',bg='black',fg='white',command=lambda:self.show('+')).place(x=270,y=275)
        Button(width=11,height=4,text='-',relief='flat',bg='black',fg='white',command=lambda:self.show('-')).place(x=270,y=200)
        Button(width=11,height=4,text='/',relief='flat',bg='black',fg='white',command=lambda:self.show('/')).place(x=270,y=50)
        Button(width=11,height=4,text='x',relief='flat',bg='black',fg='white',command=lambda:self.show('*')).place(x=270,y=125)
        Button(width=11,height=4,text='=',relief='flat',bg='black',fg='white',command=self.solve).place(x=270,y=350)
        
        
     ## to show the value   
    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)
    ##to clear the Entry place   
    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)
      ##to solve the equation  
    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)
        
    







## root and class,icon
root=Tk()
root.iconbitmap("C:\\Users\\lap\\Documents\\my use\\my project\\img\\Calculator_30001.ico")
Calculator=calculator(root)
root.mainloop()
