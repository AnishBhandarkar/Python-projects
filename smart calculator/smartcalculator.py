# python C:\Users\ANISH\Desktop\my\ani_py_files\practicepyt.py

# Calculator

from tkinter import *
from tkinter import messagebox
import math

screen = Tk()
screen.title("Calculator")
screen.configure(bg='pink')

screen.iconbitmap('calci.ico')
screen.maxsize(width=470, height=490)
screen.minsize(width=470, height=490)



def click(number):
    global operator
    operator += str(number)
    tex.set(operator)


def clear():
    global operator
    operator = ''
    tex.set(operator)


def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong', parent=screen)


def cmsin():
    try:
        global operator
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong', parent=screen)


def cmcos():
    try:
        global operator
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong', parent=screen)


def cmtan():
    try:
        global operator
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong', parent=screen)


def cmsqrt():
    try:
        global operator
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong', parent=screen)


def cmlog():
    try:
        global operator
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong', parent=screen)


##############################################Binding functions
def on_enterentry(e):
    entry1.configure(bg='salmon', fg='white')


def on_leaventry(e):
    entry1.configure(bg='orange', fg='black')


def on_enter7(e):
    btn7.configure(bg='deep pink')


def on_leave7(e):
    btn7.configure(bg='aquamarine')


def on_enter8(e):
    btn8.configure(bg='deep pink')


def on_leave8(e):
    btn8.configure(bg='aquamarine')


def on_enter9(e):
    btn9.configure(bg='deep pink')


def on_leave9(e):
    btn9.configure(bg='aquamarine')


def on_enteradd(e):
    btnadd.configure(bg='RoyalBlue1')


def on_leaveadd(e):
    btnadd.configure(bg='medium orchid')


def on_enter4(e):
    btn4.configure(bg='deep pink')


def on_leave4(e):
    btn4.configure(bg='aquamarine')


def on_enter5(e):
    btn5.configure(bg='deep pink')


def on_leave5(e):
    btn5.configure(bg='aquamarine')


def on_enter6(e):
    btn6.configure(bg='deep pink')


def on_leave6(e):
    btn6.configure(bg='aquamarine')


def on_entersub(e):
    btnsub.configure(bg='RoyalBlue1')


def on_leavesub(e):
    btnsub.configure(bg='medium orchid')


def on_enter1(e):
    btn1.configure(bg='deep pink')


def on_leave1(e):
    btn1.configure(bg='aquamarine')


def on_enter2(e):
    btn2.configure(bg='deep pink')


def on_leave2(e):
    btn2.configure(bg='aquamarine')


def on_enter3(e):
    btn3.configure(bg='deep pink')


def on_leave3(e):
    btn3.configure(bg='aquamarine')


def on_entermul(e):
    btnmul.configure(bg='RoyalBlue1')


def on_leavemul(e):
    btnmul.configure(bg='medium orchid')


def on_enter0(e):
    btn0.configure(bg='deep pink')


def on_leave0(e):
    btn0.configure(bg='aquamarine')


def on_enterclear(e):
    btnclear.configure(bg='lime green')


def on_leaveclear(e):
    btnclear.configure(bg='yellow')


def on_enterequal(e):
    btnequal.configure(bg='lime green')


def on_leaveequal(e):
    btnequal.configure(bg='yellow')


def on_enterdiv(e):
    btndiv.configure(bg='RoyalBlue1')


def on_leavediv(e):
    btndiv.configure(bg='medium orchid')


def on_entersin(e):
    btnsin.configure(bg='green2')


def on_leavesin(e):
    btnsin.configure(bg='brown1')


def on_entercos(e):
    btncos.configure(bg='green2')


def on_leavecos(e):
    btncos.configure(bg='brown1')


def on_entertan(e):
    btntan.configure(bg='green2')


def on_leavetan(e):
    btntan.configure(bg='brown1')


def on_entersqrt(e):
    btnsqrt.configure(bg='green2')


def on_leavesqrt(e):
    btnsqrt.configure(bg='brown1')


def on_enterlog(e):
    btnlog.configure(bg='green2')


def on_leavelog(e):
    btnlog.configure(bg='brown1')


tex = StringVar()
operator = ''

entry1 = Entry(screen, bg='orange', font=('arial', 20, 'italic bold'), bd='30', justify='right', textvariable=tex)
entry1.grid(row=0, columnspan=4)

btn7 = Button(screen, text='7', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click(7),
              activebackground='green', activeforeground='white', bg='aquamarine')
btn7.grid(row=1, column=0)

btn8 = Button(screen, text='8', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click(8),
              activebackground='green', activeforeground='white', bg='aquamarine')
btn8.grid(row=1, column=1)

btn9 = Button(screen, text='9', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click(9),
              activebackground='green', activeforeground='white', bg='aquamarine')
btn9.grid(row=1, column=2)

btnadd = Button(screen, text='+', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click('+'),
                activebackground='green', activeforeground='white', bg='medium orchid')
btnadd.grid(row=1, column=3)

btn4 = Button(screen, text='4', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click(4),
              activebackground='green', activeforeground='white', bg='aquamarine')
btn4.grid(row=2, column=0)

btn5 = Button(screen, text='5', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click(5),
              activebackground='green', activeforeground='white', bg='aquamarine')
btn5.grid(row=2, column=1)

