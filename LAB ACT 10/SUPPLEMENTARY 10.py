import tkinter as tk
from tkinter import ttk, messagebox

# Create the main window
birthyear = tk.Tk()
birthyear.title("Birth Date Selector")
birthyear.geometry("450x300")
birthyear.configure(bg="#B0BEC5")

header = tk.Label(birthyear, text="Select Your Birth Date", font=("Verdana", 14, "bold"), bg="#B0BEC5", fg="black")
header.pack(pady=10)

mode = tk.StringVar(value="combo")

def toggle_mode():
    if mode.get() == "combo":
        combo_frame.pack()
        manual_frame.pack_forget()
    else:
        manual_frame.pack()
        combo_frame.pack_forget()

radio_frame = tk.Frame(birthyear, bg="#B0BEC5")
radio_frame.pack(pady=5)
tk.Radiobutton(radio_frame, text="Use Combo Box", variable=mode, value="combo", bg="#B0BEC5", command=toggle_mode).pack(side="left")
tk.Radiobutton(radio_frame, text="Manual Input", variable=mode, value="manual", bg="#B0BEC5", command=toggle_mode).pack(side="left")


combo_frame = tk.Frame(birthyear, bg="#B0BEC5")
combo_frame.pack()

tk.Label(combo_frame, text="Day", bg="#B0BEC5").grid(row=0, column=0, padx=5, pady=5, sticky="e")
day_combo = ttk.Combobox(combo_frame, width=5, values=[str(i) for i in range(1, 32)])
day_combo.grid(row=0, column=1, padx=5, pady=5)

tk.Label(combo_frame, text="Month", bg="#B0BEC5").grid(row=1, column=0, padx=5, pady=5, sticky="e")
month_combo = ttk.Combobox(combo_frame, width=10, values=['January', 'February', 'March', 'April', 'May', 'June',
                                                          'July', 'August', 'September', 'October', 'November', 'December'])
month_combo.grid(row=1, column=1, padx=5, pady=5)

tk.Label(combo_frame, text="Year", bg="#B0BEC5").grid(row=2, column=0, padx=5, pady=5, sticky="e")
year_combo = ttk.Combobox(combo_frame, width=6, values=[str(i) for i in range(1980, 2025)])
year_combo.grid(row=2, column=1, padx=5, pady=5)

manual_frame = tk.Frame(birthyear, bg="#B0BEC5")
tk.Label(manual_frame, text="Enter Birth Date (DD MM YYYY):", bg="#B0BEC5").pack(pady=5)
manual_entry = tk.Entry(manual_frame, width=30)
manual_entry.pack(pady=5)

def show_birthdate():
    if mode.get() == "combo":
        day = day_combo.get()
        month = month_combo.get()
        year = year_combo.get()
        if day and month and year:
            birthdate = f"{day} {month} {year}"
        else:
            messagebox.showwarning("Incomplete Data", "Please select all fields.")
            return
    else:
        birthdate = manual_entry.get()
        if not birthdate:
            messagebox.showwarning("Incomplete Data", "Please enter your birth date.")
            return
    messagebox.showinfo("Your Birth Date", f"Your Birth Date is: {birthdate}")

submit_button = tk.Button(birthyear, text="Display Birth Date", command=show_birthdate, bg="#607D8B", fg="white", font=("Arial", 10))
submit_button.pack(pady=15)

toggle_mode()

birthyear.mainloop()