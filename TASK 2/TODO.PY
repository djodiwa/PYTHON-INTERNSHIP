# todo.py

import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from file into a list."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks(tasks):
    """Save tasks list to file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added!")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    """Remove a task by index."""
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main CLI loop."""
    tasks = load_tasks()
    print("Welcome to To-Do List App!")
    
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Choose (1-4): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()