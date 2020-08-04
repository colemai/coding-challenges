#!/usr/bin/env python3

"""
Author: Ian Coleman
Purpose: Coding challenge

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
    """ Delete a column seperator """ 
    if i == 1:
        converted_row =  2
    else: 
        converted_row = 2 + (2 * (i - 1)) 
    converted_column = ((j) * 2) + (j + 1)

    string_to_change = g[converted_row]
    new_string = string_to_change[:converted_column] \
        + " " + string_to_change[converted_column + 1:]
    g[converted_row] = new_string
    
    return grid


def delete_h(g, i, j):
    """ Delete a row seperator """ 
    # pdb.set_trace()
    if i == 1:
        converted_row = 3
    else: 
        converted_row = 3 + (2 * (i - 1))
    converted_column = ((j - 1) * 2) + j + 1


    string_to_change = g[converted_row]
    new_string = string_to_change[:converted_column] \
        + "  " + string_to_change[converted_column + 2:]
    g[converted_row] = new_string
    
    return grid

if __name__ == "__main__":
    grid = new_grid(5)
    print_grid(grid)
    new_grid = delete_v(grid, 1, 1)
    new_grid = delete_h(new_grid, 1, 1)
    print_grid(new_grid)