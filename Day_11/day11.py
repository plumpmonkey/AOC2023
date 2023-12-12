#!/usr/bin/env python
import os
from enum import Enum
from helpers import Grid, Point, Colours
from itertools import combinations

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input.txt')

def check_all_dots(string : str) -> bool:
    """ Check if a string is all dots. """
    return all(char == "." for char in string)


def part1(universe: Grid):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    print(universe)
    print()
    # Universe expansion
    # Loop through the rows in the universe and if it contains all empty data
    # "." chars, then insert a new row

    for row_index, row in reversed(list(enumerate(universe.rows_as_str()))):
        if check_all_dots(row):
            universe.insert_empty_row(row_index, ".")
            print(f'{Colours.GREEN.value}Inserted empty row at index {row_index}{Colours.NORMAL.value}')

    # Transpose the universe so we can do the same for columns
    universe.transpose()

    for row_index, row in reversed(list(enumerate(universe.rows_as_str()))):
        if check_all_dots(row):
            universe.insert_empty_row(row_index, ".")
            print(f'{Colours.GREEN.value}Inserted empty column at index {row_index}{Colours.NORMAL.value}')

    # Transpose back
    universe.transpose()

    print(universe.__repr__())
    print(f'{Colours.BOLD.value}Final Universe{Colours.NORMAL.value}')
    print(universe)

    galaxies = []
    # Find all the points in the universe that are "#" chars
    for point in universe.all_points():
        if universe.get_value(point) == "#":
            galaxies.append(point)

    print(f'{Colours.BOLD.value}Galaxies{Colours.NORMAL.value} - {len(galaxies)}')

    # Find all the combinations of galaxies
    galaxy_combinations = list(combinations(galaxies, 2))

    print(f'{Colours.BOLD.value}Galaxy Combinations{Colours.NORMAL.value} - {len(galaxy_combinations)}')

    # Loop through the combinations and sum the manhattan distance between them
    total_distance = 0
    for galaxy_a, galaxy_b in galaxy_combinations:
        total_distance += universe.manhattan_distance(galaxy_a, galaxy_b)

    print(f'{Colours.BOLD.value}Total Distance{Colours.NORMAL.value} - {total_distance}')

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

        universe = Grid(data)

        part1(universe)
        part2(data)

if __name__ == "__main__":
    main()