from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Tic Tac Toe')

clicked=True
count=0

def disable_buttons():
    b_1.config(state=DISABLED)
    b_2.config(state=DISABLED)
    b_3.config(state=DISABLED)
    b_4.config(state=DISABLED)
    b_5.config(state=DISABLED)
    b_6.config(state=DISABLED)
    b_7.config(state=DISABLED)
    b_8.config(state=DISABLED)
    b_9.config(state=DISABLED)
    
def check():
    global winner
    winner =False
    if b_1['text'] =='X' and b_2['text'] == 'X' and b_3['text'] == 'X':
        b_1.config(bg='green')
        b_2.config(bg='green')
        b_3.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 1 is Victorious!')
        disable_buttons()
    elif b_4['text'] =='X' and b_5['text'] == 'X' and b_6['text'] == 'X':
        b_4.config(bg='green')
        b_5.config(bg='green')
        b_6.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 1 is Victorious!')
        disable_buttons()
    elif b_7['text'] =='X' and b_8['text'] == 'X' and b_9['text'] == 'X':
        b_7.config(bg='green')
        b_8.config(bg='green')
        b_9.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 1 is Victorious!')
        disable_buttons()
    elif b_1['text'] =='X' and b_4['text'] == 'X' and b_7['text'] == 'X':
        b_1.config(bg='green')
        b_4.config(bg='green')
        b_7.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 1 is Victorious!')
        disable_buttons()
    elif b_2['text'] =='X' and b_5['text'] == 'X' and b_8['text'] == 'X':
        b_2.config(bg='green')
        b_5.config(bg='green')
        b_8.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 1 is Victorious!')
        disable_buttons()
    elif b_3['text'] =='X' and b_6['text'] == 'X' and b_9['text'] == 'X':
        b_3.config(bg='green')
        b_6.config(bg='green')
        b_9.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 1 is Victorious!')
        disable_buttons()
    elif b_1['text'] =='X' and b_5['text'] == 'X' and b_9['text'] == 'X':
        b_1.config(bg='green')
        b_5.config(bg='green')
        b_9.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 1 is Victorious!')
        disable_buttons()
    elif b_3['text'] =='X' and b_5['text'] == 'X' and b_7['text'] == 'X':
        b_3.config(bg='green')
        b_5.config(bg='green')
        b_7.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 1 is Victorious!')
        disable_buttons()
    elif b_1['text'] =='O' and b_2['text'] == 'O' and b_3['text'] == 'O':
        b_1.config(bg='green')
        b_2.config(bg='green')
        b_3.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 2 is Victorious!')
        disable_buttons()
    elif b_4['text'] =='O' and b_5['text'] == 'O' and b_6['text'] == 'O':
        b_4.config(bg='green')
        b_5.config(bg='green')
        b_6.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 2 is Victorious!')
        disable_buttons()
    elif b_7['text'] =='O' and b_8['text'] == 'O' and b_9['text'] == 'O':
        b_7.config(bg='green')
        b_8.config(bg='green')
        b_9.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 2 is Victorious!')
        disable_buttons()
    elif b_1['text'] =='O' and b_4['text'] == 'O' and b_7['text'] == 'O':
        b_1.config(bg='green')
        b_4.config(bg='green')
        b_7.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 2 is Victorious!')
        disable_buttons()
    elif b_2['text'] =='O' and b_5['text'] == 'O' and b_8['text'] == 'O':
        b_2.config(bg='green')
        b_5.config(bg='green')
        b_8.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 2 is Victorious!')
        disable_buttons()
    elif b_3['text'] =='O' and b_6['text'] == 'O' and b_9['text'] == 'O':
        b_3.config(bg='green')
        b_6.config(bg='green')
        b_9.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 2 is Victorious!')
        disable_buttons()
    elif b_1['text'] =='O' and b_5['text'] == 'O' and b_9['text'] == 'O':
        b_1.config(bg='green')
        b_5.config(bg='green')
        b_9.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 2 is Victorious!')
        disable_buttons()
    elif b_3['text'] =='O' and b_5['text'] == 'O' and b_7['text'] == 'O':
        b_3.config(bg='green')
        b_5.config(bg='green')
        b_7.config(bg='green')
        winner =True
        messagebox.showinfo('Tic Tac Toe', 'Congratulations! Player 2 is Victorious!')
        disable_buttons()
    if count==9 and winner == False:
        messagebox.showinfo('Tic Tac Toe', "It's a Tie!")
        disable_buttons()
def but_click(b):
    global clicked, count
    if b['text'] == ' ' and clicked==True:
        b['text']='X'
        clicked=False
        count+=1
        check()
    elif b['text']==' ' and clicked==False:
        b['text']='O'
        clicked=True
        count+=1
        check()
    else:
        messagebox.showerror('Tic Tac Toe', "That's already been selected, please select another box")
    

def reset():
    global b_1,b_2,b_3,b_4,b_5,b_6,b_7,b_8,b_9
    global but_click, count
    clicked=True
    count=0
    
    b_1=Button(root, text= ' ', font=('Helvetica',20), height=3, width=6, bg='SystemButtonFace', command= lambda:but_click(b_1))
    b_2=Button(root, text= ' ', font=('Helvetica',20), height=3, width=6, bg='SystemButtonFace', command= lambda:but_click(b_2))
    b_3=Button(root, text= ' ', font=('Helvetica',20), height=3, width=6, bg='SystemButtonFace', command= lambda:but_click(b_3))

    b_4=Button(root, text= ' ', font=('Helvetica',20), height=3, width=6, bg='SystemButtonFace', command= lambda:but_click(b_4))
    b_5=Button(root, text= ' ', font=('Helvetica',20), height=3, width=6, bg='SystemButtonFace', command= lambda:but_click(b_5))
    b_6=Button(root, text= ' ', font=('Helvetica',20), height=3, width=6, bg='SystemButtonFace', command= lambda:but_click(b_6))

    b_7=Button(root, text= ' ', font=('Helvetica',20), height=3, width=6, bg='SystemButtonFace', command= lambda:but_click(b_7))
    b_8=Button(root, text= ' ', font=('Helvetica',20), height=3, width=6, bg='SystemButtonFace', command= lambda:but_click(b_8))
    b_9=Button(root, text= ' ', font=('Helvetica',20), height=3, width=6, bg='SystemButtonFace', command= lambda:but_click(b_9))

    b_1.grid(row=0,column=0)
    b_2.grid(row=0,column=1)
    b_3.grid(row=0,column=2)

    b_4.grid(row=1,column=0)
    b_5.grid(row=1,column=1)
    b_6.grid(row=1,column=2)

    b_7.grid(row=2,column=0)
    b_8.grid(row=2,column=1)
    b_9.grid(row=2,column=2)

menu_1=Menu(root)
root.config(menu=menu_1)
menu_options=Menu(menu_1, tearoff=False)
menu_1.add_cascade(label='Options', menu=menu_options)
menu_options.add_command(label='Reset game', command=reset)
reset()

root.mainloop()
