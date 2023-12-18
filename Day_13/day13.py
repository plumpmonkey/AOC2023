#!/usr/bin/env python
import os
from enum import Enum
import numpy as np

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input.txt')

# Define the colours used for text printing
class Colours(Enum):
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    NORMAL = "\033[0m"

def part1(patterns: list[np.ndarray]):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    final_val = 0
    for pattern in patterns:
        print()
        print(f'{Colours.BOLD.value}Pattern:{Colours.NORMAL.value}')
        print(pattern)
        print(f'{Colours.BLUE.value}Searching Rows:{Colours.NORMAL.value}')
        row_num = find_symmetry(pattern, axis=0)
        
        final_val += row_num * 100

        # Transpose the pattern and find the symmetry line in the columns
        print(f'{Colours.BLUE.value}Searching Columns:{Colours.NORMAL.value}')
        print(f'{Colours.BOLD.value}Transposed Pattern:{Colours.NORMAL.value}')
        print(pattern.T)
        col_num = find_symmetry(pattern.T, axis=1)

        final_val += col_num

        print(f'{Colours.YELLOW.value}Symmetry line is at row {row_num} and column {col_num}{Colours.NORMAL.value}')

    print(f'{Colours.GREEN.value}Final value: {final_val}{Colours.NORMAL.value}')
    return 


def part2(patterns: list[np.ndarray]):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')

    final_val = 0
    for pattern in patterns:
        print()
        print(f'{Colours.BOLD.value}Pattern:{Colours.NORMAL.value}')
        print(pattern)
        print(f'{Colours.BLUE.value}Searching Rows:{Colours.NORMAL.value}')
        row_num = find_symmetry(pattern, axis=0, num_differences=1)
        
        final_val += row_num * 100

        # Transpose the pattern and find the symmetry line in the columns
        print(f'{Colours.BLUE.value}Searching Columns:{Colours.NORMAL.value}')
        print(f'{Colours.BOLD.value}Transposed Pattern:{Colours.NORMAL.value}')
        print(pattern.T)
        col_num = find_symmetry(pattern.T, axis=1, num_differences=1)

        final_val += col_num

        print(f'{Colours.YELLOW.value}Symmetry line is at row {row_num} and column {col_num}{Colours.NORMAL.value}')

    print(f'{Colours.GREEN.value}Final value: {final_val}{Colours.NORMAL.value}')

    return

def parse_pattern(data) -> list[np.ndarray]:
    # Split the data into blocks based on a blank line
    blocks = data.split('\n\n')

    # For each block read in the data and convert # to 1 and . to 0
    # and return as a numpy array
    patterns = []

    for block in blocks:
        patterns.append(np.array([list(line) for line in block.splitlines()]))

    return patterns

def find_symmetry(pattern: np.ndarray, axis: int = 0, num_differences: int = 0) -> int:
    # Find the line of symmetry for the pattern and return the number
    # rows before the symmetry line.

    if axis == 0:
        debug_text = 'row'
    else:
        debug_text = 'column'

    # Loop through each row and compare to the next row
    for row_number in range(len(pattern) - 1):
        print(f'\t{row_number} - {pattern[row_number]}')
        print(f'\t{row_number+ 1} - {pattern[row_number + 1]}')

        diffs = np.sum(pattern[row_number] != pattern[row_number + 1])
        if num_differences == 0:
            print(f'{Colours.BOLD.value}comparing {debug_text} {row_number} to {row_number + 1}{Colours.NORMAL.value}')
        else: 
            print(f'{Colours.BOLD.value}comparing {debug_text} {row_number} to {row_number + 1} - {diffs} differences{Colours.NORMAL.value}')

        if diffs <= num_differences:
            print(f'{Colours.GREEN.value}Found potential symmetry at {debug_text} {row_number}{Colours.NORMAL.value}')
            
            # Validate the remaining rows are also symmetrical
            rows_after = len(pattern) - (row_number + 2)
            print(f'{Colours.BOLD.value}Number of {debug_text} remaining after symmetry line: {len(pattern)} - {row_number + 2} = {rows_after}{Colours.NORMAL.value}')

            is_symmetrical = True
            for i in range(rows_after):
                if row_number - i == 0:
                    # We have run out of rows in the first half, or the symmetry line is the first row
                    break
            
                print(f'\t{row_number - 1 - i} - {pattern[row_number - 1 - i]}')
                print(f'\t{row_number + 2 + i} - {pattern[row_number + 2 + i]}')
                print()
            
                diffs += np.sum(pattern[row_number - 1 - i] != pattern[row_number + 2 + i])
                if diffs > num_differences:
                    print(f'{Colours.RED.value}Pattern is not symmetrical{Colours.NORMAL.value}')
                    is_symmetrical = False
                    break

            # Check we are symmetrical and that the number of differences is correct.
            if is_symmetrical and diffs == num_differences:
                print(f'{Colours.GREEN.value}Pattern is symmetrical at {debug_text} {row_number} {Colours.NORMAL.value}')
                return row_number + 1
    
    print(f'{Colours.RED.value}Pattern is not symmetrical for {debug_text}s {Colours.NORMAL.value}')
    return 0

def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read()

        patterns = parse_pattern(data)

        # part1(patterns)
        part2(patterns)

if __name__ == "__main__":
    main()