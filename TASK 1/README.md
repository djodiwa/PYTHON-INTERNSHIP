# PYTHON INTERNSHIP - Task 1: Build a Calculator CLI App

## Overview
As part of my Python internship, I completed Task 1 by developing a command-line interface (CLI) calculator script. This exercise focused on implementing basic arithmetic operations using core Python concepts, including functions, loops, conditionals, and user interaction via input/output. The deliverable is a single Python script, `calculator.py`, located in this directory, which provides an interactive calculator supporting addition, subtraction, multiplication, and division.

This README serves as documentation of the development process, tools utilized, usage instructions, and key learnings, reflecting my approach as a student interning in software development.

## Features
- **Supported Operations**: Addition (+), subtraction (-), multiplication (*), and division (/).
- **Interactive CLI**: Users select operations and input numbers through terminal prompts.
- **Error Handling**: Includes safeguards for division by zero and invalid numeric inputs.
- **Persistent Loop**: Continues execution until the user explicitly chooses to exit.
- **User-Friendly Output**: Clear prompts, formatted results, and graceful handling of invalid selections.

## Tools and Setup
The development environment utilized **Visual Studio Code (VS Code)**, selected for its robust support for Python development, including syntax highlighting, debugging capabilities, and an integrated terminal. No external libraries were required, ensuring portability.

- **Python Version**: 3.x (tested with 3.12).
- **Prerequisites**: Python installed on the system (available from python.org).

## How to Run the Script
1. **Prepare the Environment**:
   - Ensure Python is installed and accessible via the command line.
   - Place `calculator.py` in your working directory.
2. **Launch in VS Code**:
   - Open VS Code and load the directory containing `calculator.py`.
3. **Execute the Script**:
   - Open the integrated terminal (View > Terminal).
   - Run the command: `python calculator.py`.
4. **Interact with the Script**:
   - Select an operation (1-4) and provide two numbers.
   - View the result and continue or exit (option 5).

**Sample Output**:
```
Welcome to ~DIWA Simple CLI PYTHON Calculator!

1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Choose (1-5): 3
First number: 2
Second number: 5
Result: 10.0

1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Choose (1-5): 2
First number: 34
Second number: 456
Result: -422.0

1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Choose (1-5): 

```

If Python is not recognized in the terminal, verify that it is added to the system's PATH environment variable.

## Development Process
Following the task guidelines, I structured the script around modular functions for operations, user input collection, and a controlling loop. The process was iterative, emphasizing simplicity and robustness.

### Step 1: Initial Planning
- Created a new file in VS Code named `calculator.py`.
- Outlined requirements in initial comments, including operations and control flow elements.

### Step 2: Implementing Core Functions
- Defined dedicated functions for each arithmetic operation.
- Incorporated conditional logic within the division function to manage edge cases like division by zero.
- Verified functionality using VS Code's interactive Python REPL for isolated testing.

### Step 3: Building the Main Interface
- Established a `while` loop to maintain interactivity until user exit.
- Integrated `input()` for operation selection and numeric values, with `print()` for menu display and results.
- Employed `try-except` blocks to validate inputs and prevent runtime errors.

### Step 4: Testing and Refinement
- Executed the script repeatedly in the VS Code terminal to simulate user interactions.
- Tested boundary conditions, such as non-numeric inputs and invalid choices.
- Utilized the debugger to inspect code execution and resolve minor issues, such as indentation.

### Step 5: Finalization
- Added introductory and exit messages for enhanced user experience.
- Ensured concise code structure while meeting all functional requirements.

The entire development took approximately one hour, facilitated by VS Code's efficient workflow tools.

## Key Learnings
- **CLI Development Fundamentals**: Gained proficiency in using `input()` and `print()` to create responsive terminal applications.
- **Error Management**: Understood the importance of exception handling for robust user experiences.
- **VS Code Proficiency**: Appreciated features like the integrated terminal and debugging tools for rapid prototyping.
- **Code Organization**: Reinforced the value of modular design with functions to promote maintainability.
- **Challenges Overcome**: Addressed input validation for decimal numbers, enhancing the script's versatility.

This script provided a solid foundation in Python scripting and CLI design, preparing me for more advanced internship tasks.  
