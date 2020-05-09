#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Candy distribution challenge as per
https://leetcode.com/problems/distribute-candies/
Input: File with single list of ints, even length
Output: INT, number of candies sister can have
"""

from sys import argv
import pdb
import ast
from collections import Counter
from time import time

"""
Questions about the question:
- Are the ints always positive (no!)
- Is the input always valid

Edge Cases:
- [] --> handles successfully
- neg ints --> handles successfully

Efficiency:
- Big O linear one

"""

def get_list(file):
	with open(file) as file_object:
		candies = file_object.readline()
		candies = ast.literal_eval(candies)
		return candies

def distribute_candies (candies):
	"""
	Purpose: Evenly distribute candies to maximise types sister has
	Input: LIST candies of even length with only ints
	Output: INT max number of types of candies sister had
	Example: distribute_candies([1,1,-2,-2,3,3]) # 3
	"""
	total_candies = len(candies)
	sis_quota = total_candies//2
	unique_types = set(candies)
	ans = min(sis_quota, len(unique_types))
	return ans


if __name__ == "__main__":
	candies = get_list(argv[1])
	t1 = time()

	candies = [1,1,1,1,7,8,7,9]
	answer = distribute_candies(candies)
	print('time: ', time()-t1)
	print(answer)

	assert distribute_candies([1,1,2,3]) == 2, 'candies 1123 fail'
	assert distribute_candies([1,1,2,3,1,4]) == 3, 'candies 112314 fail'