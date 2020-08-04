#!/usr/bin/env python3

"""
Author: Ian Coleman
Purpose: Coding challenge
Input: 
Output: 
Example Run: 


Plan:
1. Read challenge three times
2. Plan
3. Implement brute solution
4. Account for edge cases
5. Adapt or rewrite for readability, modularity, PEP8 style
6. Adapt or rewrite for efficency
7. Adapt or rewrite for security
8. Sanity checks


Task:
1. Create n by n grid
2. 
"""


import pdb

def print_grid(n):
    grid = []

    column_numbers = [str(x) for x in range(1, n + 1)]
    first_line = "  " + "  ".join(column_numbers)
    grid.append(first_line)

    horizontal_unit = "+--"
    vertical_unit = "|  "

    for row in range(1, n + 1):
        grid += [" " + (horizontal_unit * n) + "+"]
        grid += [str(row) + (vertical_unit * n) + "|"]
    grid += [" " + (horizontal_unit * n) + "+"]

    return grid


if __name__ == "__main__":
    
    ans = print_grid(3)
    [print(x) for x in ans]

    # assert sherlockAndAnagrams("mom") == 2
    # assert type(options) is dict
    # assert 'message' in options
    # assert isinstance(options['message'], str)
    # assert bool(options) == True