#!/usr/bin/env python
import os
from enum import Enum
from helpers import Grid, Point, Colours
from itertools import combinations
import copy

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input.txt')

def check_all_dots(string : str) -> bool:
    """ Check if a string is all dots. """
    return all(char == "." for char in string)


def part1(universe: Grid):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    # print(universe)
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
    # print(f'{Colours.BOLD.value}Final Universe{Colours.NORMAL.value}')
    # print(universe)

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


def part2(universe2: Grid):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')


    # Determine the starting galaxy locations
    # Find all the points in the universe that are "#" chars
    galaxies = []
    for point in universe2.all_points():
        if universe2.get_value(point) == "#":
            galaxies.append(point)

    print(f'{Colours.BOLD.value}Galaxies{Colours.NORMAL.value} - {len(galaxies)}')
    print(f'{Colours.BOLD.value}Galaxy locations{Colours.NORMAL.value} - {galaxies}')

    # Find all the combinations of galaxies
    galaxy_combinations = list(combinations(galaxies, 2))

    print(f'{Colours.BOLD.value}Galaxy Combinations{Colours.NORMAL.value} - {len(galaxy_combinations)}')
    print(f'{Colours.BOLD.value}Galaxy Combinations{Colours.NORMAL.value} - {galaxy_combinations}')

    columns_to_expand = []
    rows_to_expand = []

    # find the columns and rows that need to be expanded
    for row_index, row in enumerate(universe2.rows_as_str()):
        if check_all_dots(row):
            rows_to_expand.append(row_index)

    universe2.transpose()

    for row_index, row in enumerate(universe2.rows_as_str()):
        if check_all_dots(row):
            columns_to_expand.append(row_index)

    print(f'{Colours.BOLD.value}Rows to expand{Colours.NORMAL.value} - {rows_to_expand}')
    print(f'{Colours.BOLD.value}Columns to expand{Colours.NORMAL.value} - {columns_to_expand}')

    # for each column to expand, loop through the galaxy combinations and check if the column is between the two galaxies
    # if it is, then add 10 to the 2nd point x value
    point_distance = {}
    for galaxy_a, galaxy_b in galaxy_combinations:
            # Determine manhattan distance between the two galaxies
            point_distance[(galaxy_a, galaxy_b)] = universe2.manhattan_distance(galaxy_a, galaxy_b)

            if galaxy_a.x == 4 and galaxy_a.y == 0 and galaxy_b.x == 9 and galaxy_b.y == 10:
                print(f'{Colours.BOLD.value}Galaxy A{Colours.NORMAL.value} - {galaxy_a}')
                print(f'{Colours.BOLD.value}Galaxy B{Colours.NORMAL.value} - {galaxy_b}')
            
                print(f'{Colours.BOLD.value}Point Distance{Colours.NORMAL.value} - {point_distance[(galaxy_a, galaxy_b)]}')

            for column in columns_to_expand:
                if min(galaxy_a.x, galaxy_b.x) < column < max(galaxy_a.x, galaxy_b.x):
                    point_distance[(galaxy_a, galaxy_b)] += 1000000 - 1
            
            for row in rows_to_expand:
                if min(galaxy_a.y, galaxy_b.y) < row < max(galaxy_a.y, galaxy_b.y):
                    point_distance[(galaxy_a, galaxy_b)] += 1000000 - 1
    

    print(f'{Colours.BOLD.value}Point Distance{Colours.NORMAL.value} - {point_distance}')
    # sum all the points_distance values
    total_distance = sum(point_distance.values())

    print(f'{Colours.YELLOW.value}Total Distance{Colours.NORMAL.value} - {total_distance}')
    return


def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read().splitlines()

        universe = Grid(data)
        universe2 = copy.deepcopy(universe)

        part1(universe)

        part2(universe2)

if __name__ == "__main__":
    main()