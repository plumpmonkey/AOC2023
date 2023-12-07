#!/usr/bin/env python
import os
from enum import Enum
import re
from collections import defaultdict

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input.txt')

class Colours(Enum):
    """
    Enumeration for terminal colour codes.
    These are used to add colour to printed text in the terminal.
    """
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
    """
    Solves part 1 of the problem, which involves calculating win conditions based on hold times and distances.

    Args:
    times (list): List of times in milliseconds.
    distances (list): List of distances in meters.

    Prints the win conditions for each race and calculates the overall margin of error.
    """
    print(f'{Colours.BOLD.value}Part 1{Colours.NORMAL.value}')
    print('======')

    wins = defaultdict(dict)

    # Loop over each duration in times
    for i, duration in enumerate(times):
        print(f'Race {i+1} takes {duration} milliseconds')
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

def part2(times, distances):
    """
    Solves part 2 of the problem by finding the range of hold times that result in a win.

    Args:
    times (list): List of times in milliseconds.
    distances (list): List of distances in meters.

    Prints the calculated time, distance, start, end, and total wins.
    """
    print(f'{Colours.BOLD.value}Part 2{Colours.NORMAL.value}')
    print('======')

    time = int(''.join(map(str, times)))
    distance = int(''.join(map(str, distances)))

    print(f'Time: {time}')
    print(f'Distance: {distance}')

    # Calculate the start and end points
    for j in range(time):
        if j * (time - j) > distance:
            start = j
            break
    for j in range(time, 0, -1):
        if j * (time - j) > distance:
            end = j
            break

    print(f'Start: {start}')
    print(f'End: {end}')
    print(f'Total Wins {end - start + 1}')

def main():
    """
    Main function to execute the solution for the problem.
    It reads input data, processes it, and executes the problem-specific functions.
    """
    # Determine the current day based on the file name
    current_day = os.path.basename(__file__).split('.')[0]
    print(current_day)

    # Read in the input file
    with open(input_file) as f:
        times = [int(x) for x in re.findall(r'\d+', f.readline().strip())]
        distances = [int(x) for x in re.findall(r'\d+', f.readline().strip())]

    part1(times, distances)
    part2(times, distances)

if __name__ == "__main__":
    main()
