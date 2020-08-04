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


def new_grid(n):
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


def print_grid(grid):
    [print(x) for x in grid]


def delete_v(g, i, j):
    converted_column = ((j) * 2) + (j + 1)
    converted_row = ((i - 1) * 2) + i 
    string_to_change = g[converted_row]
    new_string = string_to_change[:converted_column] \
        + " " + string_to_change[converted_column + 1:]
    g[converted_row] = new_string
    
    return grid


# def delete_h(g, i, j):
#     pdb.set_trace()
#     converted_column = ((j) * 2) + (j + 1)
#     converted_row = ((i - 1) * 2) + i 
#     string_to_change = g[converted_row]
#     new_string = string_to_change[:converted_column] \
#         + " " + string_to_change[converted_column + 1:]
#     g[converted_row] = new_string
    
#     return grid

if __name__ == "__main__":
    grid = new_grid(3)
    print_grid(grid)
    new_grid = delete_v(grid, 2, 3)
    # new_grid = delete_h(grid, 2, 3)
    print_grid(grid)


    # assert sherlockAndAnagrams("mom") == 2
    # assert type(options) is dict
    # assert 'message' in options
    # assert isinstance(options['message'], str)
    # assert bool(options) == True