from tkinter import *
from tkinter import messagebox   
  
top = Tk()  
  
top.geometry("200x100")  
  
def fun():  
    messagebox.showinfo("Hello", "Vermelho Button clicked")  
def fun1():  
    messagebox.showinfo("Hello", "Azul Button clicked") 
def fun2():  
    messagebox.showinfo("Hello", "Verde Button clicked") 
def fun3():  
    messagebox.showinfo("Hello", "Amarelo Button clicked")   
  
b1 = Button(top,text = "Vermelho",command = fun,activeforeground = "red",bg = "red",pady=10)  
  
b2 = Button(top, text = "Azul",command = fun1,activeforeground = "blue",bg = "blue",pady=10)  
  
b3 = Button(top, text = "Verde",command = fun2,activeforeground = "green",bg = "green",pady = 10)  
  
b4 = Button(top, text = "Amarelo",command = fun3,activeforeground = "yellow",bg = "yellow",pady = 10)  
  
b1.pack(side = LEFT)  
  
b2.pack(side = RIGHT)  
  
b3.pack(side = TOP)  
  
b4.pack(side = BOTTOM)  
  
top.mainloop()  