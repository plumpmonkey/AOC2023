#!/usr/bin/env python
import os
import regex as re

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input.txt')

def part1(data):
    print("Part 1")

    print(data)

    # Take the input data in a format such as 
    # ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
    # and then for each line take the first digit and the last digit in that order
    # to create a two-digit number. If there is only one number, use that number twice.
    # Then add the two-digit numbers together to get the final answer.
    # For example:
    # 1abc2 => 12
    # pqr3stu8vwx => 38
    # a1b2c3d4e5f => 15
    # treb7uchet => 77
    # final answer = 12 + 38 + 15 + 77 = 142

    total = 0

    # Loop through each line of the input data
    for line in data:
        print(f'\nline = {line}')

        # Use regex to get the first and last digit in the line.
        # We will use (2*line) as the input in case there is only one 
        # digit in the input
        first_digit, *_, last_digit = re.findall(r'\d', 2 * line)

        print(f'first_digit = {first_digit}')
        print(f'last_digit = {last_digit}')

        # Add the first and last digits together so it forms a two digit number. 
        # Add the numbers together as strings, then convert to an int.
        two_digit_number = int(first_digit + last_digit)

        print(f'two_digit_number = {two_digit_number}')

        # Add the two digit number to the total
        total = total + two_digit_number
        
    print(f'total = {total}')

    return 


def part2(data):
    print("Part 2")

    # Like part one, one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
    # For example:
    # two1nine -> 29
    # eightwothree -> 83
    # abcone2threexyz -> 13
    # xtwone3four -> 24
    # 4nineeightseven2 -> 42
    # zoneight234 -> 84
    # 7pqrstsixteen -> 76
    #
    # Add all of these together to get the final answer. which would be 281 in this case

    total = 0

    # Create a dictionary of words and their corresponding digits
    words_to_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for line in data:
        print(f'\ninput line = {line}')

        # Find all the digits (\d) or words (one, two, three, etc) in the line. Use the python library
        # regex instead of re so we can use the overlapped=True option to find all the digits/words.
        digits = re.findall("\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True)

        print(f'digits = {digits}')

        # Convert the words to numbers
        digits = [words_to_digits.get(x, x) for x in digits]

        print(f'digits = {digits}')

        # If there is only one digit in the input, use that digit twice
        if len(digits) == 1:
            digits.append(digits[0])
            
        # Take the first and last digit in the line and add them together
        first_digit, *_, last_digit = digits

        print(f'first_digit = {first_digit}')
        print(f'last_digit = {last_digit}')

        # Add the first and last digits together so it forms a two digit number.
        # Add the numbers together as strings, then convert to an int.
        two_digit_number = int(first_digit + last_digit)

        print(f'two_digit_number = {two_digit_number}')

        # Add the two digit number to the total
        total = total + two_digit_number
        
    print(f'total = {total}')

def main():
    # Work out the current day based on the current file name
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    # Read in the input file to a list
    with open(input_file) as f:
        data = f.read().splitlines()

        #part1(data)
        part2(data)

if __name__ == "__main__":
    main()