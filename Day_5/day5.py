#!/usr/bin/env python
import os
from enum import Enum

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'sample.txt')

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

def part1(data):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

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

        processed_data = {}
        current_key = None

        for line in data:
            if not line:
                continue  # Skip empty lines

            if line.endswith("map:") or line == "seeds:":
                current_key = line
                processed_data[current_key] = []
            elif current_key:
                try:
                    processed_data[current_key].append([int(x) for x in line.split()])
                except ValueError as e:
                    print(f"Error processing line '{line}': {e}")
            else:
                print(f"Unrecognized line format or missing category header: {line}")

        print(processed_data)

        part1(data)
        part2(data)

if __name__ == "__main__":
    main()