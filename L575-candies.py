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
	brothers_quota = total_candies//2
	sister_types = 0
	unique_types = set(candies)
	counts = Counter(candies).values() # Get list of value counts
	counts = sorted(counts, reverse=True)

	for i in range(0, len(counts)):
		if counts[i] > 1 and (brothers_quota > 0):
			if brothers_quota >= (counts[i] - 1):
				brothers_quota -= (counts[i] - 1)
				counts[i] = 1
			else:
				brothers_quota = 0
		elif counts[i] == 1 and (brothers_quota > 0):
			brothers_quota -= 1
			counts[i] = 0
		else:
			break

	counts = list(filter(lambda a: a != 0, counts))
	sister_types = len(counts)
	return(sister_types)


if __name__ == "__main__":
	candies = get_list(argv[1])
	answer = distribute_candies(candies)
	print(answer)