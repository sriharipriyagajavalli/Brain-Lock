import tkinter as tk
from tkinter import messagebox
import random

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("MindLock")
root.geometry("420x520")
root.configure(bg="#0f172a")

# ---------------- GAME STATE ----------------
level = 1
sequence = []
user_input = []

# ---------------- UI ----------------
title = tk.Label(
    root, text="MINDLOCK",
    font=("Arial", 26, "bold"),
    fg="#38bdf8", bg="#0f172a"
)
title.pack(pady=20)

info = tk.Label(
    root, text="Memorize the sequence",
    font=("Arial", 14),
    fg="white", bg="#0f172a"
)
info.pack()

display = tk.Label(
    root, text="",
    font=("Arial", 22, "bold"),
    fg="#22c55e", bg="#0f172a"
)
display.pack(pady=20)

frame = tk.Frame(root, bg="#0f172a")
frame.pack()

# ---------------- LOGIC ----------------
def generate_sequence():
    global sequence
    sequence = [random.randint(1, 4) for _ in range(level)]
    display.config(text=" ".join(map(str, sequence)))
    root.after(1200, lambda: display.config(text=""))

def press(n):
    global user_input
    user_input.append(n)
    if user_input != sequence[:len(user_input)]:
        messagebox.showerror("Access Denied", "Wrong sequence!")
        reset()
    elif len(user_input) == len(sequence):
        messagebox.showinfo("Unlocked", f"Level {level} cleared!")
        next_level()

def next_level():
    global level, user_input
    level += 1
    user_input = []
    info.config(text=f"Level {level}")
    root.after(500, generate_sequence)

def reset():
    global level, user_input
    level = 1
    user_input = []
    info.config(text="Memorize the sequence")
    generate_sequence()

# ---------------- BUTTONS ----------------
for i in range(1, 5):
    btn = tk.Button(
        frame, text=str(i),
        font=("Arial", 18, "bold"),
        width=5, height=2,
        bg="#1e293b", fg="white",
        command=lambda x=i: press(x)
    )
    btn.grid(row=(i-1)//2, column=(i-1)%2, padx=20, pady=20)

# ---------------- START ----------------
generate_sequence()
root.mainloop()
