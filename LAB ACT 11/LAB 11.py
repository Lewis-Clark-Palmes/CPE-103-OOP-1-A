import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#2E2E2E")

entry = tk.Entry(root ,width=20, font=("Arial", 16), bd=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    ('C', 1, 0, 4),
    ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('/', 2, 3, 1),
    ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('*', 3, 3, 1),
    ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('-', 4, 3, 1),
    ('0', 5, 0, 1), ('.', 5, 1, 1), ('+', 5, 2, 1), ('=', 5, 3, 1)
]

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
    else:
        entry.insert(tk.END, value)

for text, row, col, colspan in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, columnspan=colspan, sticky="ew", padx=5, pady=5)

root.mainloop()
