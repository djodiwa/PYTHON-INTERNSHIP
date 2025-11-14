# PYTHON INTERNSHIP - Task 2: Create a To-Do List Application (Console-based)

## Overview
As part of my Python internship, I completed Task 2 by developing a console-based to-do list application. This task focused on implementing a simple manager for tasks using lists for storage, with add, remove, and view functionalities, and persistence via file I/O. The deliverable is a single Python script, `todo.py`, located in this directory, which provides an interactive CLI for managing tasks that survive program restarts.

This README documents the development process, tools utilized, usage instructions, and key learnings, reflecting my approach as a student interning in software development.

## Features
- **Task Storage**: Uses a Python list to hold tasks dynamically.
- **Core Functionalities**: 
  - View: Displays numbered list of all tasks.
  - Add: Prompts for and appends new tasks.
  - Remove: Allows selection and deletion by index.
- **Persistence**: Automatically loads tasks from `tasks.txt` on startup and saves after additions/removals.
- **User-Friendly CLI**: Menu-driven loop with input validation and error handling for invalid choices or indices.
- **Edge Cases**: Handles empty task lists, invalid inputs (e.g., non-numeric removal), and empty task entries.

## Tools and Setup
The development environment utilized **Visual Studio Code (VS Code)** for editing and the integrated **terminal** for running and testing the script. No external libraries were required beyond Python's built-in `os` for file existence checks.

- **Python Version**: 3.x (tested with 3.12).
- **Prerequisites**: Python installed on the system (available from python.org).

## How to Run the Application
1. **Prepare the Environment**:
   - Ensure Python is installed and accessible via the command line.
   - Place `todo.py` in your working directory.
2. **Launch in VS Code**:
   - Open VS Code and load the directory containing `todo.py`.
3. **Execute the Script**:
   - Open the integrated terminal (View > Terminal).
   - Run the command: `python todo.py`.
4. **Interact with the Application**:
   - Select options (1-4) from the menu.
   - For add/remove, follow prompts; changes are saved automatically.
   - Exit with option 4; tasks persist in `tasks.txt`.

**Sample Output**:
```
Welcome to To-Do List App!

Options:
1. View tasks
2. Add task
3. Remove task
4. Exit
Choose (1-4): 2
Enter a new task: Buy groceries
Task added!

Options:
1. View tasks
2. Add task
3. Remove task
4. Exit
Choose (1-4): 1

Your To-Do List:
1. Buy groceries

Options:
...
Choose (1-4): 4
Goodbye!
```

Rerun the script to see persisted tasks. If `tasks.txt` is manually edited/deleted, the app adapts accordingly.

## Development Process
Following the task guidelines, I structured the script with modular functions for task operations and file handling, integrated into a main CLI loop. The process was iterative, emphasizing persistence and simplicity.

### Step 1: Initial Planning
- Created `todo.py` in VS Code via "New File."
- Outlined functions in comments: load/save for persistence, view/add/remove for core logic.

### Step 2: Implementing Data Persistence
- Defined `load_tasks()` to read from `tasks.txt` using `open()` in read mode, stripping newlines.
- Defined `save_tasks()` to write the list back with `open()` in write mode.
- Used `os.path.exists()` to handle first-run scenarios without the file.

### Step 3: Building Core Functions
- `view_tasks()`: Enumerates and prints tasks if list is non-empty.
- `add_task()`: Takes input, appends if non-empty.
- `remove_task()`: Calls view, parses index, pops with bounds/error checking via try-except.

### Step 4: Creating the Main Interface
- Initialized tasks list by loading from file.
- Used a `while True` loop with menu print and input for choice.
- Mapped choices to functions; saved after modifications; broke on exit.

### Step 5: Testing and Refinement
- Ran in VS Code terminal multiple times: Added tasks, exited, reloaded to verify persistence.
- Tested edges: Empty list, invalid index (ValueError), non-numeric input.
- Debugged a minor indexing off-by-one error using print statements.

The entire development took approximately one hour, supported by VS Code's syntax highlighting and terminal integration.

## Key Learnings
- **List Manipulation**: Gained hands-on experience with append/pop for dynamic data structures.
- **File I/O Basics**: Understood reading/writing text files for persistence, including stripping whitespace.
- **CLI Design**: Reinforced menu loops and input validation for robust user interaction.
- **Error Handling**: Applied try-except for graceful failures, improving app reliability.
- **VS Code Efficiency**: Utilized the terminal for quick iterations without leaving the editor.
- **Challenges Overcome**: Ensuring index-based removal was intuitive required clear numbering and bounds checks.

This task enhanced my skills in building persistent, interactive Python applications, bridging toward more complex data management in the internship.
