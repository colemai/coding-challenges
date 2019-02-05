#!/usr/bin/env python3
"""
Author: Ian
Purpose: Coding challenge as per
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Input: Sorted List
Output: INT len of list w/o duplicates nb memory restriction
"""

import pdb
from itertools import permutations
from lib import testing

"""
1. q
2. brute
3. edge
4. prof opt
5. testing
"""

def removeDuplicates(nums):
	"""
	"""
	nums = [x for i,x in enumerate(nums) if x != nums[i-1]]
	print(nums)
	return len(nums)

if __name__ == "__main__":
	nums = [1,1,1,2]
	ans = removeDuplicates(nums)
	print(ans)

	assert removeDuplicates([1,1,2]) == 2
	assert removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
