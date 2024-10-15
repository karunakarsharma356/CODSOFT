import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.entry = tk.Entry(master, width=20)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(master, text="AC", width=10, command=self.clear).grid(row=row_val, column=0, columnspan=2)
        tk.Button(master, text="+/-", width=5, command=self.negate).grid(row=row_val, column=2)
        tk.Button(master, text="del", width=5, command=self.delete).grid(row=row_val, column=3)

    def click_button(self, button):
        if button == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

    def clear(self):
        self.entry.delete(0, tk.END)

    def negate(self):
        current_value = self.entry.get()
        if current_value != "":
            if current_value[0] == "-":
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, current_value[1:])
            else:
                self.entry.insert(tk.END, "-")
    def delete(self):
        current_value = self.entry.get()
        if current_value != "":
            self.entry.delete(len(current_value) - 1, tk.END)

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()