btn6 = Button(screen, text='6', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click(6),
              activebackground='green', activeforeground='white', bg='aquamarine')
btn6.grid(row=2, column=2)

btnsub = Button(screen, text='-', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click('-'),
                activebackground='green', activeforeground='white', bg='medium orchid')
btnsub.grid(row=2, column=3)

btn1 = Button(screen, text='1', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click(1),
              activebackground='green', activeforeground='white', bg='aquamarine')
btn1.grid(row=3, column=0)

btn2 = Button(screen, text='2', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click(2),
              activebackground='green', activeforeground='white', bg='aquamarine')
btn2.grid(row=3, column=1)

btn3 = Button(screen, text='3', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click(3),
              activebackground='green', activeforeground='white', bg='aquamarine')
btn3.grid(row=3, column=2)

btnmul = Button(screen, text='*', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click('*'),
                activebackground='green', activeforeground='white', bg='medium orchid')
btnmul.grid(row=3, column=3)

btn0 = Button(screen, text='0', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click(0),
              activebackground='green', activeforeground='white', bg='aquamarine')
btn0.grid(row=4, column=0)

btnclear = Button(screen, text='c', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=clear,
                  activebackground='green', activeforeground='white', bg='yellow')
btnclear.grid(row=4, column=1)

btnequal = Button(screen, text='=', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=equal,
                  activebackground='green', activeforeground='white', bg='yellow')
btnequal.grid(row=4, column=2)

btndiv = Button(screen, text='/', font=('arial', 20, 'italic bold'), bd=8, padx=16, pady=16, command=lambda: click('/'),
                activebackground='green', activeforeground='white', bg='medium orchid')
btndiv.grid(row=4, column=3)

################################################### Advance calculation

btnsin = Button(screen, text='sin', font=('arial', 15, 'italic bold'), bd=8, padx=23, pady=20, command=cmsin,
                activebackground='green', activeforeground='white', bg='brown1')
btnsin.grid(row=0, column=4)

btncos = Button(screen, text='cos', font=('arial', 20, 'italic bold'), bd=8, padx=12, pady=14, command=cmcos,
                activebackground='green', activeforeground='white', bg='brown1')
btncos.grid(row=1, column=4)

btntan = Button(screen, text='tan', font=('arial', 20, 'italic bold'), bd=8, padx=15, pady=14, command=cmtan,
                activebackground='green', activeforeground='white', bg='brown1')
btntan.grid(row=2, column=4)

btnsqrt = Button(screen, text='sqrt', font=('arial', 20, 'italic bold'), bd=8, padx=10, pady=14, command=cmsqrt,
                 activebackground='green', activeforeground='white', bg='brown1')
btnsqrt.grid(row=3, column=4)

btnlog = Button(screen, text='log', font=('arial', 20, 'italic bold'), bd=8, padx=15, pady=14, command=cmlog,
                activebackground='green', activeforeground='white', bg='brown1')
btnlog.grid(row=4, column=4)

################################################### Binding
btnsin.bind('<Enter>', on_entersin)
btnsin.bind('<Leave>', on_leavesin)

btncos.bind('<Enter>', on_entercos)
btncos.bind('<Leave>', on_leavecos)

btntan.bind('<Enter>', on_entertan)
btntan.bind('<Leave>', on_leavetan)

btnsqrt.bind('<Enter>', on_entersqrt)
btnsqrt.bind('<Leave>', on_leavesqrt)

btnlog.bind('<Enter>', on_enterlog)
btnlog.bind('<Leave>', on_leavelog)

entry1.bind('<Enter>', on_enterentry)
entry1.bind('<Leave>', on_leaventry)

btn7.bind('<Enter>', on_enter7)
btn7.bind('<Leave>', on_leave7)

btn8.bind('<Enter>', on_enter8)
btn8.bind('<Leave>', on_leave8)

btn9.bind('<Enter>', on_enter9)
btn9.bind('<Leave>', on_leave9)

btnadd.bind('<Enter>', on_enteradd)
btnadd.bind('<Leave>', on_leaveadd)

btn4.bind('<Enter>', on_enter4)
btn4.bind('<Leave>', on_leave4)

btn5.bind('<Enter>', on_enter5)
btn5.bind('<Leave>', on_leave5)

btn6.bind('<Enter>', on_enter6)
btn6.bind('<Leave>', on_leave6)

btnsub.bind('<Enter>', on_entersub)
btnsub.bind('<Leave>', on_leavesub)

btn1.bind('<Enter>', on_enter1)
btn1.bind('<Leave>', on_leave1)

btn2.bind('<Enter>', on_enter2)
btn2.bind('<Leave>', on_leave2)

btn3.bind('<Enter>', on_enter3)
btn3.bind('<Leave>', on_leave3)

btnmul.bind('<Enter>', on_entermul)
btnmul.bind('<Leave>', on_leavemul)

btn0.bind('<Enter>', on_enter0)
btn0.bind('<Leave>', on_leave0)

btnclear.bind('<Enter>', on_enterclear)
btnclear.bind('<Leave>', on_leaveclear)

btnequal.bind('<Enter>', on_enterequal)
btnequal.bind('<Leave>', on_leaveequal)

btndiv.bind('<Enter>', on_enterdiv)
btndiv.bind('<Leave>', on_leavediv)

screen.mainloop()
