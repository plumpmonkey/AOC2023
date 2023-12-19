#!/usr/bin/env python
import os
from enum import Enum

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


def hash_routine(input: str) -> int:
    hash_val = 0
    # for each character in the input string
    for char in input:
        # Convert the character to its ASCII value
        hash_val += ord(char)
        
        # Multiply the hash value by 17
        hash_val *= 17

        # Set the value to the remainder of dividing itself by 256
        hash_val %= 256

    return hash_val


def part1(inputs: list):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    # Compute hash for each input and sum them
    total = 0
    for input in inputs:
        total += hash_routine(input)

    # Print the total
    print(f'The total is: {total}')

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

        # Split the data based on the `,`
        inputs = data[0].split(',')
        part1(inputs)
        part2(inputs)

if __name__ == "__main__":
    main()