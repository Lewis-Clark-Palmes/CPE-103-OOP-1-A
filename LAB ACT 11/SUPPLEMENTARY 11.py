import tkinter as tk
import math

def on_button_click(value):
    if value == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    elif value == "sin":
        try:
            result = str(math.sin(math.radians(float(entry.get()))))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "cos":
        try:
            result = str(math.cos(math.radians(float(entry.get()))))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "tan":
        try:
            result = str(math.tan(math.radians(float(entry.get()))))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "^":
        entry.insert(tk.END, "**")
    else:
        entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#2E2E2E")

entry = tk.Entry(root, width=20, font=("Arial", 16), bd=8, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear", command=clear_entry)

buttons = [
    ('C', 1, 0, 4),
    ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('/', 2, 3, 1),
    ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('*', 3, 3, 1),
    ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('-', 4, 3, 1),
    ('0', 5, 0, 1), ('.', 5, 1, 1), ('+', 5, 2, 1), ('=', 5, 3, 1),
    ('^', 6, 0, 1), ('sin', 6, 1, 1), ('cos', 6, 2, 1), ('tan', 6, 3, 1)
]

for text, row, col, colspan in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, columnspan=colspan, sticky="ew", padx=5, pady=5)

root.mainloop()
