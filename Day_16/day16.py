#!/usr/bin/env python
import os
from enum import Enum
from helpers import Grid, Point, Colours, Vectors, get_enum_name_from_value
from collections import defaultdict
from collections import deque

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input.txt')

class LaserGrid(Grid):

    def __init__(self, grid_array: list) -> None:
        
        # Dictionary of points and direction. Use default dict to return a default value if the key doesn't exist
        self.energised_points = defaultdict(set)
        self.path: list[tuple[Point, tuple[int, int]]] = []

        super().__init__(grid_array)


    def get_valid_neighbours(self, position: Point, direction: tuple[int, int]) -> list[tuple[Point, tuple[int, int]]]:
        """ Return a list of the points that are adjacent to this point if they are valid to move to 
            direction is a vector value (from helpers.py)"""
        # Get the value of the current position
        current_value = self.get_value(position)

        # print(f'{Colours.BOLD.value}Current Position - {Colours.NORMAL.value} {position} - Value `{current_value}`')

        # Check if we can pass through in the current direction
        if (current_value == '.' or (current_value == "|" and direction in [Vectors.N.value, Vectors.S.value]) or 
                                   (current_value == "-" and direction in [Vectors.E.value, Vectors.W.value])):
            
            # print("pass through")
            # if we are pass through, then we just move the one space in the current direction
            new_position = position + Point(direction[0], direction[1])

            if self.validate_point(new_position):
                yield (new_position, direction) 
            else:
                # print(f'Invalid point new point {new_position}')
                return
        
        elif current_value == '|':
            # Vertical mirror. We need to split to two directions (pass through has already been covered)
            # print("Vertical mirror")
            for next_direction in (Vectors.N.value, Vectors.S.value):
                new_position = position + Point(next_direction[0], next_direction[1])

                if self.validate_point(new_position):
                    yield (new_position, next_direction) 
                else:
                    # print(f'Invalid point new point {new_position}')
                    pass
        elif current_value == '-': 
            # Horizontal mirror. We need to split to two directions (pass through has already been covered)
            # print("Horizontal mirror")
            for next_direction in (Vectors.E.value, Vectors.W.value):
                new_position = position + Point(next_direction[0], next_direction[1])

                if self.validate_point(new_position):
                    yield (new_position, next_direction) 
                else:
                    # print(f'Invalid point new point {new_position}')
                    pass
        elif current_value == '/':
            # Forward slash mirror. We need to split to two directions (pass through has already been covered)
            # print("Forward slash mirror")
            if direction == Vectors.E.value:
                next_direction = Vectors.N.value
            elif direction == Vectors.W.value:
                next_direction = Vectors.S.value
            elif direction == Vectors.N.value:
                next_direction = Vectors.E.value
            elif direction == Vectors.S.value:
                next_direction = Vectors.W.value
            else:
                # print(f'Invalid direction {direction} for forward slash mirror and point {position}')   
                return
            
            new_position = position + Point(next_direction[0], next_direction[1])   
            if self.validate_point(new_position):
                yield (new_position, next_direction)
            else:
                # print(f'Invalid point new point {new_position}')
                pass
        elif current_value == '\\':
            # Back slash mirror. We need to split to two directions (pass through has already been covered)
            # print("Back slash mirror")
            if direction == Vectors.E.value:
                next_direction = Vectors.S.value
            elif direction == Vectors.W.value:
                next_direction = Vectors.N.value
            elif direction == Vectors.N.value:
                next_direction = Vectors.W.value
            elif direction == Vectors.S.value:
                next_direction = Vectors.E.value
            else:
                # print(f'Invalid direction {direction} for back slash mirror and point {position}')   
                return
            
            new_position = position + Point(next_direction[0], next_direction[1])   
            if self.validate_point(new_position):
                yield (new_position, next_direction)
            else:
                # print(f'Invalid point new point {new_position}')
                pass
          
    
    # start location is a tuple of the point and the direction. Direction is a vector value (from helpers.py)
    def bfs(self, start_location: tuple[Point, tuple[int, int]]):
        visited = set()
        queue = deque([start_location])

        visited.add(start_location)
        self.energised_points[start_location[0]].add(start_location[1])

        while queue:
            position, direction = queue.popleft()

            # print(f'{Colours.BOLD.value}Queue Entry - {Colours.NORMAL.value} {position} - {get_enum_name_from_value(Vectors, direction)}')

            # Determine neighbours
            for neighbour in self.get_valid_neighbours(position, direction):
                # print(f'{Colours.BOLD.value}Neighbour - {Colours.NORMAL.value} {neighbour[0]} - {get_enum_name_from_value(Vectors, neighbour[1])}')
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

                    # Add the point to the list of energised points
                    self.energised_points[neighbour[0]].add(neighbour[1])

        
        visted_points = {point for point, _ in visited} 
        for y in range(self._height):
            for x in range(self._width):
                if Point(x,y) in visted_points:
                    print(f'{Colours.BOLD.value}#{Colours.NORMAL.value}', end='')
                else:
                    print(f'{Colours.BOLD.value}.{Colours.NORMAL.value}', end='')
            print()


        print(f'Energised points: {len(self.energised_points)}')
            
            


def part1(grid):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    grid.bfs((Point(0, 0), Vectors.E.value))

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

        grid = LaserGrid(data)

        part1(grid)
        part2(data)

if __name__ == "__main__":
    main()