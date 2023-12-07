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

def part1(seeds, maps, num_maps, map_names):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    seed_result = []

    # Loop through each seed in the input data
    for seed in seeds:
        # print(f'{Colours.YELLOW.value}Seed:{Colours.NORMAL.value} {seed}')

        resource_value = seed

        # Take the value and loop through each map in turn.
        for map_num in range(num_maps):
            # print(f'\t{Colours.YELLOW.value}Map:{Colours.NORMAL.value} {map_num+1} - {map_names[map_num]}')

            # Loop through each entry in the map and check if the value is in the range
            # If it is, change the value. If the number is not in the map, it stays the same

            for value in maps[map_num]:
                # print(f"\t\t{value} - Range = {value[1]} to {value[1] + value[2]}")
                if value[1] <= resource_value < value[1] + value[2]:
                    # print(f"\t\t\t{Colours.GREEN.value}Value {resource_value} Found - Changing to {resource_value + (value[0] - value[1])}{Colours.NORMAL.value}")

                    # Adjust the resource value by the destination range
                    resource_value += (value[0] - value[1])

                    break

        # print(f'\t{Colours.YELLOW.value}Final Resource Value:{Colours.BOLD.value}{Colours.BLUE.value} {resource_value}{Colours.NORMAL.value}')
        seed_result.append(resource_value)


    # Determine the minimum value in seed_result
    min_value = min(seed_result)
    print(f'{Colours.YELLOW.value}Minimum Value:{Colours.BOLD.value}{Colours.BLUE.value} {min_value}{Colours.NORMAL.value}')
    return 

def process_ranges(range_list,maps):

    # print(f'\t\t{Colours.YELLOW.value}Range List:{Colours.NORMAL.value} {range_list}')
    new_ranges = []

    for current_range in range_list:
        # print(f'\t\t{Colours.YELLOW.value}Current Range:{Colours.NORMAL.value} {current_range}')

        start_value = current_range[0]
        end_value =  current_range[1] 
        # print(f'\t\t{Colours.YELLOW.value}Start Value:{Colours.NORMAL.value} {Colours.BOLD.value} {start_value} {Colours.NORMAL.value} - {Colours.YELLOW.value}End Value:{Colours.NORMAL.value}{Colours.BOLD.value} {end_value}{Colours.NORMAL.value} ')

        tmp_ranges = [current_range]

        values_adjusted = False

        while tmp_ranges:
            # print(f'\t\t{Colours.RED.value}tmp Ranges:{Colours.NORMAL.value} {tmp_ranges}')

            tmp_range = tmp_ranges.pop()
            # 
            start_value = tmp_range[0]
            end_value =  tmp_range[1] 

            values_adjusted = False
   
            # print(f'\t\t{Colours.YELLOW.value}Working Value:{Colours.NORMAL.value} {Colours.BOLD.value} {start_value} {Colours.NORMAL.value} - {Colours.YELLOW.value}End Value:{Colours.NORMAL.value}{Colours.BOLD.value} {end_value}{Colours.NORMAL.value} ')
            
            for value in maps:
                
                # Calculate the range boundaries
                range_start = value[1]
                range_end = value[1] + value[2] - 1

                # print(f"\t\t{value} - Map Range = {range_start} to {range_end}")

                # Check all cases
                if start_value < range_start and end_value < range_start:
                    # print(f'\t\t\t{Colours.BLUE.value}Both start_value and end_value are below the range - Skipping{Colours.NORMAL.value}')
                    pass
                elif start_value < range_start and end_value >= range_start and end_value <= range_end:                
                    # Start value is OUTSIDE the range and end value is INSIDE the range
                    # print(f'\t\t\t{Colours.RED.value}Start Outside Range - End Inside Range - Splitting ranges to {(start_value, value[1] - 1)} and {(value[1], end_value)} {Colours.NORMAL.value}')
                    tmp_ranges.append((start_value, value[1] - 1))
                    tmp_ranges.append((value[1], end_value))
                    # print(f'\t\t\t{Colours.YELLOW.value}tmp Ranges:{Colours.NORMAL.value} {tmp_ranges}')
                    values_adjusted = True

                    break

                elif start_value < range_start and end_value > range_end:
                    # print(f'\t\t\t{Colours.RED.value}Start Outside Range - End Outside Range - valid range in middle- Splitting ranges to {(start_value, value[1] - 1)} {(value[1], value[1] + value[2] - 1)} {(value[1] + value[2], end_value)}{Colours.NORMAL.value}')
                    tmp_ranges.append((start_value, value[1] - 1))
                    tmp_ranges.append((value[1], value[1] + value[2] -1))
                    tmp_ranges.append((value[1] + value[2], end_value))
                    # print(f'\t\t\t{Colours.YELLOW.value}Tmp Ranges:{Colours.NORMAL.value} {tmp_ranges}')
                    values_adjusted = True

                    break                

                elif start_value >= range_start and start_value <= range_end and end_value <= range_end:
                    start_value += (value[0] - value[1])
                    end_value += (value[0] - value[1]) 
                    # print(f'\t\t\t{Colours.RED.value}new_ranges {new_ranges} {Colours.NORMAL.value}')
                    # print(f'\t\t\t{Colours.GREEN.value}All Inside Range - Adjusting values to {start_value}-{end_value} {Colours.NORMAL.value}')
                    new_ranges.append((start_value, end_value))
                    values_adjusted = True
                    # print(f'\t\t\t{Colours.YELLOW.value}Finished adjusting - New Ranges:{Colours.NORMAL.value} {new_ranges}')
                    values_adjusted = True
                    break

                elif start_value >= range_start and start_value <= range_end and end_value > range_end:
                    # Start value is INSIDE the range and end value is OUTSIDE the range
                    # print(f'\t\t\t{Colours.RED.value}Start Inside Range - End Outside Range - Splitting Ranges to {(start_value, value[1] + value[2] -1)} {(value[1] + value[2], end_value)} {Colours.NORMAL.value}')
                    tmp_ranges.append((start_value, value[1] + value[2]-1))
                    tmp_ranges.append((value[1] + value[2] , end_value))
                    # print(f'\t\t\t{Colours.YELLOW.value}Tmp Ranges:{Colours.NORMAL.value} {tmp_ranges}')
                    values_adjusted = True
                    break

                    
                elif start_value > range_end and end_value > range_end:
                    # print(f'\t\t\t{Colours.BLUE.value}Both start_value and end_value are above the range - Skipping{Colours.NORMAL.value}')
                    pass                
                elif start_value > range_end and end_value < range_start:
                    print(f'{Colours.RED.value}Both start_value and end_value are outside the range, and end_value is before start_value.{Colours.NORMAL.value}')
                    # This shouldnt happen....
                    pass

                else:
                    print(f'\t\t\t{Colours.RED.value}Something went wrong{Colours.NORMAL.value}')
                    print(f'\t\t\t{Colours.RED.value}Start Value:{Colours.NORMAL.value} {Colours.BOLD.value} {start_value} {Colours.NORMAL.value} - {Colours.YELLOW.value}End Value:{Colours.NORMAL.value}{Colours.BOLD.value} {end_value}{Colours.NORMAL.value} ')
                    print(f'\t\t\t{Colours.RED.value}Map Range:{Colours.NORMAL.value} {value[1]} to {value[1] + value[2] - 1}')
                    print(f'\t\t\t{Colours.RED.value}start < start:{Colours.NORMAL.value} {start_value < value[1]}')
                    print(f'\t\t\t{Colours.RED.value}start > end:{Colours.NORMAL.value} {start_value > (value[1] + value[2])}')
                    print(f'\t\t\t{Colours.RED.value}end < start:{Colours.NORMAL.value} {end_value < value[1]}')
                    print(f'\t\t\t{Colours.RED.value}end > end:{Colours.NORMAL.value} {end_value > (value[1] + value[2])}')

            # Nothing changed, pass through the old range
            if not values_adjusted:
                # print(f'\t\t{Colours.MAGENTA.value}No changes made - passing through old range {start_value},{end_value}{Colours.NORMAL.value}')
                new_ranges.append((start_value, end_value))
                # print(f'\t\t{Colours.MAGENTA.value}new_ranges {new_ranges} {Colours.NORMAL.value}')
                

    # print(f'\t\t{Colours.YELLOW.value}New Ranges:{Colours.NORMAL.value} {new_ranges}')

    return new_ranges


