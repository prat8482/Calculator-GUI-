from tkinter import *

root=Tk()

entry=Entry(root, borderwidth=5, width=35, fg='blue')
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    var=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(var)+str(number))

def button_clear():
    entry.delete(0,END)

def button_add():
    first_num=entry.get()
    global f_num
    global math
    math='addition'
    f_num=float(first_num)
    entry.delete(0, END)

def button_equal():
    second_num=entry.get()
    entry.delete(0, END)
    if math=='addition':
        entry.insert(0, f_num + float(second_num))
    if math=='multiplication':
        entry.insert(0, f_num * float(second_num))
    if math=='subtraction':
        entry.insert(0, f_num - float(second_num))
    if math=='division':
        entry.insert(0, f_num / float(second_num))
    if math=='power':
        entry.insert(0, f_num**float(second_num))

def button_multiply():
    first_num=entry.get()
    global f_num
    global math
    math='multiplication'
    f_num=float(first_num)
    entry.delete(0, END)
    
def button_subtract():
    first_num=entry.get()
    global f_num
    global math
    math='subtraction'
    f_num=float(first_num)
    entry.delete(0, END)

def button_divide():
    first_num=entry.get()
    global f_num
    global math
    math='division'
    f_num=float(first_num)
    entry.delete(0, END)
    
def button_pow():
    first_num=entry.get()
    global f_num
    global math
    math='power'
    f_num=float(first_num)
    entry.delete(0, END)

button_1=Button(root, text='1', padx=41.5, pady=20,bg='#fab789', command=lambda:button_click(1))
button_2=Button(root, text='2', padx=41.5, pady=20,bg='#f99550', command=lambda:button_click(2))
button_3=Button(root, text='3', padx=41.5, pady=20,bg='#fb6803', command=lambda:button_click(3))
button_4=Button(root, text='4', padx=41.5, pady=20,bg='#f8fb96', command=lambda:button_click(4))
button_5=Button(root, text='5', padx=41.5, pady=20,bg='#f6fb4d', command=lambda:button_click(5))
button_6=Button(root, text='6', padx=41.5, pady=20,bg='#e1e705', command=lambda:button_click(6))
button_7=Button(root, text='7', padx=41.5, pady=20,bg='#a8fa6f', command=lambda:button_click(7))
button_8=Button(root, text='8', padx=41.5, pady=20,bg='#7ff62b', command=lambda:button_click(8))
button_9=Button(root, text='9', padx=41.5, pady=20,bg='#55c308', command=lambda:button_click(9))
button_0=Button(root, text='0', padx=41.5, pady=20,bg='#f7525e', command=lambda:button_click(0))
button_pt=Button(root, text='.', padx=43, pady=20,bg='#85c4ee', command=lambda:button_click('.'))
button_addit=Button(root, text='+', padx=40, pady=20,bg='#e18df9', command=button_add)
button_equal=Button(root, text='=', padx=41, pady=20,bg='#fb3846', command=button_equal)
button_pow=Button(root, text='^n', padx=37, pady=20,bg='#087ecd', command=button_pow)
button_clear=Button(root, text='Clear', padx=31, pady=20,bg='#f18991', command=button_clear)
button_multiply=Button(root, text='x', padx=43, pady=20,bg='#a408c4', command=button_multiply)
button_subtract=Button(root, text='-', padx=41.5, pady=20,bg='#de48fb', command=button_subtract)
button_divide=Button(root, text='÷', padx=42,bg='#0230c4', pady=20, command=button_divide)

button_addit.grid(row=1, column=0)
button_subtract.grid(row=1, column=1)
button_multiply.grid(row=1, column=2)
button_divide.grid(row=2, column=2)
button_pow.grid(row=2, column=1)
button_pt.grid(row=2,column=0)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_clear.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_equal.grid(row=6, column=2)

root.mainloop()
