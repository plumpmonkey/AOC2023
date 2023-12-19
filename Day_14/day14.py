#!/usr/bin/env python
import os
from enum import Enum
import numpy as np
import copy

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

def tilt_platform(platform: np.ndarray) -> np.ndarray:
 
    # Keep track of the last row that is currently being occupied - Default to -1
    last_occupied_row = { col_num: -1 for col_num, _ in enumerate(platform[0]) }
    
    # Iterate over the platform from top to bottom
    for current_row, row in enumerate(platform):
        # Iterate over the columns in the row
        for column_number, character in enumerate(row):
            # Check if we have a round rock
            if character == 'O':            
                # Determine the row where we can next place a rock
                target_row = last_occupied_row[column_number] + 1

                if target_row != current_row:
                    # We need to move this rock
                    platform[target_row, column_number] = 'O'
                    
                    # Clear the current space
                    platform[current_row, column_number] = '.'

                    # Update the last occupied row
                    last_occupied_row[column_number] = target_row

            # If the current space is not empty, update the highest occupied row
            if platform[current_row, column_number] != '.':
                last_occupied_row[column_number] = current_row            

    return platform              

def calculate_loading(platform: np.ndarray) -> int:
    # Determine the number of rows in the platform
    num_rows = len(platform)

    # For each row, count the number of 'O' characters and multiply by the number of rows
    # in the platform - the current row
    loading = sum([np.count_nonzero(row == 'O') * (num_rows - row_number) for row_number, row in enumerate(platform)])

    print(f'Loading: {loading}')

def part1(platform):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    print(f'{Colours.BOLD.value}Initial Platform{Colours.NORMAL.value}')
    print(platform)

    tilt_platform(platform)

    print()
    print(f'{Colours.BOLD.value}Tilted Platform{Colours.NORMAL.value}')
    print(platform)

    calculate_loading(platform)
    return 


def tilt_cycle(platform: np.ndarray) -> np.ndarray:
    # For each cycle we tilt the rocks nort, east, south and west.
    # To do this we can rotate the platform 90 degrees clockwise
    # and perform the tilt again.

    # Loop 4 times
    for _ in range(4):
        # Tilt the platform
        platform = tilt_platform(platform)
        
        # Rotate the platform 90 degrees clockwise
        platform = np.rot90(platform, -1)

    # We are now facing north again
    return platform
        

def part2(platform):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')

    # Define the number of cycles to run for
    max_cycles = 1000000000

    platform_cache = {}
    for i in range(max_cycles):
        platform = tilt_cycle(platform)

        # Convert the np.array to a a tuple so that it is immutable and can be used as a key in a dictionary
        platform_tuple = tuple(map(tuple, platform))

        # Check if we have seen this platform before
        if platform_tuple in platform_cache:
            # We have seen this before. retrieve the index of the last time we saw it
            last_seen = platform_cache[platform_tuple]

            # Calculate the number of cycles between the last time we saw it and now
            cycle_length = i - last_seen

            cycles_after_repeat = max_cycles - i

            remaining_cycles = cycles_after_repeat % cycle_length - 1
            
            print(f'Cycle {i}: {remaining_cycles} cycles after repeat')

            # Tilt the platform the remaining number of cycles
            for _ in range(remaining_cycles):
                platform = tilt_cycle(platform)

            calculate_loading(platform)
            print(f'{Colours.BOLD.value}Final Platform{Colours.NORMAL.value}')
            print(platform)
            return
        else:
            # We have not seen this before, log this in the cache with the current cycle number
            platform_cache[platform_tuple] = i

    print()

    return


def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read()

        # Parse the input data into an np.array
        platform = np.array([list(line) for line in data.splitlines()])

        # Take a deep copy of the platform to use for part 2
        platform2 = copy.deepcopy(platform)

        part1(platform)
        part2(platform2)

if __name__ == "__main__":
    main()