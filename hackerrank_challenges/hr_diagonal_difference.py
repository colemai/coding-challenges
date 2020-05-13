#!/usr/bin/env python3
"""
Author: Ian
Purpose: Coding challenge as per
https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen
Input: Square matrix
Output: The difference of the (sum of diagonal)'s

NB Hackerrank didn't accept this as they don't allow import of special libs like numpy
"""

import numpy as np


def diagonalDifference(arr):
    np_arr = np.array(arr)
    flipped = np.fliplr(np_arr)
    sum_diag = (np.trace(np_arr))
    sum_reverse_diag = (np.trace(flipped))
    return abs(sum_diag - sum_reverse_diag)

if __name__ == "__main__":
	arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
	ans = diagonalDifference(arr)
	print(ans)