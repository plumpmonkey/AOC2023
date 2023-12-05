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

def part1(seeds, maps, num_maps, map_names):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    for seed in seeds:
        print(f'{Colours.YELLOW.value}Seed:{Colours.NORMAL.value} {seed}')

        for map_num in range(num_maps):
            print(f'\t{Colours.YELLOW.value}Map:{Colours.NORMAL.value} {map_num+1} - {map_names[map_num]}')

            # Index into the maps list to get the current map
            for value in maps[map_num]:
                print(f"\t\t{value} - Range = {value[1]} to {value[1] + value[2]}")
                if value[1] <= seed < value[1] + value[2]:
                    print(f"\t\t\t{Colours.GREEN.value}Value {seed} Found{Colours.NORMAL.value}")
                    break

    return 


def part2(data):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')

    return

def process_data(data):

    seeds = []
    maps = []
    current_map = []
    map_names = []

    for line in data:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        if line.startswith("seeds:"):
            # Extracting seeds data
            seed_data = line.split(":")[1].strip()
            seeds = [int(seed) for seed in seed_data.split()]
        elif line.endswith("map:"):
            # Start of a new map category
            map_names.append(line.split(":")[0].strip())

            if current_map:
                # Save the previous map before starting a new one
                maps.append(current_map)
                current_map = []

        else:
            # Add data to the current map
            current_map.append([int(x) for x in line.split()])

    # Add the last map if it exists
    if current_map:
        maps.append(current_map)

    print(f'{Colours.BOLD.value}Seeds:{Colours.NORMAL.value} {seeds}')
    print(f'{Colours.BOLD.value}Maps:{Colours.NORMAL.value} {maps}')

    # print out how many maps we have
    num_maps = len(maps)

    return seeds, maps, num_maps, map_names


def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read().splitlines()

        seeds, maps, num_maps, map_names = process_data(data)

        part1(seeds, maps, num_maps, map_names) 
        part2(data)

if __name__ == "__main__":
    main()