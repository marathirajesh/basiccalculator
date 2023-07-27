import tkinter as tk

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

def create_button(root, text, row, col, width=10, height=2):
    button = tk.Button(root, text=text, width=width, height=height,
                       command=lambda: on_click(text))
    button.grid(row=row, column=col, padx=5, pady=5)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=30, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0),
]

for (button_text, row, col) in buttons:
    create_button(root, button_text, row, col)

root.mainloop()

