#!/usr/bin/env python
import os
from enum import Enum
from helpers import Point, Grid, Colours, Pipes, Vectors
from collections import deque

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'sample2.txt')

def bfs_search(grid: Pipes, start: Point, end: Point) -> list[Point]:

    visited = set()
    queue = deque()
    parent = {} # Dictionary to keep track of the parent of each node for path reconstruction. Store the step count for each node

    visited.add(start)

    # For the queue and parent dictionary, store the point and the number of steps to get to that point
    queue.append((start, 0))
    parent[start] = (None, 0)

    max_steps = 0 
    while queue:
        node, step_count = queue.popleft()

        # print(f'{Colours.YELLOW.value}Visiting node {node} - Step count: {step_count} - Pipe value {grid.get_value(node)} {Colours.NORMAL.value}')

        # If the step count of this node is further than we have been, then update the max_steps
        if step_count > max_steps:
            max_steps = step_count
            furthest_point = node

        # Find the neighbours of this node
        neighbours = grid.valid_neighbour_pipes(node)

        # print(f'{Colours.BLUE.value}\tValid Neighbours: {neighbours}{Colours.NORMAL.value}')

        for neighbour in neighbours:
            # print(f'{Colours.WHITE.value}Checking neighbour {neighbour} - Pipe value {grid.get_value(neighbour)}{Colours.NORMAL.value}')
            if neighbour not in visited:
                # print(f'{Colours.GREEN.value}\tNeighbour {neighbour} not visited{Colours.NORMAL.value}')
                visited.add(neighbour)
                queue.append((neighbour, step_count + 1))
                parent[neighbour] = (node, step_count + 1)
            else:
                # print(f'{Colours.RED.value}\tNeighbour {neighbour} already visited{Colours.NORMAL.value}')
                pass

    return max_steps, furthest_point, visited

def part1(input_grid: Pipes):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    # Find the starting point. Loop through each point in the grid until we
    # find the 'S' character
    start = next(point for point in input_grid.all_points() if input_grid.get_value(point) == 'S')
    print(f'Found starting point at {start}')   
    
    # Perform our BFS search
    max_steps, furthest_point, visited = bfs_search(input_grid, start, None)
    
    print()
    print(f'{Colours.BOLD.value}Part 1 Answer: {max_steps}{Colours.NORMAL.value}')
    print(f'{Colours.BOLD.value}Part 1 Answer: {furthest_point}{Colours.NORMAL.value}')
    
    return start, visited


def part2(input_grid: Pipes, visited: list[Point], start: Point):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')


    # Create a new Pipes map that only contains the visited points, copying across
    # the pipe values from the original map
    
   
    visited_grid = Pipes([[' ' for _ in range(input_grid.width())] for _ in range(input_grid.height())])
    inside_grid = Pipes([[' ' for _ in range(input_grid.width())] for _ in range(input_grid.height())])

    # Loop through all the points in the visited_grid
    for point in visited_grid.all_points():
        if point in visited:
            # Copy the pipe value from the input_grid to the visited_grid
            visited_grid.set_value(point, input_grid.get_value(point))




    # print(visited_grid)

    # Obatin the rows as a list of strings
    rows = visited_grid.rows_as_str()

    inside_count = 0
    rownum, col = 0, 0

    # Loop through each row, and each character in the row
    for row in rows:
        outside = True
        col = 0
        for char in row:
            if char in "-S":
                pass
            elif char in "F7":
                pass
            # If we are outside and we find a "|","L", or "J" then transition to inside
            elif outside and char in "|LJ":
                outside = False
                inside_grid.set_value(Point(col, rownum), char)

            # If we are inside and we find a "|","L", or "J" then transition to outside 
            elif not outside and char in "|LJ":
                outside = True
                inside_grid.set_value(Point(col, rownum), char)

            # If we are inside and its any other character then increment the inside count
            elif not outside:
                inside_count += 1
                inside_grid.set_value(Point(col, rownum), 'I')
            else:
                inside_grid.set_value(Point(col, rownum), 'O')

            col += 1

        rownum += 1

    print(f'{Colours.BOLD.value}Part 2 Answer: {inside_count}{Colours.NORMAL.value}')

    print(inside_grid)

    return


def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read().splitlines()

        input_grid = Pipes(data)
        print(input_grid.__repr__())

        
        start, visited = part1(input_grid)

        part2(input_grid, visited, start)

if __name__ == "__main__":
    main()