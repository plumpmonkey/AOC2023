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
        # print()
        # print(f'{Colours.BOLD.value}Symbol location:{Colours.NORMAL.value} {symbol_location}')

        # Find the adjacent points for each location
        adjacent_points = symbol_location.neighbours()
        # print(f'{Colours.BOLD.value}Adjacent points:{Colours.NORMAL.value} {adjacent_points}')

        for point in adjacent_points:
            # Check that this point is within the grid
            if engine_schematic.validate_point(point):
                # Get the value of the point
                value = engine_schematic.get_value(point)

                # If the value is a digit, then add it to the list
                if value.isdigit():
                    part_number_locations.append(point)
                    # print(f'{Colours.BOLD.value}Part number location:{Colours.NORMAL.value} {point}')
                
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


    return symbol_locations, part_number_ranges
    

def part2(engine_schematic, symbol_locations, part_number_ranges):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')

    # Loop through the symbol locations and find the symbols that represent the gears '*'
    gear_locations = [point for point in symbol_locations if engine_schematic.get_value(point) == '*']
    print(f'{Colours.BOLD.value}Gears:{Colours.NORMAL.value} {gear_locations}')

    # For each gear, find the adjacent points and see if this exists in the part_number_ranges
    # If it is, log this as range for this gear.
    sum_of_gear_ratios = 0

    for gear_location in gear_locations:
        local_gear_ranges = set()
        local_gears = set()

        print(f'{Colours.YELLOW.value}Gear location:{Colours.NORMAL.value} {gear_location}')
        for point in gear_location.neighbours():
            print(f'{Colours.BLUE.value}Point:{Colours.NORMAL.value} {point}')
            # Check if this point is in a part number range
            # Use only the part_number ranges that match the y coordinate neighbour point
            matching_ranges = [part_number_range for part_number_range in part_number_ranges if part_number_range[0].y == point.y]
            print(f'{Colours.BOLD.value}Matching ranges:{Colours.NORMAL.value} {matching_ranges}')

            # For each matching range tuple, expand out the ((StartX,StartY),(EndX,EndY)) into a list of points in that range.
            matching_points = []
            for matching_range in matching_ranges:
                # Get the start and end points
                start_point = matching_range[0]
                end_point = matching_range[1]

                # Loop through the range and add each point to the list
                for x in range(start_point.x, end_point.x + 1):
                    matching_points.append(Point(x, start_point.y))

            print(f'{Colours.BOLD.value}Matching points:{Colours.NORMAL.value} {matching_points}')

            # Check if the gear neighbour point is in the matching points list
            if point in matching_points:
                # If it is, then add the gear to the set
                local_gears.add(point)
                print(f'{Colours.GREEN.value}Adding local gear :{Colours.NORMAL.value} {point}')

        # expand out the local_gears into a list of ranges and add them to the local_gear_ranges set
        for local_gear in local_gears:
            local_gear_ranges.add(engine_schematic.get_part_number_location_range(local_gear))


        # If there are 2 ranges in the set, and only 2 elements, then work out the gear ration
        if len(local_gear_ranges) == 2:
            # Obtain the part numbers for each range
            part_numbers = []
            for local_gear_range in local_gear_ranges:
                part_numbers.append(engine_schematic.get_full_part_number(local_gear_range))

            print(f'{Colours.RED.value}Part numbers:{Colours.NORMAL.value} {part_numbers}')           

            # Work out the gear ratio
            gear_ratio = part_numbers[0] * part_numbers[1]

            print(f'{Colours.BOLD.value}Gear ratio:{Colours.NORMAL.value} {gear_ratio}')

            # Add this to the sum of gear ratios
            sum_of_gear_ratios += gear_ratio
            
    print()
    print(f'{Colours.BOLD.value}Sum of gear ratios:{Colours.NORMAL.value} {sum_of_gear_ratios}')

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

        # Call Part 1 and save the symbol_locations & part_number_ranges for Part 2
        symbol_locations, part_number_ranges = part1(engine_schematic)
        part2(engine_schematic, symbol_locations, part_number_ranges)

if __name__ == "__main__":
    main()