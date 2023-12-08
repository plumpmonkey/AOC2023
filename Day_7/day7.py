#!/usr/bin/env python
import os
from enum import Enum
from collections import Counter

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

class Hand:
    # Define a dict for the card score
    card_scores = { "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "T" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14 }

    # Define a dict for the hand type - assign a rank integer 
    # to each hand type so we can compare later
    hand_type_dict = { "FiveOfKind" : 7,
                  "FourOfKind" : 6,
                  "FullHouse" : 5,
                  "ThreeOfKind" : 4,
                  "TwoPair" : 3,
                  "Pair" : 2,
                  "HighCard" : 1 }
    
    def __init__(self, cards: str, bid: int) -> None:
        # Initialise the hand
        self.cards = cards
        self.bid = bid
        self.hand_type= self.get_hand_type()  
    
    def get_hand_type_name(self, hand_type_value: int) -> str:
        reverse_hand_type = {value: key for key, value in Hand.hand_type_dict.items()}
        return reverse_hand_type.get(hand_type_value, "Unknown Hand Type")

    def get_hand_type(self) -> int:

        # This returns a  list of tuples with the key (card) and the count
        counts = Counter(self.cards).most_common()

        # To understand the hand type, we need to know what the count
        # of the most common card was, and also the count of the second
        # most common card
        # 
        # EG, if the most common card was 3 and the second most common
        # was 2, then we have a full house
        #
        # If the most common card was 2 and the second most common is also
        # 2, then we have a two pair.
        #

        # Get the count of the most common card, and its type
        best_card, best_card_count = counts[0]

        # If this is 5, then we have a five of a kind and we are done,
        # same for 4 of a kind
        if best_card_count == 5:
            return self.hand_type_dict["FiveOfKind"]
        elif best_card_count == 4:
            return self.hand_type_dict["FourOfKind"]

        # If we get here, then we have a three of a kind, full house, two pair
        # pair or high card
        # For these we need to know the count of the second most common card
        second_best_card, second_best_card_count = counts[1]

        # If the best card is 3 and second best is 2, then we have a full house
        if best_card_count == 3 and second_best_card_count == 2:
            return self.hand_type_dict["FullHouse"]
        elif best_card_count == 3 and second_best_card_count == 1:
            return self.hand_type_dict["ThreeOfKind"]
        elif best_card_count == 2 and second_best_card_count == 2:
            return self.hand_type_dict["TwoPair"]
        elif best_card_count == 2 and second_best_card_count == 1:
            return self.hand_type_dict["Pair"]
        elif best_card_count == 1 and second_best_card_count == 1:
            return self.hand_type_dict["HighCard"]
        else:
            print(f'Error: Unable to determine hand type for {self.cards}')       

        
        return 


    def __lt__(self, other: 'Hand'):
        """ Define our own less than operator so we can compare hands
        based on the card strength"""
   
        # If the hand types are different, then we can just compare the hand types
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type

        # If we get here, then the hand types are the same, so we need to compare
        # the cards
        # We need to compare the cards in order, starting with the first card in the hand
        for this_card, other_card in zip(self.cards, other.cards):
            if this_card == other_card:
                continue
            
            return Hand.card_scores[this_card] < Hand.card_scores[other_card]
        
        assert False, "We should not get here"

    def __str__(self) -> str:
        name = self.get_hand_type_name(self.hand_type).ljust(12)
        return (f'{Colours.BOLD.value}Cards: {Colours.NORMAL.value}{self.cards} - '
                f'{Colours.BOLD.value}Hand Type: {Colours.NORMAL.value} {self.hand_type} / {name} - '
                f'{Colours.BOLD.value}Bid: {Colours.NORMAL.value}{self.bid}')



def part1(hands: list[Hand]):
    print()
    print(f'{Colours.BOLD.value}Part 1')
    print(f'======{Colours.NORMAL.value}')

    # Hands is already sorted by hand type and then card score ranging from lowest to highest
    # rank
    # Determine the total winndons by adding the bid for each hand * its rank
    total_winnings = 0

    for index, hand in enumerate(hands):
        total_winnings += hand.bid * (index + 1)

    print(f'{Colours.YELLOW.value}Total Winnings: {Colours.NORMAL.value}{total_winnings}')
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

        hands = []
        # Input data is in the format of:
        # 32T3K 765
        # The first 5 characters are the cards and the last number is the bid
        for line in data:
            cards, bid = line.split(' ')
            
            # Create a hand object
            hand = Hand(cards, int(bid))

            # Add the hand to the list
            hands.append(hand)

        # Sort the hands by hand type
        hands = sorted(hands)

        print(f'{Colours.YELLOW.value}Hands sorted by hand type and then card scores{Colours.NORMAL.value}')
        for hand in hands:
            print(hand)

        part1(hands)
        part2(data)

if __name__ == "__main__":
    main()