#!/usr/bin/env python
import os
from enum import Enum
import re
from collections import defaultdict

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

def part1(times, distances):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    # Dictionary containing win conditions of holdtime:distance
    wins = defaultdict(dict)

    for i, duration in enumerate(times):
        print(f'Race {i+1} takes {duration} miliseconds')
        for hold in range(1, duration):
            d = (duration - hold) * hold

            if d > distances[i]:
                wins[i][hold] = d

    print(wins)

    margin_of_error = 1

    for race_num, results in wins.items():
        print(f'{race_num}: Num results {len(results)}')
        margin_of_error *= len(results)

    print(f'Margin of error: {margin_of_error}')
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
        times = []
        distances = []

        times_line = f.readline().strip()
        times = [int(x) for x in re.findall(r'\d+', times_line)]

        distances_line = f.readline().strip()
        distances = [int(x) for x in re.findall(r'\d+', distances_line)]
    
        part1(times, distances)

if __name__ == "__main__":
    main()