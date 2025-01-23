#!/usr/bin/env python3
import sys
import os
from pathlib import Path

from taipan_framework.taipan_interpreter.taipan_interpreter import TaipanInterpreter

def main():
    print("Taipan starting...")
    
    if len(sys.argv) != 2:
        print("Usage: taipan <filename.taip>")
        sys.exit(1)
    
    # Convert relative path to absolute and check if file exists
    filename = Path(sys.argv[1]).absolute()
    if not filename.exists():
        print(f"Error: File not found: {filename}")
        print("Make sure your .taip file exists in the current directory!")
        sys.exit(1)
    
    # Read the file content to print it styled
    with open(filename, 'r') as file:
        file_contents = file.read()
    
    # Print the file contents with a nice separator
    print("\nFile contents:")
    print("=" * 20)
    print(file_contents)
    print("=" * 20)
    
    # Initialize the interpreter and execute the file
    interpreter = TaipanInterpreter()
    print("\nCode Output:")
    interpreter.execute(str(filename))

if __name__ == "__main__":
    main()
