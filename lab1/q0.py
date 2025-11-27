#question 1
"""
from tkinter import *
from tkinter.ttk import *
window = Tk()
data = StringVar()
data.set("Data to display")
label = Label(window, textvariable=data)
label.grid(row=0, column=0)
entry = Entry(window, textvariable=data)
entry.grid(row=1, column=0)
window.mainloop()
"""


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

#question 2
"""
from tkinter import *
from tkinter.ttk import *

window = Tk()

for label_num in range(6):
    button = Button(window, text="Button"+str(label_num))
    button.grid(row=label_num // 2, column=label_num % 3)

window.mainloop()
"""

#question 2
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

#question 2
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

"""
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Text Widget with Scrollbars")

# Create a frame to hold the Text widget and scrollbars
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create vertical scrollbar
v_scroll = ttk.Scrollbar(frame, orient=tk.VERTICAL)
v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Create horizontal scrollbar
h_scroll = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

# Create Text widget
text = tk.Text(
    frame,
    wrap="none",  # Disable line wrapping to use horizontal scrolling
    width=24,
    height=10,
    yscrollcommand=v_scroll.set,
    xscrollcommand=h_scroll.set
)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure scrollbars to control the Text widget
v_scroll.config(command=text.yview)
h_scroll.config(command=text.xview)

# Insert some sample text (optional)
text.insert(tk.END, "This is an example of a Text widget.\nYou can scroll horizontally and vertically.")

# Start the main event loop
root.mainloop()
"""

