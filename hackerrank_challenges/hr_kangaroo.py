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

Edge cases
 - if v2 > v1
 - 
"""



import pdb

def kangaroo(x1, v1, x2, v2):
	""""""
	# The following is the max number of possible steps based on given constraints
	if v2 > v1:
		return "NO" # kang1 will never catch up

	x1_even = (min(x1, 2) % max(x1,2)) % 2 == 0
	v1_even = max(v1, 2) % min(v1,2) == 0
	k1_always_even = x1_even and v1_even
	k1_always_odd = not x1_even and not v1_even
	x2_even = (min(x2, 2) % max(x2,2)) % 2 == 0
	v2_even = max(v2, 2) % min(v2,2) == 0
	k2_always_even = x2_even and v2_even
	k2_always_odd = not x2_even and not v2_even
	if (k1_always_even and k2_always_odd) or (k1_always_odd) and (k2_always_even):
		return "NO"

	steps = range(1,10000)
	for step in steps:
		kang1_pos = x1 + (v1 * step)
		kang2_pos = x2 + (v2 * step)
		if kang1_pos > kang2_pos:
			return "NO"
		elif kang1_pos == kang2_pos:
			return "YES"
	return "NO"



if __name__ == "__main__":
	assert kangaroo(0, 3, 4, 2 ) == "YES"
	assert kangaroo(0, 2, 5, 3) == "NO"
