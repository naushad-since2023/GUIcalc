import tkinter as tk
import math

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def clear_memory():
    memory.set("")

def store_to_memory():
    memory.set(entry.get())

def recall_memory():
    entry.insert(tk.END, memory.get())

def square_root():
    try:
        result = math.sqrt(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Enhanced Calculator")

# Entry widget to display and input numbers/expressions
entry = tk.Entry(window, width=30, borderwidth=5, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Button widget layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('%', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('√', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('M+', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('M-', 4, 4),
]

# Memory variable
memory = tk.StringVar()
memory.set("")

# Creating and placing buttons
for (text, row, column) in buttons:
    button = tk.Button(window, text=text, padx=20, pady=10, font=('Arial', 12),
                       command=lambda t=text: entry.insert(tk.END, t))
    button.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

# Special functions: Calculate, Clear, Clear Memory, Store to Memory, Recall from Memory, Square Root
calculate_button = tk.Button(window, text="Calculate", padx=20, pady=10, font=('Arial', 12),
                             command=calculate)
calculate_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky='nsew')

clear_button = tk.Button(window, text="Clear", padx=20, pady=10, font=('Arial', 12), command=clear)
clear_button.grid(row=5, column=4, padx=5, pady=5, sticky='nsew')

clear_memory_button = tk.Button(window, text="MC", padx=10, pady=5, font=('Arial', 12),
                                command=clear_memory)
clear_memory_button.grid(row=6, column=0, padx=5, pady=5, sticky='nsew')

store_memory_button = tk.Button(window, text="MS", padx=10, pady=5, font=('Arial', 12),
                                command=store_to_memory)
store_memory_button.grid(row=6, column=1, padx=5, pady=5, sticky='nsew')

recall_memory_button = tk.Button(window, text="MR", padx=10, pady=5, font=('Arial', 12),
                                 command=recall_memory)
recall_memory_button.grid(row=6, column=2, padx=5, pady=5, sticky='nsew')

square_root_button = tk.Button(window, text="√", padx=10, pady=5, font=('Arial', 12),
                               command=square_root)
square_root_button.grid(row=6, column=3, padx=5, pady=5, sticky='nsew')

# Displaying the memory
memory_label = tk.Label(window, textvariable=memory, font=('Arial', 12))
memory_label.grid(row=7, column=0, columnspan=5, padx=10, pady=5, sticky='nsew')

window.mainloop()
