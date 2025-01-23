Taipan Tail Development Guide
What are Tails?

Tails are the building blocks of Taipan - they're modular components that add specific functionality to the language. Think of them as puzzle pieces that snap together to create the full language capabilities. Each tail lives in its own file under the modules directory.

==Tail Structure==

Every tail follows a simple pattern:
    A main class named 'Taipan' followed by the functionality (like TaipanPrint, TaipanMathOps)
    Static methods that perform specific actions
    An init_module() function that returns an instance of the class
    Clear, focused functionality - one tail does one thing well

Creating New Tails
    Place your new tail in the taipan_tails/modules directory
    Name it descriptively (like print.py, math_ops.py, logicops.py)
    Include the init_module() function
    Use static methods for your functionality
    Keep it simple and focused

Running and Testing Tails
    The spine automatically loads all tails from the modules directory
    No need to manually import individual tails
    Create a test.taip file to try out your new tail
    Run it with the 'taipan' command from any directory

Best Practices
    Keep each tail focused on a single type of operation
    Document your tail's functionality clearly
    Handle errors gracefully within the tail
    Make function names clear and descriptive
    Test thoroughly before adding to the main branch

Using Tails in Taipan Code
    All tails are automatically available through the spine
    Import them with: from taipan_spine.taipanspine import *
    Use them directly in your .taip files
    Mix and match tails to create complex functionality


    EXAMPLE: (math_ops.py)
class TaipanMathOps:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b if b != 0 else "Cannot divide by zero"

def init_module():
    return TaipanMathOps()
