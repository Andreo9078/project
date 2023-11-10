from tkinter import ttk
from tkinter import *
from typing import Any
from triangle import EquilateralTriangle
import re
import tkinter.messagebox




def calc(event):
    trinagle = EquilateralTriangle()
    if side.get():
        trinagle.side = float(side.get())
    if enterS.get():
        trinagle.area = float(enterS.get())
    if enterR.get():
        trinagle.r_circumscribed_circle = float(enterR.get())
    if enterRIn.get():
        trinagle.r_inscribed_circle = float(enterRIn.get())
    side.insert(0, float(trinagle.side))
    enterS.insert(0, float(trinagle.area))
    enterR.insert(0, float(trinagle.r_circumscribed_circle))
    enterRIn.insert(0, float(trinagle.r_inscribed_circle))

window = Tk()
window.title("Параметры треугольника")
window.geometry('400x250')
#window.columnconfigure(index=0,weight=1)

def is_validate(val):
    err = "error is valid"
    try:
        for i in val:
            if str(type(i)) != "<class 'int'>":
                raise err
    except ValueError:
        tkinter.messagebox.showinfo("Err")


checkerr = (window.register(is_validate),"%P")
errmsg = StringVar()

lbl = Label(window,textvariable=errmsg,text="Введите сторону треугольника: ")
lbl.grid(column=0, row=0, sticky="w")
    
side = Entry(window, width=10,validate="key",validatecommand=is_validate)
side.grid(column=1, row=0, sticky="w")

lbl2 = Label(window, textvariable=errmsg ,text="Введите радиус описанной окружности: ")
lbl2.grid(column=0, row=1, sticky="w")

enterR = Entry(window,width=10,validate="key",validatecommand=is_validate)
enterR.grid(column=1, row=1, sticky="w")

lbl3 =  Label(window, textvariable=errmsg ,text="Введите радиус вписанной окружности: ")
lbl3.grid(column=0, row=2, sticky="w")

enterRIn = Entry(window, width=10,validate="key",validatecommand=is_validate)
enterRIn.grid(column=1, row=2, sticky='w')

lbl4 = Label(window, textvariable=errmsg ,text="Введите значение площади: ")
lbl4.grid(column=0, row=3, sticky='w')

enterS = Entry(window,width=10,validate="key",validatecommand=is_validate)
enterS.grid(column=1,row=3,sticky='w')

testbutton = Button(window,text="Рассчитать")
testbutton.grid(column=2,row=6,sticky='w',padx=5,pady=100)
testbutton.bind("<Button-1>",calc)

window.mainloop()
