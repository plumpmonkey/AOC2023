# AoC2023
Advent of Code 2023 Challenges

| Day    | Title                   | Description                                                     |
|:-------|:------------------------|:----------------------------------------------------------------|
| [Day 1](https://adventofcode.com/2023/day/1)  | Trebuchet?!        | More difficult than traditional Day 1 - Used `regex` to find digits in a string. Part 2 complex in that also used words, but text could overlap. Used `regex` instead of `re` for `overlapped` keyword |
| [Day 2](https://adventofcode.com/2023/day/2)  | Cube Conundrum     | Parsed input data into `Games` and `Rounds` using `split` and `enumerate`. Each round had coloured cubes. Some basic math on the results.  |
| [Day 3](https://adventofcode.com/2023/day/3)  | Gear Ratios     | Map the data into a 2D grid and examine adjacent data. Created `Point` and `Grid` classes to support this.  |
| [Day 4](https://adventofcode.com/2023/day/4)  | Scratchcards     | Created a `Scratchcard` class to store the card number, winning numbers and scratched numbers. Used a `set` to store the winning numbers and scratched numbers, so that we could easily find the intersection of the two sets to find the number of matches.  |
| [Day 5](https://adventofcode.com/2023/day/5)  | If You Give A Seed A Fertilizer     | Data is split into a seed list, and another list of lists containing the maps. For each seed we check if its in the range of the map, if it is we convert it to the new value and repeat until we get to the location map. Part 2 tricky |
| [Day 6](https://adventofcode.com/2023/day/6)  | Wait For It     | Fairly straight forward. Work through a list and calculate times. Could have used quadratic equation, when for an optimised brute force. Still runs < 1 second|
| [Day 7](https://adventofcode.com/2023/day/7) | Camel Cards | Used `Counter` to count the number of cards in a hand. Created a `Hand` class to store the hand and its rank. The `Hand` class has a `__lt__` method that compares Hand type of the hand, followed the rank of the card scores of two hands. |
| [Day 8](https://adventofcode.com/2023/day/8) | Haunted Wasteland | used `itertools.cycle` to create an infinite list of instructions. Used a dict to store the nodes and their left and right nodes. Used a `while` loop to follow the instructions until the `ZZZ` node was found. **Part 2** was not bruteforce-able, so determined that we need the **least common multiplier** of all the loop counts|
| [Day 9](https://adventofcode.com/2023/day/9) | Mirage Maintenance | Used `numpy` to perform a difference in values in a list. Recursive function to keep doing this until we get the right answers|
| [Day 10](https://adventofcode.com/2023/day/10) | Pipe Maze | A horrible day. Needed to extend the `Grid` class to cater for the pipes, and then use a BFS. Part 2 was a lot of guesswork on the code and still not quite sure why it works.  |