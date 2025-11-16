import csv
import os
import sys


class Task:
    def __init__(self, title, priority='Medium', done=False):
        self.title = title
        self.priority = priority
        self.done = done

    def __str__(self):
        return f"{self.title}"

    def __iter__(self):
        iterable = [self.title, self.priority, 1 if self.done else 0]
        for item in iterable:
            yield item


class TodoList:
    def __init__(self):
        self.file_name = 'todo.csv'
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                reader = csv.reader(f)
                for title, priority, done in reader:
                    done = True if done == "1" else False
                    task = Task(title, priority, done)
                    self.tasks.append(task)

    def save_tasks(self):
        with open(self.file_name, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.tasks)

    def create_task(self, title, priority='Medium', done=False):
        new_task = Task(title, priority, done)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task \"{new_task}\" created successfully.", end="")

    def list_tasks(self):
        if self.tasks:
            print("Task List:")
            blue_print = "{:<6} {:<15} {:<10} {:<10}"
            print(blue_print.format("Index", "Title", "Priority", "Done"))
            for i, task in enumerate(self.tasks):
                print(blue_print.format(i+1, task.title, task.priority, task.done))
        else:
            print("No tasks found.")

    def update_task(self, title, field, edit):
        for task in self.tasks:
            if task.title == title:
                if field == "priority":
                    task.priority = edit
                elif field == "done":
                    task.done = True if edit == "1" else False
                self.save_tasks()
                print(f"Task \"{task}\" updated successfully.")
                break
        else:
            print("Invalid title.")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task \"{task}\" deleted successfully.")
                break
        else:
            print("Invalid title.")

    def clear_list(self):
        self.tasks = []
        self.save_tasks()
        print("To-do list cleared successfully.")

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                print("{:<15} {:<10} {:<10}".format("Title", "Priority", "Done"))
                print("{:<15} {:<10} {:<10}".format(task.title, task.priority, task.done))
                break


def main():
    todo_list = TodoList()
    command = sys.argv[1]

    if command == "create":
        title = sys.argv[2]
        if len(sys.argv) < 4:
            todo_list.create_task(title)
        elif len(sys.argv) < 5:
            priority = sys.argv[3]
            todo_list.create_task(title, priority)
        else:
            priority = sys.argv[3]
            done = True if sys.argv[4] == "1" else False
            todo_list.create_task(title, priority, done)
    elif command == "list":
        todo_list.list_tasks()
    elif command == "update":
        title = sys.argv[2]
        field = sys.argv[3]
        edit = sys.argv[4]
        todo_list.update_task(title, field, edit)
    elif command == "delete":
        title = sys.argv[2]
        todo_list.delete_task(title)
    elif command == "clear":
        todo_list.clear_list()
    elif command == "search":
        title = sys.argv[2]
        todo_list.get_task(title)
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
