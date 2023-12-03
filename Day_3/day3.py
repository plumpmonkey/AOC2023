#!/usr/bin/env python
import os
from helpers import Point, Grid, Colours


dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input.txt')


class Schematic(Grid):
    
    def __init__(self, grid_array: list) -> None:
        super().__init__(grid_array)
        

    def get_symbol_locations(self) -> list[Point]:
        """ Return a list of the locations of all the symbols in the grid. """
        symbol_locations = [point for point in self.all_points() if self._is_a_symbol(point)]
        return symbol_locations
    
    def get_part_number_location_range(self, point: Point) -> tuple[Point, Point]:
        """ With an input point, find the start and end of the part number and return this as a tuple of Points"""
        
        # Obtain the row that this point is on
        row = self._grid_array[point.y]

        # Find the start of the part number
        start = point.x

        while start > 0:
            if row[start-1].isdigit():
                start -= 1
            else:
                break

        # Find the end of the part number
        end = point.x

        while end < len(row) - 1:
            if row[end+1].isdigit():
                end += 1
            else:
                break

        # Return the start and end points
        return Point(start, point.y), Point(end, point.y)


    def get_full_part_number(self, range: tuple[Point,Point] ) -> int:
        """ Given a start and end point, return the full part number."""

        startx, y = range[0].x, range[0].y
        endx = range[1].x + 1

        # Obtain the row that this point is on
        row = self._grid_array[y]

        return int(row[startx:endx])


    def _is_a_symbol(self, point: Point) -> bool:
        """ Check if a point is a symbol. """
        # Get the value of the point
        value = self.get_value(point)

        # if the value is a digit or a `.`, then it is not a symbol.
        if value.isdigit() or value == '.': 
            return False
        else:
            return True   


def part1(engine_schematic: Schematic):
    """ Part 1 - Need to find the numbers adjacent to any symbol and sum them."""
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    part_number_locations = []

    symbol_locations = engine_schematic.get_symbol_locations()

    print(f'{Colours.BOLD.value}Symbols locations:{Colours.NORMAL.value} {symbol_locations}')

    for symbol_location in symbol_locations:
        print()
        print(f'{Colours.BOLD.value}Symbol location:{Colours.NORMAL.value} {symbol_location}')

        # Find the adjacent points for each location
        adjacent_points = symbol_location.neighbours()
        print(f'{Colours.BOLD.value}Adjacent points:{Colours.NORMAL.value} {adjacent_points}')

        for point in adjacent_points:
            # Check that this point is within the grid
            if engine_schematic.validate_point(point):
                # Get the value of the point
                value = engine_schematic.get_value(point)

                # If the value is a digit, then add it to the list
                if value.isdigit():
                    part_number_locations.append(point)
                    print(f'{Colours.BOLD.value}Part number location:{Colours.NORMAL.value} {point}')
                
    # print()
    # print(f'{Colours.BOLD.value}All part number locations:{Colours.NORMAL.value} {part_number_locations}')

    # We have now found all the part number locations. We need to see find out the
    # range of the part numbers and ensure they are unique. For example
    #
    # .*..
    # .10.
    # 
    # this would currently show us two part numbers, but they are for the same range.
    part_number_ranges = set()
    
    # Loop through each part number location
    for part_number_location in part_number_locations:
        # Get the range of the part number
        part_number_ranges.add(engine_schematic.get_part_number_location_range(part_number_location))

    # print()
    # print(f'{Colours.BOLD.value}Part number ranges:{Colours.NORMAL.value} {part_number_ranges}')

    # For each range, grab the full part number
    part_numbers = []

    for part_number_range in part_number_ranges:
        part_numbers.append(engine_schematic.get_full_part_number(part_number_range))

    # print()
    # print(f'{Colours.BOLD.value}Part numbers:{Colours.NORMAL.value} {sorted(part_numbers)}')
    
    # Sum the part numbers
    print()
    print(len(part_numbers))
    part_numbers_sum = sum(part_numbers)
    print()
    print(f'{Colours.BOLD.value}Part numbers sum:{Colours.NORMAL.value} {part_numbers_sum}')


    return 


def part2(data):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')

    return


def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(f'{Colours.BOLD.value}{currentDay}\n{Colours.NORMAL.value}')

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read().splitlines()

        # Load the data into a grid
        engine_schematic = Schematic(data)
        print(repr(engine_schematic))
        print(engine_schematic) 

        part1(engine_schematic)
        part2(engine_schematic)

if __name__ == "__main__":
    main()