def part2(seeds, maps, num_maps, map_names):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')

    lowest_value = 0

    # Convert the seeds to tuples of ranges
    seed_ranges = [(seeds[i], (seeds[i]+seeds[i+1]) -1) for i in range(0, len(seeds), 2)]
    # print(f'{Colours.YELLOW.value}Seed Ranges:{Colours.NORMAL.value} {seed_ranges}')

    # Loop through each range in turn
    for seed_range in seed_ranges:
        # print(f'{Colours.YELLOW.value}Range:{Colours.NORMAL.value} {seed_range}')

        # Set the current_range to be the seed_range - but have this as a list so we can split the ranges later
        ranges_to_process = [seed_range]
        # print(f'\t{Colours.YELLOW.value}Starting Range:{Colours.NORMAL.value} {ranges_to_process}')

        # start_value = current_range[0]
        # end_value =  current_range[1] 
        # print(f'\t{Colours.YELLOW.value}Start Value:{Colours.NORMAL.value} {Colours.BOLD.value} {start_value} {Colours.NORMAL.value} - {Colours.YELLOW.value}End Value:{Colours.NORMAL.value}{Colours.BOLD.value} {end_value}{Colours.NORMAL.value} ')

        # loop through each map in turn passing in the range or ranges to be processed
        for map_num in range(num_maps): 
            # print(f'\t{Colours.YELLOW.value}Map:{Colours.NORMAL.value} {map_num+1} - {map_names[map_num]} - {Colours.YELLOW.value} {Colours.NORMAL.value}')

            # Process the current range(s) for the current map
            ranges_to_process = process_ranges(ranges_to_process, maps[map_num]) 

        # print(f'\t{Colours.YELLOW.value}Final Range:{Colours.NORMAL.value} {ranges_to_process}')  

        # Look through the list, and find the lowest value of the first element of any tuple
        min_value = min([x[0] for x in ranges_to_process])
        # print(f'\t{Colours.YELLOW.value}Minimum Value:{Colours.BOLD.value}{Colours.BLUE.value} {min_value}{Colours.NORMAL.value}')

        if min_value < lowest_value or lowest_value == 0:
            lowest_value = min_value

    print(f'{Colours.YELLOW.value}Lowest Value:{Colours.BOLD.value}{Colours.BLUE.value} {lowest_value}{Colours.NORMAL.value}')

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

    # print(f'{Colours.BOLD.value}Seeds:{Colours.NORMAL.value} {seeds}')
    # print(f'{Colours.BOLD.value}Maps:{Colours.NORMAL.value} {maps}')

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
        part2(seeds, maps, num_maps, map_names)

if __name__ == "__main__":
    main()