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


class Scrachcard:
    """Define a class to represent a scratchcard containing the 
    Card Number, Winning Numbers, and the Scratched Numbers"""
    def __init__(self, card_info: str):
        card_parts = card_info.split('|')

        self.id = int(card_parts[0].split()[1].replace(':', ''))
        self.winning_numbers = set(map(int, card_parts[0].split(':')[1].split()))
        self.scratched_numbers = set(map(int, card_parts[1].split()))

    def __str__(self):
        return (f"\n{Colours.YELLOW.value}ScratchCard ID: {Colours.BLUE.value}{self.id}{Colours.NORMAL.value}\n"
                f"{Colours.YELLOW.value}Winning Numbers: {Colours.BLUE.value}{sorted(self.winning_numbers)}{Colours.NORMAL.value}\n"
                f"{Colours.YELLOW.value}Scratched Numbers: {Colours.BLUE.value}{sorted(self.scratched_numbers)}{Colours.NORMAL.value}")


def part1(cards):
    """Input is the list of scratchcards"""
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    total_score = 0

    # loop through each card
    for card in cards:
        # determine how many numbers are matched
        matched_numbers = card.winning_numbers.intersection(card.scratched_numbers)
        
        # Determine the score for the card. The score is doubled for each number matched
        if len(matched_numbers) > 0:
            score = 2 ** (len(matched_numbers) - 1)
            total_score += score
        else:
            score = 0

        print(f'\n{Colours.YELLOW.value}ScratchCard ID: {Colours.BLUE.value}{card.id}{Colours.NORMAL.value} '
              f'{Colours.YELLOW.value}Matched Numbers: {Colours.BLUE.value}{sorted(matched_numbers)}{Colours.NORMAL.value} '
              f'{Colours.YELLOW.value}Number of Matches: {Colours.BLUE.value}{len(matched_numbers)}{Colours.NORMAL.value}'
                f'{Colours.YELLOW.value} Score: {Colours.BLUE.value}{score}{Colours.NORMAL.value}')
        
    print()
    print(f'{Colours.BOLD.value}{Colours.YELLOW.value}Total Score: {Colours.BLUE.value}{total_score}{Colours.NORMAL.value}')
    return total_score


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

        cards = [Scrachcard(card) for card in data]

        for card in cards:
            print(card)

        part1(cards)
        part2(data)

if __name__ == "__main__":
    main()