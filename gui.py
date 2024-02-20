from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from main import TodoList


class Table:
    def __init__(self, frame, tl: TodoList) -> None:
        self.todo_list = tl
        navbar = Frame(frame)
        Button(navbar, text="new task", command=self.new_task).grid(row=0, column=0)
        Button(navbar, text="save", command=self.save_tasks).grid(row=0, column=1)
        Button(navbar, text="clear tasks", command=self.clear_tasks).grid(row=0, column=2)
        navbar.pack(fill="x")
        self.table = Frame(master=frame)
        self.table.columnconfigure(0, weight=1)
        self.table.columnconfigure(1, weight=1)
        self.table.columnconfigure(2, weight=1)
        self.table.columnconfigure(3, weight=1)
        self.table.columnconfigure(4, weight=1)
        Label(self.table, text="Index", relief="sunken", borderwidth=1).grid(row=0, column=0, sticky=W+E)
        Label(self.table, text="Task Title", relief="sunken", borderwidth=1).grid(row=0, column=1, sticky=W+E)
        Label(self.table, text="Priority", relief="sunken", borderwidth=1).grid(row=0, column=2, sticky=W+E)
        Label(self.table, text="Done", relief="sunken", borderwidth=1).grid(row=0, column=3, sticky=W+E)
        Label(self.table, text="Delete", relief="sunken", borderwidth=1).grid(row=0, column=4, sticky=W+E)
        self.table.pack(fill="both", expand=True, pady=5)
        self.table_var = {}
        self.load_tasks()

    def add_row(self, title, priority, done, index):
        Label(self.table, text=index, borderwidth=1, relief="sunken", background="white").grid(row=index, column=0,
                                                                                               sticky="wens")
        Entry(self.table, textvariable=title, justify="center").grid(row=index, column=1, sticky="wens")
        Combobox(self.table, textvariable=priority, values=["Low", "Medium", "High"], state="readonly").grid(row=index, column=2,
                                                                                           sticky="wens")
        Checkbutton(self.table, variable=done, relief="sunken", borderwidth=1, onvalue=1, offvalue=0,
                    background="white").grid(row=index, column=3, sticky="wens")
        Button(self.table, text="submit",
               command=lambda: self.delete_task(title.get())).grid(row=index, column=4, sticky="wens")

    def new_task(self):
        _, index = self.table.grid_size()
        title, priority, done = StringVar(), StringVar(value="Medium"), IntVar(value=0)
        self.add_row(title, priority, done, index)
        self.table_var[index] = title, priority, done

    def save_tasks(self):
        self.todo_list.clear_list()
        for title, priority, done in self.table_var.values():
            if not title.get() or not priority.get():
                continue
            self.todo_list.create_task(title.get(), priority.get(), done.get())
        self.load_tasks()

    def load_tasks(self):
        for item in list(self.table.children.values())[5:]:
            item.destroy()

        self.table_var = {}
        for i, task in enumerate(self.todo_list.tasks):
            title, priority, done = task
            self.table_var[i + 1] = StringVar(value=title), StringVar(value=priority), IntVar(value=int(done))

        for index, task in self.table_var.items():
            title, priority, done = task
            self.add_row(title, priority, done, index)

    def delete_task(self, title):
        self.todo_list.delete_task(title)
        self.load_tasks()

    def clear_tasks(self):
        mes_box = messagebox.askyesno("Clear All Tasks", "Are you sure about to clear all tasks?")
        if mes_box:
            self.todo_list.clear_list()
            self.load_tasks()


if __name__ == "__main__":
    todo_list = TodoList()
    root = Tk()
    root.title("Task Management")
    root.geometry('600x400+50+50')
    table = Table(root, todo_list)
    root.mainloop()
