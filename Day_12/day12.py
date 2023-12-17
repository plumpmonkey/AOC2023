#!/usr/bin/env python
import os
from enum import Enum
import functools

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

def part1(data):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    arrangements = 0

    # For each input line, split this into a springs string and a list of groups as integers
    for line in data:
        springs, groups_str = line.split(' ')

        groups = list(map(int, groups_str.split(',')))
        
        print(f'{Colours.BLUE.value}{springs} {groups}{Colours.NORMAL.value}')
        # Make groups a tuple so that it can be used as a key in cache (needs to be immutable, lists are not)
        arrangements += calculate_arrangements(springs, tuple(groups))

    print(f'{Colours.GREEN.value}Total arrangements: {arrangements}{Colours.NORMAL.value}')

    return 


def part2(data):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')


    arrangements = 0

    # For each input line, split this into a springs string and a list of groups as integers
    for line in data:
        springs, groups_str = line.split(' ')

        groups = list(map(int, groups_str.split(',')))

        # Unfold the springs and groups    
        unfolded_springs = "?".join(5 * [springs])
        unfolded_groups = 5 * groups

        print(f'{Colours.BLUE.value}{unfolded_springs} {unfolded_groups}{Colours.NORMAL.value}')
        # Make groups a tuple so that it can be used as a key in cache (needs to be immutable, lists are not)
        arrangements += calculate_arrangements(unfolded_springs, tuple(unfolded_groups))

    print(f'{Colours.GREEN.value}Total arrangements: {arrangements}{Colours.NORMAL.value}')

    return

@functools.cache
def calculate_arrangements(springs, groups):

    # print(f'Entering calculate_arrangements with springs: {springs} and groups: {groups}')
    
    def hash():
        # If the first character is a  hash, then the first n chars must be
        # a group of n damaged springs
        # print('Hash')
        char_group = springs[:next_group]

        # Replace any damaged springs with hashes
        char_group = char_group.replace('?', '#')

        # Check to see if the group is invalid
        if char_group != '#' * next_group:
            # If the group is invalid, then we have an invalid arrangement
            # print(f'Invalid group: {char_group}')
            return 0
        
        # If the remaining part of the record is the final group, then there
        # is only one valid arrangement
        if len(springs) == next_group:
            if (len(groups) == 1):
                # print('Final group')
                return 1
            else:
                # There are more groups left, so this is not a valid arrangement
                # print('Final structure but more groups left')
                return 0
            
        # Determine the next group could be a separator character
        if springs[next_group] in ['.', '?']:
            return calculate_arrangements(springs[next_group+1:], groups[1:])
            
        # If the next character is not a separator, then this is not a valid arrangement
        return 0
    
    def period():
        # Skip over the period looking for the next hash
        # print('Period')
        return calculate_arrangements(springs[1:], groups)

    # Check to see if there are any groups left
    if not groups:
        if "#" not in springs:
            # If there are no groups left and no damaged springs left, then we have a valid arrangement
            # print('No groups left and no springs left')
            return 1    
        else:
            # There are damaged springs left, so this is not a valid arrangement
            # print('No groups left but springs left')
            return 0

    if not springs:
        # There are groups left but no springs left, so this is not a valid arrangement
        # print('No springs left but groups left')
        return 0
    
    # Look at the next element in the springs string groups
    next_spring_char = springs[0]
    # print(f'Next spring char: {next_spring_char}')

    next_group = groups[0]
    # print(f'Next group: {next_group}')


    if next_spring_char == '#':
        # If the next spring char is a hash, then we need to process the hash
        # print('Hash')
        out = hash()

    elif next_spring_char == '.':
        # If the next spring char is a period, then we need to process the period
        # print('Period')
        out = period()
    
    elif next_spring_char == '?':
        # If the next spring char is a question mark, then we it could be either char and 
        # we need to process the hash and the period
        # print('Question mark')
        out = hash() + period()

    else:
        # Here be dragons
        raise ValueError('Invalid spring char')

    # print(f'{Colours.YELLOW.value}{springs} {groups} -> Returning {out}{Colours.NORMAL.value}')
    return out
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

    