#!/usr/bin/env python3
"""
Author: Ian
Purpose: Coding challenge as per
https://leetcode.com/problems/perfect-squares/submissions/
Input: INT, positive int
Output: INT, least number of perf squares that sum to input 
"""
from itertools import combinations_with_replacement
import pdb

if __name__ == "__main__":

	num = 9

	assert isinstance(num, int), 'Input must be int'
	assert num != 0, 'Input must not be 0'

	# all sq_nums that are less than num
	sq_nums = [x**2 for x in range(1, round(num ** (1/2)) + 1)]

	# get first combo of sq_nums that == num
	i = 0
	outcome = 0
	while outcome == 0:
		i += 1
		combos = list([ x for x in combinations_with_replacement(sq_nums, i) if sum(x) == num])
		if combos == []: continue
		else: outcome = len(combos[0]); print(combos[0])

	print(outcome)
