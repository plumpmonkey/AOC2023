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