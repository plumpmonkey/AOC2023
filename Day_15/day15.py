#!/usr/bin/env python
import os
from enum import Enum

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input.txt')


class Box():

    def __init__(self, num: int):
        self.box_num = num
        self.lenses: list[tuple[str, int]] = []
        self.lens_set = set()
    
    def lens_in_box(self, lens: str) -> bool:
        return lens in self.lens_set

    def update_lens(self, lens: str, focal_length: int):
        # Find the location of the lens with the given label
        # and update the focal length
        loc = self.lens_location(lens)
        self.lenses[loc] = (lens, focal_length)
        

    # Return the location in the list of the lens with the given label
    # Note - must exist, otherwise raises ValueError
    def lens_location(self, lens_to_del: str) -> int:
        for i, (lens, focal_length) in enumerate(self.lenses):
            if lens == lens_to_del:
                return i
        
        raise ValueError(f'No lens with label {lens} found in box {self.box_num}')

    def add_lens(self, lens: str, focal_length: int):
        self.lenses.append((lens, focal_length))
        self.lens_set.add(lens)

    def remove_lens(self, lens: str):
        if self.lens_in_box(lens):
            # Find lens location in the list
            loc = self.lens_location(lens)
            self.lenses.pop(loc)
            self.lens_set.remove(lens)
            
    def focusing_power(self) -> int:
        power = 0

        for i, (lens, focal_length) in enumerate(self.lenses):
            # Power is box_num + 1 * (slot index + 1) * focal_length
            power += (self.box_num + 1) * (i + 1) * int(focal_length)

    
        return power

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


def hash_routine(input: str) -> int:
    hash_val = 0
    # for each character in the input string
    for char in input:
        # Convert the character to its ASCII value
        hash_val += ord(char)
        
        # Multiply the hash value by 17
        hash_val *= 17

        # Set the value to the remainder of dividing itself by 256
        hash_val %= 256

    return hash_val


def part1(inputs: list):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    # Compute hash for each input and sum them
    total = 0
    for input in inputs:
        total += hash_routine(input)

    # Print the total
    print(f'The total is: {total}')

    return 


def part2(inputs: list):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')

    # Create the 256 boxes as a dict with key of the box num
    boxes = {i: Box(i) for i in range(256)}

    for input in inputs:
        # Determine the operation character
        operation = "=" if "=" in input else "-"

        # Split on the operation character
        lens, focal_length = input.split(operation)

        # Compute the hash of the string
        hash_val = hash_routine(lens)

        # Get the box for this hash value
        box = boxes[hash_val]

        # If the operation is to add a lens
        if operation == "=":
            if box.lens_in_box(lens):
                # Label already exists in this box. Update the focal length with the new value
                box.update_lens(lens, focal_length)
            else:
                # Label doesn't exist in this box. Add it to the box to the end
                box.add_lens(lens, focal_length)
        elif operation == "-":
            # Remove the lens from the box
            box.remove_lens(lens)

    # sum the focusing power of all the boxes
    power = 0
    for box in boxes.values():
        power += box.focusing_power()
        
    print(f'The total focusing power is: {power}')
    return


def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read().splitlines()

        # Split the data based on the `,`
        inputs = data[0].split(',')
        part1(inputs)
        part2(inputs)

if __name__ == "__main__":
    main()