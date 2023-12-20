#!/usr/bin/env python
import os
from enum import Enum
from helpers import Point, get_enum_name_from_value
import heapq


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

def dijkstra(grid, start_point, end_point, max_steps=3):

    # Store the current state
    queue = []

    total_cost = 0
    current_point = start_point
    direction = Point(0, 0)         # (0,0) for start point as we arent moving yet
    steps_taken = 0                 # Number of steps taken so far without a turn

    # Cost needs to be the first element in the priority queue
    heapq.heappush(queue, (total_cost, current_point, direction, steps_taken))

    visited = set()

    while queue:
        # Get the next item from the queue
        total_cost, current_point, direction, steps_taken = heapq.heappop(queue)

        # print(f'Current point: {current_point}, direction: {direction}, steps taken: {steps_taken}, total cost: {total_cost}')  

        # Check if we are at the end point
        if current_point == end_point:
            return total_cost
        
        # Check if we have visited this point before
        if (current_point, direction, steps_taken) in visited:
            continue

        # Add this point to the visited set
        visited.add((current_point, direction, steps_taken))

        possible_moves = []

        if direction == Point(0,0):
            # We are at the start point so we can move in any direction
            for direction in [Point(-1,0), Point(1,0), Point(0,-1), Point(0,1)]:
                new_point = current_point + direction

                # Validate the new point is within the grid
                if 0 <= new_point.x < len(grid[0])  and 0 <= new_point.y < len(grid) :
                    possible_moves.append((new_point, direction, steps_taken+1))

        else:
            # We are not at the start point so we can either move in the current direction if we are less than 3 steps,
            # or turn left or right
            if steps_taken < max_steps:
                # We can move in the current direction
                new_point = current_point + direction
               
                # Validate the new point is within the grid
                if 0 <= new_point.x < len(grid[0])  and 0 <= new_point.y < len(grid) :
                    possible_moves.append((new_point, direction, steps_taken+1))

            # Turn left or right
            # turn 90 degrees CCW (left)
            new_direction = Point(-direction.y, direction.x)
            new_point = current_point + new_direction

           # Validate the new point is within the grid
            if 0 <= new_point.x < len(grid[0]) and 0 <= new_point.y < len(grid) :
                possible_moves.append((new_point, new_direction, 1))
            
            # turn 90 degrees CW (right)
            new_direction = Point(direction.y, -direction.x)
            new_point = current_point + new_direction
            
            # Validate the new point is within the grid
            if 0 <= new_point.x < len(grid[0])  and 0 <= new_point.y < len(grid) :
                possible_moves.append((new_point, new_direction, 1))

        # print(f'\tPossible moves: {possible_moves}')

        for neighbour, direction, next_step in possible_moves:
            new_cost = total_cost + grid[neighbour.y][neighbour.x]

            heapq.heappush(queue, (new_cost, neighbour, direction, next_step))
                
    return total_cost

def part1(grid):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    start_point = Point(0,0)
    end_point = Point(len(grid[0])-1, len(grid)-1)

    distances = dijkstra(grid, start_point, end_point)

    print(f'Distance to end point: {distances}')
    return 


def part2(grid):
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

        grid = [list(map(int, line)) for line in data]

        part1(grid)
        part2(grid)

if __name__ == "__main__":
    main()