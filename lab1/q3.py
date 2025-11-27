"""
from tkinter import *
from tkinter.ttk import *
def add_one():
    value.set(value.get()+1)

def wow(event):
    label2.config(text="WWWWOOOOWWWW")

window = Tk()
value = IntVar(window, 0)
label = Label(window, textvariable=value)
label.pack()
label2 = Label(window)
label2.pack()
button = Button(window, text="Add one", command=add_one)
button.bind("<Shift-Double-Button-1>", wow)
button.pack()
window.mainloop()
"""

"""
from tkinter import *
from tkinter.ttk import *

def change(the_value, n):
    the_value.set(the_value.get()+n)

window = Tk()
value = IntVar(window, 0)
label = Label(window, textvariable=value)
label.pack()
button = Button(window, text="Left +1, Right -1")
button.bind("<Button-1>", lambda event: change(value, 1))
button.bind("<Button-3>", lambda event: change(value, -1))
button.pack()
window.mainloop()
"""

from tkinter import *
from tkinter.ttk import *

window = Tk()

text_var = StringVar()
text_var.set("")

label = Label(window, textvariable=text_var, font=("Arial", 16))
label.pack(padx=10, pady=10, fill=X)

board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

def append(char):
    current = text_var.get()
    text_var.set(current + char)

def clear_text():
    text_var.set("")

clear_button = Button(window, text="Clear", command=clear_text)
clear_button.pack(side=TOP, anchor=NE)

for row in board:
    frame = Frame(window)
    frame.pack(pady=5)
    for ch in row:
        b = Button(frame, text=ch, command=lambda x=ch: append(x))
        b.pack(side=LEFT, padx=2)


window.mainloop()

