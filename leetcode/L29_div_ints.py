#!/usr/bin/env python3
"""
Author: Ian
Purpose: Coding challenge as per
https://leetcode.com/problems/divide-two-integers/
Input: two INTs
Output: INT -> division product rounded down w/o * / %
"""

import pdb
from itertools import permutations
from lib import testing

"""
Victory!
Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Divide Two Integers.
Memory Usage: 6.5 MB, less than 90.91% of Python3 online submissions for Divide Two Integers.
"""

"""
1. q
2. brute
3. edge
4. prof opt
5. testing
"""

# # Brute
# @testing.profile
# def divide(dividend, divisor):
# 	"""
# 	"""
# 	# Account for 0
# 	if divisor == 0: exit('loser')

# 	# Account for negative value
# 	one_neg = (dividend * divisor)
# 	if divisor < 0: divisor *= -1
# 	if dividend < 0: dividend *= -1

# 	ans = 0
# 	while dividend >= divisor:
# 		ans += 1
# 		dividend -= divisor
# 	if one_neg < 0:
# 		ans *= -1
# 	return ans

@testing.profile
def divide(dividend, divisor):
	"""
	"""
	# Account for 0
	if divisor == 0: exit('loser')

	# Account for negative value
	one_neg = (dividend * divisor)
	dividend, divisor = abs(dividend), abs(divisor)

	ans = 0
	div = divisor + divisor
	div_fx = 2		
	
	while dividend >= (divisor + divisor):
		while dividend >= div:
			dividend -= div 
			ans += div_fx
			div += div
			div_fx += div_fx
		div = divisor + divisor
		div_fx = 2

	while dividend >= divisor:
		ans += 1
		dividend -= divisor
	
	if one_neg < 0:
		ans *= -1
	
	return ans



if __name__ == "__main__":
	dividend, divisor = 10, 1
	ans = divide(dividend, divisor)
	print(ans)

	assert divide(30, 11) == 2
	assert divide(0, 1) == 0
	assert divide(10, -1) == -10
	assert divide(-2147483648, -1) == 2147483648
