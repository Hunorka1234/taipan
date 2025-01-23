
# Taipan Programming Language

## Overview

**Taipan** is a modular, Python-based programming language designed to be simple, clean, and robust. It focuses on breaking code into small, easy-to-manage blocks, called **tails**. These modules or blocks are imported and used in the main code (the **spine**), allowing for clear organization and efficient code management.

---

## Taipan Structure

### Main Components:

1. **taipan_framework**: 
   - Contains the core interpreter and logic for running Taipan scripts.
   - Key file: `taipan.py` (the entry point for running scripts).

2. **taipan_spine**:
   - The central hub that imports and loads all available modules (called "tails").
   - It dynamically imports modules from the `taipan_tails` directory.

3. **taipan_tails**:
   - Contains individual function modules, which are categorized into directories and files.
   - These "tails" are what provide the functionality of the language (e.g., math operations, input/output, etc.).

4. **taipan_testing**: 
   - A folder for testing files written in Taipan.
   - Used for experimenting and validating the language.

---

## Setup Instructions (for Development or Publishing)

To set up Taipan on your machine or as a developer, follow these steps:

### 1. **Clone or Download the Taipan Repository**

If you're setting this up from a GitHub repository:

```bash
git clone https://github.com/yourusername/taipan.git
cd taipan
```

### 2. **Install Dependencies (if any)**

Taipan is based on Python 3, so ensure Python is installed. You might also need to install dependencies if there are any (this example doesn't have any external dependencies yet).

```bash
pip3 install -r requirements.txt
```

### 3. **Install Taipan as a Python Package (Editable Mode)**

To install Taipan on your system, use the following command from the project root:

```bash
pip3 install -e .
```

This will install the package in **editable mode**, meaning changes you make to the source code will automatically reflect in the installed version.

### 4. **Create a Symlink (Optional)**

To easily run Taipan from anywhere, create a symlink to the `taipan.py` script in `/usr/local/bin`:

```bash
sudo ln -s /path/to/taipan/Language/taipan_framework/taipan.py /usr/local/bin/taipan
```

This allows you to run the `taipan` command from the terminal.

---

## Usage Guide

### 1. **Running a Taipan Script**

To execute a Taipan script, use the following command in the terminal:

```bash
taipan path/to/your/script.taip
```

This will run the Taipan interpreter and execute the code in your script.

---

### 2. **Writing Taipan Code**

Taipan scripts are simple and modular. Here’s an example of a Taipan script using the `math_ops` tail:

#### Example: `math_test.taip`

```python
from taipan_spine.taipanspine import *

a = 10
b = 5

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
```

In this example:
- We use the `add` and `subtract` functions, which are defined in `taipan_tails/modules/math_ops.py`.
- The functions are directly available because they are imported via the spine (`taipan_spine.taipanspine.py`).

### 3. **Creating a New Tail**

To create a new tail, follow these steps:

- **Create a new file** in the `taipan_tails/modules` folder.
- Define your function(s) inside that file.

#### Example: `multiply.py`:

```python
def multiply(x, y):
    return x * y
```

- Your new tail (`multiply.py`) will automatically be loaded by the spine.

### 4. **Modifying the Spine to Load New Tails**

The spine automatically loads new tails from the `taipan_tails/modules` folder. However, if you need to access a function from a specific module in the spine, you can modify the `taipan_spine.py` file.

For example, if you want to manually import a function:

```python
from taipan_tails.modules.multiply import multiply
```

---

## Directory Structure

Here’s a detailed overview of the Taipan directory structure:

```
TAIPAN/
├── Language/
│   ├── setup.py                # Setup file for package installation
│   ├── taipan.egg-info/        # Metadata for the Python package
│   ├── taipan_framework/       # Core interpreter and logic
│   │   ├── taipan.py           # Main entry point to run Taipan code
│   ├── taipan_spine/           # Central hub to load modules
│   │   └── taipanspine.py      # Imports all available functions from tails
│   ├── taipan_tails/           # Directory containing all tail modules
│   │   ├── modules/            # Function modules (e.g., math_ops.py)
│   └── taipan_testing/         # Test scripts
│       └── test.taip           # Example test file
└── requirements.txt            # Any necessary dependencies
```

### Key Files:
- **`taipan.py`**: The main script for running Taipan code.
- **`taipanspine.py`**: The central hub that dynamically imports and manages available modules.
- **`math_ops.py`**: Example tail module with functions like `add`, `subtract`, etc.
- **`test.taip`**: Example test script showing how to use Taipan.

---

## Publishing to GitHub (User Guide)

Once you've set everything up, you can publish this project to GitHub. Here’s what users need to do to get started:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/taipan.git
   cd taipan
   ```

2. **Install Taipan:**
   ```bash
   pip3 install -e .
   ```

3. **Run a Taipan Script:**
   Users can now run any `.taip` script using the `taipan` command:
   ```bash
   taipan path/to/script.taip
   ```

4. **Create and Modify Tails:**
   To add functionality, users can create new tails in the `taipan_tails/modules` directory. Each file in that folder is a module that can be accessed by the `taipan_spine`.

---

## Notes for Future Development

- **Modularization**: Continue expanding the `taipan_tails` directory with more function modules.
- **Error Handling**: Implement robust error handling and debugging support in the interpreter.
- **Performance**: Optimize the module loading mechanism if necessary.
- **User Guide**: Enhance the guide as the language grows with new features.

---