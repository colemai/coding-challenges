#!/usr/bin/env python3
"""
Author: Ian
Purpose: Coding challenge as per
https://www.hackerrank.com/challenges/kangaroo/problem
Input: Four ints
Output: Str "YES" or "NO"

1. Brute
2. Edge Cases
3. Optimise
4. Clean
"""



import pdb

def kangaroo(x1, v1, x2, v2):
	""""""
	# The following is the max number of possible steps based on given constraints
	steps = range(1,10000)
	for step in steps:
		kang1_pos = x1 + (v1 * step)
		kang2_pos = x2 + (v2 * step)
		if kang1_pos == kang2_pos:
			return "YES"
	return "NO"


if __name__ == "__main__":
	assert kangaroo(0, 3, 4, 2 ) == "YES"
	assert kangaroo(0, 2, 5, 3) == "NO"
