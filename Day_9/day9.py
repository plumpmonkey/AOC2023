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

def recursive_diff(sequence: np.array ) -> int:
    """
    Recursively calculate the differences between each element in the sequence and pass this new list
    back into the function until all the elements in the list are the same. Then return the difference

    This difference gets added to the last value in the sequence and returned to the calling function

    We work all the way back to the top of the stack and return the final value
    """
    # Get a list of the differences between each element in the sequence
    diffs = np.diff(sequence)
    
    # if all the diff values are the same then we have reached 
    # the end of the sequence. We can return the difference
    # so that we can add this to the end of the line
    if np.all(diffs == diffs[0]):
        print(f'{Colours.YELLOW.value}Final Differences: {Colours.NORMAL.value}{diffs}')
        value = diffs[0]
    else:
        # If the differences are not all the same then we need to
        # recursively call this function again
        print(f'{Colours.YELLOW.value}Intermediate Differences: {Colours.NORMAL.value}{diffs}')
        
        value = recursive_diff(diffs)

        # Add the value to the diff line
        value += diffs[-1]

    return value
        

def part1(data):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    sum_of_values = 0
    for history in data:
        # Convert the string to a list of integers
        history = list(map(int, history.split(' ')))

        print(f'{Colours.BLUE.value}\nHistory: {Colours.NORMAL.value}{history}')
        final = recursive_diff(np.array(history))

        # Add the final value + the value of the last element in the history to the history
        history.append(final + history[-1])
        
        sum_of_values += history[-1]

        print(f'{Colours.BLUE.value}Final History: {Colours.NORMAL.value}{history}')

        # Print out the final value
        print(f'{Colours.GREEN.value}New value: {Colours.NORMAL.value}{history[-1]}')
        print()

    print(f'{Colours.BOLD.value}Sum of all values: {Colours.NORMAL.value}{sum_of_values}')
    return 


def part2(data):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')

    return


def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read().splitlines()

        part1(data)
        part2(data)

if __name__ == "__main__":
    main()