#!/usr/bin/env python
import os
from enum import Enum
from itertools import cycle
from math import gcd

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

def part1(left_right_instructions,nodes):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    instuction_cycle = cycle(left_right_instructions) # Cycle through the instructions

    current_node = 'AAA' # Start at AAA

    loop_count = 0

    while current_node != 'ZZZ':
        # print(f'{Colours.BOLD.value}Current Node: {current_node}{Colours.NORMAL.value}')
        # Get the next instruction
        instruction = next(instuction_cycle)

        # Get the next node
        current_node = nodes[current_node][0] if instruction == 'L' else nodes[current_node][1]

        loop_count += 1

    print(f'{Colours.YELLOW.value}Loop Count: {loop_count}{Colours.NORMAL.value}')
    return loop_count


def part2(left_right_instructions,nodes):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')

    # Determine all the start nodes. This is any node that has a source node that ends in an 'A'
    start_nodes = [node for node in nodes if node.endswith('A')]

    # We are going to need to understand each loop count for each start node
    loop_counts = []

    for node in start_nodes:
        loop_count = 0
        instuction_cycle = cycle(left_right_instructions)

        while not node.endswith('Z'):
            # Get the next instruction
            instruction = next(instuction_cycle)

            # Get the next node
            node = nodes[node][0] if instruction == 'L' else nodes[node][1]

            loop_count += 1

        loop_counts.append(loop_count)

    print(f'{Colours.YELLOW.value}Loop Counts: {loop_counts}{Colours.NORMAL.value}')

    # Determine the lowest common multiple of all the loop counts
    lcm = loop_counts[0]
    for i in loop_counts[1:]:
        lcm = lcm*i//gcd(lcm, i)

    print(f'{Colours.YELLOW.value}Lowest Common Multiple: {lcm}{Colours.NORMAL.value}')

    return

def parse_map(data):
    """Parse the input map. Is of format
    LLR

    AAA = (BBB, BBB)
    BBB = (AAA, ZZZ)
    ZZZ = (ZZZ, ZZZ)

    where the first line is the left/right instruction.

    Starting at AAA, follow the instructions to the left/right until we reach ZZZ
    """

    left_right_instructions = data[0]

    nodes = {}
    # skip the blank line 
    for line in data[2:]:
        # Create a dict of source nodes, and a tuple of the left/right destination nodes. Ensure the ( and ) and any spaces are removed
        source, dest = line.split(" = ")
        nodes[source] = tuple(dest.replace("(", "").replace(")", "").replace(" ", "").split(","))
        

    print(f'{Colours.BLUE.value}Left/Right Instructions: {left_right_instructions}{Colours.NORMAL.value}')
    print(f'{Colours.BLUE.value}Nodes: {nodes}{Colours.NORMAL.value}')

    return left_right_instructions, nodes


def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read().splitlines()

        left_right_instructions,nodes = parse_map(data)

        # part1(left_right_instructions,nodes)
        part2(left_right_instructions,nodes)

if __name__ == "__main__":
    main()