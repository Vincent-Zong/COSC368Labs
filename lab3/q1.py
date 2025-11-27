import tkinter as tk
import random
import time
import csv

# Settings
distances = [64, 128, 256, 512]
widths = [8, 16, 32]
username = "Andy"
repetitions = 8  # Even number of task repetitions

# All distance-width combinations in random order
combination = []
for distance in distances:
    for width in widths:
        combination.append((distance, width))
random.shuffle(combination)

logfile = open("fitts_log.csv", "w", newline="")
logger = csv.writer(logfile)
logger.writerow(["Name", "Distance", "Width", "Selection#", "Time"])

window = tk.Tk()
canvas = tk.Canvas(window, width=800, height=300)
canvas.pack()

condition_index = 0
selection_number = 0
current_side = "left"
start_time = 0
target_ids = {}

def get_margin(distance, width):
    total_span = distance + width
    return (800 - total_span) // 2

def draw_targets(distance, width, active_side):
    canvas.delete("all")
    margin = get_margin(distance, width)

    leftx0 = margin
    leftx1 = margin + width

    rightx0 = margin + distance
    rightx1 = rightx0 + width

    left_color = "green" if active_side == "left" else "blue"
    right_color = "green" if active_side == "right" else "blue"

    left = canvas.create_rectangle(leftx0, 0, leftx1, 300, fill=left_color, tags="left")
    right = canvas.create_rectangle(rightx0, 0, rightx1, 300, fill=right_color, tags="right")

    global target_ids, start_time
    target_ids = {"left": left, "right": right}
    start_time = time.time()

def on_click(event):
    global selection_number, condition_index, current_side, start_time

    clicked_items = canvas.find_withtag("current")
    if not clicked_items:
        return
    if clicked_items[0] != target_ids[current_side]:
        return  # Wrong target

    time_taken = (time.time() - start_time) * 1000  # time in milliseconds
    distance, width = combination[condition_index]
    selection_number += 1

    logger.writerow([username, distance, width, selection_number, time_taken])

    current_side = "right" if current_side == "left" else "left"

    if selection_number >= repetitions:
        selection_number = 0
        condition_index += 1
        if condition_index >= len(combination):
            print("Experiment finished.")
            logfile.close()
            window.destroy()
            return

    distance, width = combination[condition_index]
    draw_targets(distance, width, current_side)


canvas.bind("<Button-1>", on_click)
initial_distance, initial_width = combination[condition_index]
draw_targets(initial_distance, initial_width, current_side)

window.mainloop()
