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

def process_data(data):

    print(f'{Colours.BOLD.value}Processing data{Colours.NORMAL.value}')
    # Define a list to store the processed data
    processed_data = []

    # Loop through each game
    for game in data:


        # Split the game data from the round information. One maximum split
        game_number, round_data = game.split(':', 1)

        # Extract the number from the game number. Eg Game 3 = 3
        game_number = game_number.strip()
        game_number = game_number.split(' ', 1)[1]

        print()
        print(f'{Colours.YELLOW.value}Game Number = {game_number}{Colours.NORMAL.value}')
        
        # Initialise the data for this game
        game_data = {
            'Game_Number': game_number,
            'Rounds': []
        }

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

            round_data = {
                'round_num': round_num,
                'red': round_total_red,
                'green': round_total_green,
                'blue': round_total_blue
            }

            game_data['Rounds'].append(round_data)
        
        processed_data.append(game_data)

    return processed_data

def part1(data):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    valid_games = 0

    max_red, max_green, max_blue = 12, 13, 14

    # Loop through each game in the processed data
    for game in data:
        # Loop through each round
        for round in game['Rounds']:
            # Check if any of the colours are over the maximum
            if round['red'] > max_red or round['green'] > max_green or round['blue'] > max_blue:
                # Mark the game as invalid and break out of the loop
                print(f'{Colours.RED.value}Invalid game {game["Game_Number"]} {Colours.NORMAL.value}')
                break
        else:
            # If the loop completes without breaking, then the game is valid
            print(f'{Colours.GREEN.value}Valid game {game["Game_Number"]} {Colours.NORMAL.value}')
            # Increment the valid game count by the game ID
            valid_games += int(game['Game_Number'])

    print(f'{Colours.BOLD.value}\nResult')
    print(f'======{Colours.NORMAL.value}')

    print(f'{Colours.YELLOW.value}Valid games = {valid_games}{Colours.NORMAL.value}')
    return 


def part2(data):
    print("Part 2")

    total_game_power = 0

    # Loop through each game in the processed data
    for game in data:
        print(f'{Colours.BOLD.value}\nGame {game["Game_Number"]} {Colours.NORMAL.value}')
        max_red, max_green, max_blue = 0, 0, 0
    
        # Loop through each round
        for round in game['Rounds']:
            # Check if any of the colours in this round is the highest we have ever seen
            # If it is, then update the max value.
            if round['red'] > max_red:
                max_red = round['red']
            if round['green'] > max_green:
                max_green = round['green']
            if round['blue'] > max_blue:
                max_blue = round['blue']

        # Print out the max values for this game
        print(f'{Colours.YELLOW.value}Max: {Colours.RED.value}{max_red} red{Colours.NORMAL.value}, {Colours.GREEN.value}{max_green} green{Colours.NORMAL.value}, {Colours.BLUE.value}{max_blue} blue{Colours.NORMAL.value}')

        # Calculate the game power (Max values multiplied together)
        game_power = max_red * max_green * max_blue

        print(f'{Colours.YELLOW.value}Game power: {game_power}{Colours.NORMAL.value}')

        total_game_power += game_power

    print(f'{Colours.BOLD.value}\nResult')
    print(f'======{Colours.NORMAL.value}')

    print(f'{Colours.YELLOW.value}Total game power = {total_game_power}{Colours.NORMAL.value}')

    return


def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read().splitlines()

        # Process the data into games and rounds
        processed_data = process_data(data)

        part1(processed_data)
        part2(processed_data)

if __name__ == "__main__":
    main()