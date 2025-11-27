#question 2
"""
from tkinter import *
from tkinter.ttk import *

window = Tk()

side_labels = ["bottom1", "bottom2", "top1", "top2", "left1", "right1"]

for theside in side_labels:

    button = Button(window, text=theside)
    button.pack(side=theside[0:-1])

window.mainloop()
"""


"""
from tkinter import *
from tkinter.ttk import *

window = Tk()

for label_num in range(6):
    button = Button(window, text="Button"+str(label_num))
    button.grid(row=label_num // 2, column=label_num % 3)

window.mainloop()
"""

"""
from tkinter import *
from tkinter.ttk import *

window = Tk()

for label_num in range(6):
    button = Button(window, text="Button" + str(label_num))
    button.grid(row=label_num // 2, column=label_num % 3)
    if label_num == 1:
        button.grid(columnspan=2, sticky="ew") # compass directions (N, E, S, W)
    elif label_num == 3:
        button.grid(rowspan=2, sticky="ns") # compass directions (N, E, S, W)

window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.mainloop()
"""

"""
from tkinter import *
from tkinter.ttk import *

window = Tk()

frame_left = Frame(window, borderwidth=4, relief=RIDGE)
frame_left.pack(side="left", fill="y", padx=5, pady=5)
frame_right = Frame(window)
frame_right.pack(side="right")
button1 = Button(frame_left, text="Button 1")
button1.pack(side="top")
button2 = Button(frame_left, text="Button 2")
button2.pack(side="bottom")
for label_num in range(4):
    button = Button(frame_right, text="Button" + str(label_num + 3))
    button.grid(row=label_num // 2, column=label_num % 2)
window.mainloop()
"""


from tkinter import *
from tkinter.ttk import *

window = Tk()

frame = Frame(window)
frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

v_scroll = Scrollbar(frame, orient=VERTICAL)
v_scroll.pack(side=RIGHT, fill=Y)

h_scroll = Scrollbar(frame, orient=HORIZONTAL)
h_scroll.pack(side=BOTTOM, fill=X)

text = Text(
        frame,
        wrap="none",
        width=24,
        height=10,
        yscrollcommand=v_scroll.set,
        xscrollcommand=h_scroll.set)
text.pack(side=LEFT, fill=BOTH, expand=True)

v_scroll.config(command=text.yview)
h_scroll.config(command=text.xview)

text.insert(END, """This lab aims to familiarise you with Graphical User
 Interface (GUI) programming with Python/TkInter. Many of the basic concepts
 of GUI programming are similar across programming platforms. While Python
 itself has many toolkits for making your own GUIs, Tkinter is good for
 learning the basics of UI development.
 At the end of this lab, you should understand the basics of the following:

1. Widget creation with Python/TkInter.

2. Geometry management with the "packer" and "gridder".

3. Event binding. """)

window.mainloop()


"""
from tkinter import *
from tkinter.ttk import *

# Create the main window
root = Tk()
root.title("Text Widget with Scrollbars")

# Create a frame to hold the Text widget and scrollbars
frame = Frame(root)
frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Create vertical scrollbar
v_scroll = Scrollbar(frame, orient=VERTICAL)
v_scroll.pack(side=RIGHT, fill=Y)

# Create horizontal scrollbar
h_scroll = Scrollbar(frame, orient=HORIZONTAL)
h_scroll.pack(side=BOTTOM, fill=X)

# Create Text widget (note: use Text from tkinter, not ttk)
text = Text(
    frame,
    wrap="none",        # No wrapping, so horizontal scrolling is enabled
    width=24,
    height=10,
    yscrollcommand=v_scroll.set,
    xscrollcommand=h_scroll.set
)
text.pack(side=LEFT, fill=BOTH, expand=True)

# Configure scrollbars
v_scroll.config(command=text.yview)
h_scroll.config(command=text.xview)

# Insert some sample text (optional)
text.insert(END, "This is an example of a Text widget.\nYou can scroll horizontally and vertically.")

# Start the main event loop
root.mainloop()
"""
