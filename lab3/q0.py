"""
from tkinter import *
from tkinter.ttk import *

master = Tk()
c = Canvas(master, width=200, height=200)
c.pack()
c.create_line(0, 0, 200, 100, tag='cool')
c.create_line(0, 100, 200, 0, fill="red", dash=(4, 4), tag='cool')
rect = c.create_rectangle(50, 25, 150, 75, fill="blue")

c.itemconfigure('cool', fill='blue')
c.itemconfigure(rect, fill='red')
#c.coords(rect, 10, 10, 50, 100)

master.mainloop()
"""

import tkinter as tk
import random
import time
import csv

# Experiment settings
distances = [64, 128, 256, 512]
widths = [8, 16, 32]
repetitions = 4  # Even number
username = "Andy"

# Generate all combinations and shuffle
conditions = [(d, w) for d in distances for w in widths]
random.shuffle(conditions)

# Setup log file
logfile = open("fitts_log.csv", "w", newline="")
logger = csv.writer(logfile)
logger.writerow(["Name", "Distance", "Width", "Selection#", "Time"])

# Tkinter setup
root = tk.Tk()
canvas_width = 800
canvas_height = 300
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# State tracking
condition_index = 0
selection_number = 0
current_side = 'left'
start_time = 0
target_ids = {}

def get_margin(distance, width):
    total_span = distance + width
    return (canvas_width - total_span) // 2

def draw_targets(distance, width, active_side):
    canvas.delete("all")
    margin = get_margin(distance, width)

    # Left and right bar positions
    left_x0 = margin
    left_x1 = margin + width

    right_x0 = margin + distance
    right_x1 = right_x0 + width

    left_color = "green" if active_side == 'left' else "blue"
    right_color = "green" if active_side == 'right' else "blue"

    left = canvas.create_rectangle(left_x0, 0, left_x1, canvas_height, fill=left_color, tags="left")
    right = canvas.create_rectangle(right_x0, 0, right_x1, canvas_height, fill=right_color, tags="right")

    # Store target rectangles
    global target_ids, start_time
    target_ids = {"left": left, "right": right}
    start_time = time.time()

def on_click(event):
    global selection_number, condition_index, current_side, start_time

    clicked_items = canvas.find_withtag("current")
    if not clicked_items:
        return

    if clicked_items[0] != target_ids[current_side]:
        return  # Clicked wrong target

    # Record reaction time
    elapsed = (time.time() - start_time) * 1000  # ms
    distance, width = conditions[condition_index]
    selection_number += 1

    logger.writerow([username, distance, width, selection_number, round(elapsed, 2)])

    # Switch side
    current_side = 'right' if current_side == 'left' else 'left'

    if selection_number >= repetitions:
        # Move to next condition
        selection_number = 0
        condition_index += 1
        if condition_index >= len(conditions):
            print("Experiment finished.")
            logfile.close()
            root.destroy()
            return

    # Draw next
    distance, width = conditions[condition_index]
    draw_targets(distance, width, current_side)

# Start experiment
canvas.bind("<Button-1>", on_click)
initial_distance, initial_width = conditions[condition_index]
draw_targets(initial_distance, initial_width, current_side)

root.mainloop()
