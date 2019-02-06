#!/usr/bin/env python3
"""
Author: Ian
Purpose: coding challenge as per:
https://leetcode.com/problems/next-permutation/
Input: List (numbers, assuming ints)
Output: List
"""

import pdb
from lib import testing


"""
1. q, assum
2. Brute
3. Edge
4. Optim
5. Test
"""

# @testing.profile
# def nextPermutation(nums):
# 	"""
# 	"""
# 	# zip it up dawg
# 	rev = nums[::-1]

# 	# Standard case (next lex perm)
# 	for i, num in enumerate(rev):
# 		if rev[i+1] < num:

# 			rev[i] = rev[i+1]
# 			rev[i+1] = num
# 			return rev[::-1]
# 	return rev 	# Rare case (lowest lex perm)


# @testing.profile
def nextPermutation(nums):
	"""
	"""	
	# Standard case (next lex perm)
	# iterate through pairs, backwards
	rev = nums[::-1]
	for i,pair in enumerate(zip(rev[:-1], rev[1:])):
		if pair[0] > pair[1]:
			rev[i] = pair[1]
			rev[i+1] = pair[0]
			return rev[::-1]
	return rev 	# Rare case (lowest lex perm)




if __name__ == "__main__":
	nums = [1,2,3]
	ans = nextPermutation(nums)
	print(ans)

	assert nextPermutation([1,2,3]) == [1,3,2]
	assert nextPermutation([3,2,1]) == [1,2,3]
	assert nextPermutation([1,1,5]) == [1,5,1]