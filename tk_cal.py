import os
import sys
import math
from tkinter import *
from math import sqrt, pow, pi


# Resource path function to help build .exe with images and folders
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = Tk()
root['bg'] = '#7393B3'
root.title('Calculator')
root.resizable(False, False)
root.iconbitmap(resource_path("cal.ico"))

# Entry box for displaying input
e = Entry(root, width=26, font=('calibre', 15, 'bold'), borderwidth=5, justify=RIGHT)
e.insert(0, '0')
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Function to display the entered input
def button_click(number):
    if e.get() == '0':
        e.delete(0, END)
        e.insert(0, number)
    else:
        current = e.get()
        e.delete(0, END)
        e.insert(0, current + number)


# Function to clear the entry box
def button_clear():
    e.delete(0, END)
    e.insert(0, '0')


# Function for equal button to calculate the output
def button_equal():
    screen = e.get()
    e.delete(0, END)
    try:
        e.insert(0, eval(screen))
    except:
        e.delete(0, END)
        e.insert(0, 'Error')


# Function for clearing the entry box with escape key in keyboard
def esc_key(event):
    e.delete(0, END)
    e.insert(0, '0')


root.bind('<Escape>', esc_key)


# Function for calculating and displaying output when enter key on keyboard is pressed
def return_key(event):
    screen = e.get()
    e.delete(0, END)
    try:
        e.insert(0, eval(screen))
    except:
        e.delete(0, END)
        e.insert(0, 'Error')


root.bind('<Return>', return_key)


# Function for clearing one character every time the delete key is clicked
def button_del():
    if len(e.get()) > 1:
        s = e.get()
        l = list(s)
        l[-1], o = '', ''
        for i in l:
            o = o + i
        e.delete(0, END)
        e.insert(0, o)
    else:
        e.delete(0, END)
        e.insert(0, '0')


# Function for calculating percentage
def button_cent():
    s = round(eval(e.get())*100, 2)
    e.delete(0, END)
    e.insert(0, str(s) + '%')


# Initialising buttons
button_c = Button(root, width=1, text='C', font=('calibre', 15, 'bold'),
                  bg='#595959', fg='#f0f0f0', padx=30, pady=10, command=button_clear)
button_1 = Button(root, width=1, text='1', font=('calibre', 15, 'bold'),
                  bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('1'))
button_2 = Button(root, width=1, text='2', font=('calibre', 15, 'bold'),
                  bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('2'))
button_3 = Button(root, width=1, text='3', font=('calibre', 15, 'bold'),
                  bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('3'))
button_4 = Button(root, width=1, text='4', font=('calibre', 15, 'bold'),
                  bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('4'))
button_5 = Button(root, width=1, text='5', font=('calibre', 15, 'bold'),
                  bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('5'))
button_6 = Button(root, width=1, text='6', font=('calibre', 15, 'bold'),
                  bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('6'))
button_7 = Button(root, width=1, text='7', font=('calibre', 15, 'bold'),
                  bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('7'))
button_8 = Button(root, width=1, text='8', font=('calibre', 15, 'bold'),
                  bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('8'))
button_9 = Button(root, width=1, text='9', font=('calibre', 15, 'bold'),
                  bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('9'))
button_0 = Button(root, width=1, text='0', font=('calibre', 15, 'bold'),
                  bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('0'))
button_add = Button(root, width=1, text='+', font=('calibre', 15, 'bold'),
                    bg='#595959', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('+'))
button_sub = Button(root, width=1, text='-', font=('calibre', 15, 'bold'),
                    bg='#595959', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('-'))
button_mul = Button(root, width=1, text='*', font=('calibre', 15, 'bold'),
                    bg='#595959', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('*'))
button_div = Button(root, width=1, text='/', font=('calibre', 15, 'bold'),
                    bg='#595959', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('/'))
button_dot = Button(root, width=1, text='.', font=('calibre', 15, 'bold'),
                    bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('.'))
button_brac1 = Button(root, width=1, text='(', font=('calibre', 15, 'bold'),
                      bg='#595959', fg='#f0f0f0', padx=10, pady=10, command=lambda: button_click('('))
button_brac2 = Button(root, width=1, text=')', font=('calibre', 15, 'bold'),
                      bg='#595959', fg='#f0f0f0', padx=10, pady=10, command=lambda: button_click(')'))
button_comma = Button(root, width=1, text=',', font=('calibre', 15, 'bold'),
                   bg='#363636', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click(','))
button_del = Button(root, width=1, text='◄', font=('calibre', 15, 'bold'),
                    bg='#595959', fg='#f0f0f0', padx=30, pady=10, command=button_del)
button_equal = Button(root, width=1, text='=', font=('calibre', 15, 'bold'),
                      bg='#3399ff', fg='#f0f0f0', padx=30, pady=10, command=button_equal)
button_cent = Button(root, width=1, text='%', font=('calibre', 15, 'bold'),
                     bg='#595959', fg='#f0f0f0', padx=30, pady=10, command=button_cent)
button_pow = Button(root, width=1, text='xⁿ', font=('calibre', 15, 'bold'),
                    bg='#595959', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('pow('))
button_sqrt = Button(root, width=1, text='√x', font=('calibre', 15, 'bold'),
                     bg='#595959', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('sqrt('))
button_pi = Button(root, width=1, text='π', font=('calibre', 15, 'bold'),
                   bg='#595959', fg='#f0f0f0', padx=30, pady=10, command=lambda: button_click('pi'))

button_pi.grid(row=1, column=0)
button_brac1.grid(row=1, column=1, sticky=W)
button_brac2.grid(row=1, column=1, sticky=E)
button_c.grid(row=1, column=2)
button_del.grid(row=1, column=3)

button_cent.grid(row=2, column=0)
button_pow.grid(row=2, column=1)
button_sqrt.grid(row=2, column=2)
button_div.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_sub.grid(row=4, column=3)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_add.grid(row=5, column=3)

button_comma.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_dot.grid(row=6, column=2)
button_equal.grid(row=6, column=3)

root.mainloop()
