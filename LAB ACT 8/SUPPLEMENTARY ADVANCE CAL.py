import tkinter as tk
from tkinter import messagebox
import math

# Functions for calculations
def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
        add_history(f"{entry1.get()} + {entry2.get()} = {result.get()}")
    except ValueError:
        result.set("Invalid input!")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
        add_history(f"{entry1.get()} - {entry2.get()} = {result.get()}")
    except ValueError:
        result.set("Invalid input!")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
        add_history(f"{entry1.get()} * {entry2.get()} = {result.get()}")
    except ValueError:
        result.set("Invalid input!")

def divide():
    try:
        if float(entry2.get()) == 0:
            result.set("Error! Division by zero.")
        else:
            result.set(float(entry1.get()) / float(entry2.get()))
            add_history(f"{entry1.get()} / {entry2.get()} = {result.get()}")
    except ValueError:
        result.set("Invalid input!")

def power():
    try:
        result.set(float(entry1.get()) ** float(entry2.get()))
        add_history(f"{entry1.get()} ^ {entry2.get()} = {result.get()}")
    except ValueError:
        result.set("Invalid input!")

def square_root():
    try:
        num = float(entry1.get())
        result.set(math.sqrt(num))
        add_history(f"√{num} = {result.get()}")
    except ValueError:
        result.set("Invalid input!")

def add_history(entry):
    history_list.insert(tk.END, entry)

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")
    history_list.delete(0, tk.END)

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x400")

root.configure(bg="pink")
font_style = ("Arial", 12)

result = tk.StringVar()

tk.Label(root, text="First Number:", font=font_style, bg="pink").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number:", font=font_style, bg="pink").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)


tk.Button(root, text="Add", command=add).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=1)
tk.Button(root, text="Power", command=power).grid(row=4, column=0)
tk.Button(root, text="Square Root", command=square_root).grid(row=4, column=1)


tk.Button(root, text="Clear All", command=clear, bg="red", fg="white").grid(row=5, column=0, columnspan=2)


tk.Label(root, text="Operation History:", font=font_style, bg="pink").grid(row=6, column=0)
history_list = tk.Listbox(root, height=5, width=30)
history_list.grid(row=7, column=0, columnspan=2)


tk.Label(root, text="Result:", font=font_style, bg="pink").grid(row=8, column=0)
tk.Label(root, textvariable=result, font=("Arial", 14), bg="white", relief="solid").grid(row=8, column=1)

root.mainloop()
