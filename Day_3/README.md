# [Day 3: Gear Ratios](https://adventofcode.com/2023/day/3)

## Solution Notes

I feel like I totally over engineered this. I built the following classes to solve this problem and extended them so they could be used in future problems (such as printing the grid columns, which is not required for this problem). Created a `helpers.py` file to store these classes and functions.

 - Defined a Point class (used in AOC2022 Day 17 and Day 22). 
   - Allows you to find the point neighbours, and optionally include diagonals.
   - Add a vector to the point and return a new point. (Used in AOC2022 - not required for this problem)
 - Defined a Grid class which is a grid of Points.
   - Get and Set values in the grid
   - Validate if a Point is within the grid (boundary checking)
   - Return a given column of the grid (not required for this problem, but has been used in previous years, so Im prepping!)

Also defined in the main code a class called `Schematic`, which is of type Grid. This was extending the Grid class to:

  - Find all symbol locations in the grid
  - Find all part number ranges in the grid (Start and end points)
  - Find the value of a part number for a given range 
  
Part 1 implementation:

 - Find all symbol locations
 - Find the adjacent points in the grid for each symbol location - with boundary checking
 - If the adjacent point is a digit, store the location as the part number
 - For all part numbers, determine the range of the part number (start and end points) and store these in a set so that we dont duplicate the parts
 - Sum the values
  
### Part 2

For part 2 we could reuse the data we had found already with the symbol locations and ranges.

 - Find the **gear** symbol `*` locations
 - Find the adjacent points in the grid for each gear location - with boundary checking
 - Determine if the adjacent points are are in known number ranges.
 - If its in a range thats adacent to the gear, store the part number
 - If there are 2 part numbers for a given gear, calculate the gear ratio
 - 
## Part One - Problem Description

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the **water source**, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can **add up all the part numbers** in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently **any number adjacent to a symbol**, even diagonally, is a "part number" and should be included in your sum. (Periods (`.`) do not count as a symbol.)

Here is an example engine schematic:

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```
In this schematic, two numbers are **not** part numbers because they are not adjacent to a symbol: `114` (top right) and `58` (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. **What is the sum of all of the part numbers in the engine schematic?**

## Part Two - Problem Description

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A **gear** is any `*` symbol that is adjacent to exactly two part numbers. Its **gear ratio** is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

In this schematic, there are **two** gears. The first is in the top left; it has part numbers `467` and `35`, so its gear ratio is `16345`. The second gear is in the lower right; its gear ratio is `451490`. (The `*` adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces `467835`.

**What is the sum of all of the gear ratios in your engine schematic?**


