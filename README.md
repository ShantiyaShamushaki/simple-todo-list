# TodoList Application Documentation

## Introduction

The TodoList application is a simple command-line tool for managing tasks in a to-do list. It provides functionality to create, list, update, delete tasks, clear the entire to-do list, and search for a specific task.

## `Task` Class

The `Task` class represents an individual task with attributes such as title, priority, and completion status. It is used to create and store tasks in the to-do list.

### Attributes

- `title`: The title or description of the task.
- `priority`: The priority level of the task (default is 'Medium').
- `done`: A boolean flag indicating whether the task is completed (default is False).

### Methods

- `__str__`: Returns a string representation of the task, showing its title.
- `__iter__`: Allows iterating over the task's attributes.

## `TodoList` Class

The `TodoList` class manages the overall to-do list, providing methods for loading, saving, creating, listing, updating, deleting tasks, clearing the list, and searching for tasks.

### Attributes

- `file_name`: The name of the CSV file used to store tasks ('todo.csv' by default).
- `tasks`: A list to store instances of the `Task` class.

### Methods

- `load_tasks`: Loads tasks from the CSV file into the `tasks` list.
- `save_tasks`: Saves tasks from the `tasks` list to the CSV file.
- `create_task(title, priority='Medium', done=False)`: Creates a new task and adds it to the to-do list.
- `list_tasks`: Displays a formatted list of tasks with index, title, priority, and completion status.
- `update_task(title, field, edit)`: Updates a task's priority or completion status.
- `delete_task(title)`: Deletes a task from the to-do list.
- `clear_list`: Clears all tasks from the to-do list.
- `get_task(title)`: Displays detailed information about a specific task.

## Main Function

The `main` function serves as the entry point for the application. It parses command-line arguments and calls the corresponding methods of the `TodoList` class based on the provided commands.

## Usage

The application is executed from the command line with the following syntax:

```bash
python todo_app.py [command] [arguments]
```


## Command
- `create`: Creates a new task. Arguments: title, priority (optional), done (optional).
- `list`: Lists all tasks in the to-do list.
- `update`: Updates a task. Arguments: title, field ('priority' or 'done'), edit.
- `delete`: Deletes a task. Argument: title.
- `clear`: Clears the entire to-do list.   
- `search`: Searches for a task by title. Argument: title.

## Example
```
python main.py create "Buy groceires" High 0
```
This command creates a new task with the title "Buy groceries," high priority, and not marked as done.

# TodoList GUI Documentation

The graphical user interface (GUI) for the TodoList application is designed using the Tkinter library in Python. This GUI provides an interactive way to manage tasks in the to-do list.

## `Table` Class

The `Table` class is responsible for creating and managing the main table display within the GUI. It interacts with the `TodoList` backend to load, create, save, delete, and clear tasks.

### Constructor

The constructor initializes the GUI components, including buttons, labels, and entry fields. It also sets up the initial table structure.

### Methods

- `add_row(title, priority, done, index)`: Adds a new row to the table with entry fields for task title, priority, completion status, and a delete button.
- `new_task()`: Adds a new row to the table when the "new task" button is clicked.
- `save_tasks()`: Saves the tasks displayed in the table to the `TodoList` backend when the "save" button is clicked.
- `load_tasks()`: Loads tasks from the `TodoList` backend and refreshes the table display.
- `delete_task(title)`: Deletes a task from the `TodoList` backend and refreshes the table display.
- `clear_tasks()`: Asks for confirmation and clears all tasks from the `TodoList` backend and table display when the "clear tasks" button is clicked.

## Main Section

The script's main section initializes the `TodoList` backend and creates the Tkinter root window. It then sets up the `Table` class to manage the GUI components and runs the Tkinter main event loop.

### Components

- `todo_list`: An instance of the `TodoList` class to manage tasks.
- `root`: The main Tkinter window.
- `table`: An instance of the `Table` class to handle the table display.

### GUI Layout

- The window title is set to "Task Management."
- The window size is set to 600x400 pixels with an offset of 50 pixels from the top-left corner.

## Running the Application

To run the application, execute the script. The GUI will appear, allowing users to interact with the to-do list, create new tasks, save changes, delete tasks, and clear the entire list.

Feel free to customize and extend the GUI to fit your specific requirements.

```python
if __name__ == "__main__":
    todo_list = TodoList()
    root = Tk()
    root.title("Task Management")
    root.geometry('600x400+50+50')
    table = Table(root, todo_list)
    root.mainloop()
```
## Note
- Tasks are stored in a CSV file (todo.csv) to persist data between application runs.
- Priorities can be 'Low,' 'Medium,' or 'High.'
- Completion status is represented as 0 (not done) or 1 (done) in the CSV file.

Feel free to modify and extend the code to suit your specific needs.