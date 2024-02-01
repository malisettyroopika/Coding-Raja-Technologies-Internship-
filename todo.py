import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tasks = []

def add_task():
    task_title = task_entry.get()
    if task_title:
        new_task = f"{task_title} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        tasks.append(new_task)
        task_listbox.insert(tk.END, new_task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        task_listbox.delete(selected_index)
        del tasks[selected_index[0]]
def mark_completed():
    selected_index = task_listbox.curselection()
    if selected_index:
        task = tasks[selected_index[0]]
        task += " - Completed"
        task_listbox.delete(selected_index)
        tasks[selected_index[0]] = task
        task_listbox.insert(tk.END, task)

root = tk.Tk()
root.title("To-Do List App")

# Create widgets
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
complete_button = tk.Button(root, text="Mark Completed", command=mark_completed)

# Grid layout
task_entry.grid(row=0, column=0, padx=10, pady=10)
add_button.grid(row=0, column=1, padx=10, pady=10)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
remove_button.grid(row=2, column=0, padx=10, pady=10)
complete_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()