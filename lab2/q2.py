"""
from tkinter import *
from tkinter.ttk import *

MODE = "static" # Change to "dynamic" for dynamic keyboard layout
BLOCKS = 6
LOG_FILE = f"experiment_{MODE}_log.txt"
"""

import tkinter as tk
from tkinter.ttk import Button, Label
import random
import time
import csv
import string


NAME = "Andy"
MODE = "static"  # Change to "dynamic" for dynamic keyboard layout
BLOCKS = 6
LETTERS_PER_BLOCK = 6
KEY_SIZE = 64
LOG_FILE = f"experiment_{MODE}_log.txt"



target_letters = random.sample(string.ascii_lowercase, LETTERS_PER_BLOCK)

blocks = [random.sample(target_letters, LETTERS_PER_BLOCK) for i in range(BLOCKS)]
current_block = 0
current_index = 0
char_counts = {char: 0 for char in target_letters}
start_time = 0

window = tk.Tk()
window.title("tk")

target_var = tk.StringVar()


top_frame = tk.Frame(window)
top_frame.pack(fill=tk.X, padx=10, pady=10)

label = Label(top_frame, textvariable=target_var, font=("Arial", 20), foreground='black')
label.pack(fill=tk.X, expand=True)
label.config(anchor='center')

keyboard_frame = tk.Frame(window)
keyboard_frame.pack()


def log_selection(character, elapsed_ms):
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow([NAME, MODE, character, char_counts[character], f"{elapsed_ms:.1f}"])


def next_target():
    global current_index, current_block, start_time

    if current_block >= BLOCKS:
        target_var.set("Experiment Complete")
        return

    if current_index >= LETTERS_PER_BLOCK:
        current_index = 0
        current_block += 1

        if current_block >= BLOCKS:
            target_var.set("Experiment Complete")
            return

    target_char = blocks[current_block][current_index]
    char_counts[target_char] += 1
    target_var.set(f"Target: {target_char}")
    start_time = time.time()


keyboard_rows = [10, 9, 7]

def build_keyboard():
    for widget in keyboard_frame.winfo_children():
        widget.destroy()


    letters = list(string.ascii_lowercase)
    if MODE == "dynamic" or (current_block == 0 and current_index == 0):
        random.shuffle(letters)

    char_iter = iter(letters)
    for row_len in keyboard_rows:
        row = tk.Frame(keyboard_frame)
        row.pack(pady=2)
        for _ in range(row_len):
            char = next(char_iter)
            key_frame = tk.Frame(row, width=KEY_SIZE, height=KEY_SIZE)
            key_frame.pack_propagate(0)
            key_frame.pack(side=tk.LEFT, padx=2)
            btn = Button(key_frame, text=char, command=lambda c=char: key_pressed(c))
            btn.pack(fill=tk.BOTH, expand=1)


def key_pressed(char):
    global current_index
    expected = blocks[current_block][current_index]
    if char == expected:
        elapsed = (time.time() - start_time) * 1000
        log_selection(char, elapsed)
        current_index += 1
        if MODE == "dynamic":
            build_keyboard()
        next_target()
    else:

        pass


build_keyboard()
next_target()

window.mainloop()
