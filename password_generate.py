import tkinter as tk
from tkinter import messagebox
import random
import string

class PassGen:
    def __init__(self, root):
        self.root = root

        self.length_label = tk.Label(root, text="Enter password length:")
        self.length_label.grid(row=0, column=0)
        self.length_entry = tk.Entry(root, width=20)
        self.length_entry.grid(row=0, column=1)

        self.lowercase_var = tk.IntVar()
        self.lowercase_checkbox = tk.Checkbutton(root, text="Include lowercase letters", variable=self.lowercase_var)
        self.lowercase_checkbox.grid(row=1, column=0)

        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbox = tk.Checkbutton(root, text="Include uppercase letters", variable=self.uppercase_var)
        self.uppercase_checkbox.grid(row=1, column=1)

        self.digits_var = tk.IntVar()
        self.digits_checkbox = tk.Checkbutton(root, text="Include digits", variable=self.digits_var)
        self.digits_checkbox.grid(row=2, column=0)

        self.special_chars_var = tk.IntVar()
        self.special_chars_checkbox = tk.Checkbutton(root, text="Include special characters", variable=self.special_chars_var)
        self.special_chars_checkbox.grid(row=2, column=1)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.password1)
        self.generate_button.grid(row=3, column=0, columnspan=2)

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.grid(row=4, column=0)
        self.password_entry = tk.Entry(root, width=40)
        self.password_entry.grid(row=4, column=1)

    def password1(self):
        length = self.length_entry.get()
        if length.isdigit() and int(length) > 0:
            length = int(length)
            chars = ''
            if self.lowercase_var.get():
                chars += string.ascii_lowercase
            if self.uppercase_var.get():
                chars += string.ascii_uppercase
            if self.digits_var.get():
                chars += string.digits
            if self.special_chars_var.get():
                chars += string.punctuation
            if chars:
                password = ''.join(random.choice(chars) for i in range(length))
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, password)
            else:
                messagebox.showerror("Error", "Please select at least one character type")
        else:
            messagebox.showerror("Error", "Please enter a valid password length")

root = tk.Tk()
password_generator = PassGen(root)
root.mainloop()
