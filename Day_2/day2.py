#!/usr/bin/env python
import os
from enum import Enum

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

# map the cube colours to a text colour
cube_colours = {
    'red': Colours.RED.value,
    'green': Colours.GREEN.value,
    'blue': Colours.BLUE.value,
}

def part1(data):
    print("Part 1")

    valid_games = 0

    max_red, max_green, max_blue = 12, 13, 14

    for game in data:
        # Initialise the counts of cubes for this game
        game_total_red, game_total_green, game_total_blue = 0, 0, 0

        # Initialise valid game flag
        valid_game = True

        # Split the game data from the round information. One maximum split
        game_number, round_data = game.split(':', 1)

        # Extract the number from the game number. Eg Game 3 = 3
        game_number = game_number.strip()
        game_number = game_number.split(' ', 1)[1]

        print()
        print(f'{Colours.YELLOW.value}Game Number = {game_number}{Colours.NORMAL.value}')

        # Split the data into a list of rounds 
        rounds = round_data.split(';')

        # Enumerate through the list of rounds, starting at 1
        for round_num, round_data in enumerate(rounds, start=1):

            # Initialise the counts of cubes for this ROUND
            round_total_red, round_total_green, round_total_blue = 0, 0, 0

            # Split the round data into a list of cubes
            cubes = round_data.split(',')

            # Enumerate through the list of cubes, starting at 1
            for cube_num, cube in enumerate(cubes, start=1):
                # Cube is a number, followed by the colour of the cube. EG "6 red"
                # Split the cube into the number and colour
                cube = cube.strip()
                cube_num, cube = cube.split(' ', 1)

                # Add the cube count to the total
                if cube == 'red':
                    round_total_red += int(cube_num)
                elif cube == 'green':
                    round_total_green += int(cube_num)
                elif cube == 'blue':
                    round_total_blue += int(cube_num)

            # print out the round_data in the format "round_num: red, green, blue", but using the correct colours
            print(f'{Colours.YELLOW.value}Round:{round_num}: {cube_colours["red"]}{round_total_red} red{Colours.NORMAL.value}, {cube_colours["green"]}{round_total_green} green{Colours.NORMAL.value}, {cube_colours["blue"]}{round_total_blue} blue{Colours.NORMAL.value}')

            # If the round total for any colour is greater than the maximum, flag this as an invalid game
            if round_total_red > max_red or round_total_green > max_green or round_total_blue > max_blue:
                print(f'{Colours.RED.value}Invalid game{Colours.NORMAL.value}')
                valid_game = False
                break

        if valid_game:
            # Add the game_id to the list of valid games
            print(f'{Colours.GREEN.value}Valid game {game_number} {Colours.NORMAL.value}')
            valid_games += int(game_number)

    print(f'{Colours.YELLOW.value}\nValid games = {valid_games}{Colours.NORMAL.value}')
    return 


def part2(data):
    print("Part 2")

    return


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