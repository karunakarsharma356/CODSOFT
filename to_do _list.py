import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        self.task_number = 1

        self.task_label = tk.Label(root, text="Task")
        self.task_label.grid(row=0, column=0)
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=1)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=1, column=0, columnspan=3)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=0)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1)

        self.clear_button = tk.Button(root, text="Clear Tasks", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=2)

        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_as_complete)
        self.complete_button.grid(row=3, column=0, columnspan=3)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.listbox.insert(tk.END, f"Task {self.task_number}: {task} (Not Completed)")
            self.task_number += 1
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task")

    def update_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            task = self.task_entry.get()
            if task:
                self.tasks[task_index]["task"] = task
                self.listbox.delete(task_index)
                if self.tasks[task_index]["completed"]:
                    self.listbox.insert(task_index, f"Task {task_index + 1}: {task} (Completed)")
                else:
                    self.listbox.insert(task_index, f"Task {task_index + 1}: {task} (Not Completed)")
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter a task")
        except:
            messagebox.showerror("Error", "Please select a task to update")

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.tasks.pop(task_index)
            self.listbox.delete(task_index)
            self.task_number -= 1
        except:
            messagebox.showerror("Error", "Please select a task to delete")

    def clear_tasks(self):
        self.tasks.clear()
        self.listbox.delete(0, tk.END)
        self.task_number = 1

    def mark_as_complete(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.tasks[task_index]["completed"] = True
            self.listbox.delete(task_index)
            self.listbox.insert(task_index, f"Task {task_index + 1}: {self.tasks[task_index]['task']} (Completed)")
        except:
            messagebox.showerror("Error", "Please select a task to mark as complete")

root = tk.Tk()
to_do_list = ToDoList(root)
root.mainloop()
