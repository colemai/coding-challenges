#!/usr/bin/env python3
"""
Author: Ian
Purpose: Find median of two sorted lists as per
https://leetcode.com/problems/median-of-two-sorted-arrays/
Input: Two sorted lists
Output: INT, their combined median
"""

from sys import argv
import pdb
import numpy as np
from statistics import median

# 1. Understand q
# 2. Brute test case
# 3. Extend to other answers
# 4. Optimise
# 5. Edge cases
# 6. tests

"""
Input always valid? - can assume that at least one list not empty
input always ints?
inputs always positive numbers? 

Edge cases:
- One empty list
- floats
- negative numbers
- zeros
"""

if __name__ == "__main__":
	nums1 = [1, 3, 5, 9]
	nums2 = [2]
	nums1.extend(nums2)
	print(median(nums1))

	# this was disappointingly easy. I should have searched for a faster solution
	# maybe I'm not supposed to use standard lib --> seems likely