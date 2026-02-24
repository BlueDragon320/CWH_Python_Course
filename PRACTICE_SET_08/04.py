'''4. Creating Command Line Utilities
        1. Write a small script count_lines.py that takes a filename as input and prints
        how many lines are in the file.
        Example usage:
        python count_lines.py tasks.txt
        # Output: Number of lines: 4

        2. Write a command-line utility search_word.py that takes two arguments:
            1. A filename
            2. A word to search and prints how many times the word appears in the file.'''
            
import sys

def count_lines(filename):
    with open(filename) as f:
        return len(f.readlines())
    
    
if __name__ == "__main__":
    filename = sys.argpv[1]
    num_lines = count_lines(filename)
    print(f"There are {num_lines} lines in {filename}")
