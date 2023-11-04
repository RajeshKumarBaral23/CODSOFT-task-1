import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stylish To-Do List")

        self.todo_list = []

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_item, font=("Arial", 12))
        self.add_button.pack()

        self.todo_display = tk.Listbox(root, selectbackground="lightblue", font=("Arial", 12))
        self.todo_display.pack()

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_item, font=("Arial", 12))
        self.complete_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_item, font=("Arial", 12))
        self.delete_button.pack()

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_item, font=("Arial", 12))
        self.edit_button.pack()

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Arial", 12))
        self.copy_button.pack()

        self.search_entry = tk.Entry(root, font=("Arial", 12))
        self.search_entry.pack()
        self.search_button = tk.Button(root, text="Search", command=self.search, font=("Arial", 12))
        self.search_button.pack()

    def add_item(self):
        item = self.entry.get()
        if item:
            self.todo_list.append({"task": item, "completed": False})
            self.todo_display.insert(tk.END, item)
            self.entry.delete(0, tk.END)

    def delete_item(self):
        selected_task_index = self.todo_display.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            item = self.todo_list.pop(index)
            self.todo_display.delete(index)
            print(f'Deleted item: {item["task"]}')

    def edit_item(self):
        selected_task_index = self.todo_display.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            item = self.todo_list[index]
            new_item = self.entry.get()
            self.todo_list[index] = {"task": new_item, "completed": item["completed"]}
            self.todo_display.delete(index)
            self.todo_display.insert(index, new_item)
            print(f'Edited item:\nBefore: {item["task"]}\nNow: {new_item}')
            self.entry.delete(0, tk.END)

    def complete_item(self):
        selected_task_index = self.todo_display.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            item = self.todo_list[index]
            item["completed"] = not item["completed"]
            self.todo_display.delete(index)
            if item["completed"]:
                self.todo_display.insert(tk.END, f'{item["task"]} (Completed)')
            else:
                self.todo_display.insert(tk.END, item["task"])

    def copy_to_clipboard(self):
        selected_task_index = self.todo_display.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            item = self.todo_list[index]["task"]
            self.root.clipboard_clear()
            self.root.clipboard_append(item)
            self.root.update()
            print(f'Copied item to clipboard: {item}')

    def search(self):
        query = self.search_entry.get()
        self.todo_display.delete(0, tk.END)
        for idx, item in enumerate(self.todo_list):
            if query in item["task"]:
                if item["completed"]:
                    self.todo_display.insert(tk.END, f'{item["task"]} (Completed)')
                else:
                    self.todo_display.insert(tk.END, item["task"])
                print(f'match: {idx}, {item["task"]}')
        if not self.todo_display.get(0, tk.END):
            print('no matches found')

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
