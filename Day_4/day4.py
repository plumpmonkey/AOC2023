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


class Scratchcard:
    """Define a class to represent a scratchcard containing the 
    Card Number, Winning Numbers, and the Scratched Numbers"""
    def __init__(self, card_info: str):
        card_parts = card_info.split('|')

        self.id = int(card_parts[0].split()[1].replace(':', ''))
        self.winning_numbers = set(map(int, card_parts[0].split(':')[1].split()))
        self.scratched_numbers = set(map(int, card_parts[1].split()))
        self.number_of_matches = 0
        self.score = 0
        self.number_of_instances = 1

    def __str__(self):
        return (f"\n{Colours.YELLOW.value}ScratchCard ID: {Colours.BLUE.value}{self.id}{Colours.NORMAL.value}\n"
                f"{Colours.YELLOW.value}\tWinning Numbers: {Colours.BLUE.value}{sorted(self.winning_numbers)}{Colours.NORMAL.value}\n"
                f"{Colours.YELLOW.value}\tScratched Numbers: {Colours.BLUE.value}{sorted(self.scratched_numbers)}{Colours.NORMAL.value}\n"
                f"{Colours.YELLOW.value}\tNumber of Matches: {Colours.BLUE.value}{self.number_of_matches}{Colours.NORMAL.value}\n"
                f"{Colours.YELLOW.value}\tScore: {Colours.BLUE.value}{self.score}{Colours.NORMAL.value}\n"
                f"{Colours.YELLOW.value}\tNumber of Instances: {Colours.BLUE.value}{self.number_of_instances}{Colours.NORMAL.value}")


def part1(cards):
    """Input is the list of scratchcards"""
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    total_score = 0

    # loop through each card
    for card_id, card in cards.items():
        # determine how many numbers are matched
        matched_numbers = card.winning_numbers.intersection(card.scratched_numbers)
        
        # Determine the score for the card. The score is doubled for each number matched
        if len(matched_numbers) > 0:
            score = 2 ** (len(matched_numbers) - 1)
            total_score += score
        else:
            score = 0

        # Set the number of matched numbers in the card object
        card.number_of_matches = len(matched_numbers)

        # Set the score in the card object
        card.score = score

        # print(card)
        
    print()
    print(f'{Colours.BOLD.value}{Colours.YELLOW.value}Total Score: {Colours.BLUE.value}{total_score}{Colours.NORMAL.value}')
    return cards


def part2(cards):
    print()
    print(f'{Colours.BOLD.value}Part 2')
    print(f'======{Colours.NORMAL.value}')

    for card_id, card in cards.items():
        # Read the cards.matching_numbers. Add one to the number of instances
        # for each id after this one. Eg, if the card has 3 matching numbers
        # then add one to card 4, 5 and 6

        # print(f'{Colours.YELLOW.value}Card ID: {Colours.BLUE.value}{card.id}{Colours.NORMAL.value}')
        # print(f'{Colours.YELLOW.value}\tNumber of Matches: {Colours.BLUE.value}{card.number_of_matches}{Colours.NORMAL.value}')
        # print(f'{Colours.YELLOW.value}\tNumber of Instances: {Colours.BLUE.value}{card.number_of_instances}{Colours.NORMAL.value}')
        
        # repeat for the number of instances of this card
        for i in range(card.number_of_instances):               
            for i in range(card.number_of_matches):
                # print(f'Adding one to card {card.id + i + 1}    ')
                
                # Ensure we are not going out of range
                if card.id + i + 1 in cards:
                    cards[card.id + i + 1].number_of_instances += 1
        
    # Print the final state of the cards
    # for card_id, card in cards.items():
    #     print(card)

    # Total up the number of instances of all cards
    total_number_of_instances = sum(card.number_of_instances for card in cards.values())
    print()
    print(f'{Colours.BOLD.value}{Colours.YELLOW.value}Total Number of Instances: {Colours.BLUE.value}{total_number_of_instances}{Colours.NORMAL.value}')

    return


def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read().splitlines()

        cards = {int(card.split()[1].replace(':', '')): Scratchcard(card) for card in data}
            
        # Cards is returned as we have now populated the score for each card
        cards = part1(cards)

        part2(cards)

if __name__ == "__main__":
    main()