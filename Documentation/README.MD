
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
git clone https://github.com/Hunorka1234/taipan.git
cd taipan
```

### 2. **Install Dependencies (if any)**

Taipan is based on Python 3, so ensure Python is installed. You might also need to install dependencies if there are any, this does it auto;

```
pip3 install -r requirements.txt
```

### 3. **Install Taipan as a Python Package (Editable Mode)**

To install Taipan on your system, use the following command from the project root:

```bash
pip3 install -e .
```

This will install the package in **editable mode**, meaning changes you make to the source code will automatically reflect in the installed version.

This allows you to run the `taipan` command from the terminal, as the installed taipan-language is now a python package. use the flag  --break-system-packages if you dont wish to use a python-venv. 

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
commit by opening a pull request, or message me at: hunoramester@gmail.com
