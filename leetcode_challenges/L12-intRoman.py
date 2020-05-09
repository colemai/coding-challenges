#!/usr/bin/env python3
"""
Author: Ian
Purpose: Convert Integer to Ruman Numeral as per
https://leetcode.com/problems/integer-to-roman/
Input: INT from 1 to 3999
Output: STR roman numeral of that int
"""

import pdb

"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Test cases
4
12
19
21
199
195
2000
2430

Edge cases?
0
1
floats
"""

def int_to_roman (num):
	"""
	"""
	# dicter = {'I': 1, 'V':5 'X':10 'L':50 'C':100 'D':500 'M':1000}
	desc_rom = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
	desc_num = [1000, 500, 100, 50, 10, 5, 1]
	ans = ''

	# Get the basic version (no subtraction)
	for i in range(0, len(desc_rom)):
		if num >= desc_num[i]:
			ans += desc_rom[i] * (num // desc_num[i])
			num = num % desc_num[i]
		if num == 0: break

	# Manually work in subtraction
	ans = ans.replace('DCCCC', 'CM')
	ans = ans.replace('CCCC', 'CD')
	ans = ans.replace('LXXXX', 'XC')
	ans = ans.replace('XXXX', 'XL')
	ans = ans.replace('VIIII', 'IX')
	ans = ans.replace('IIII', 'IV')
	return ans


if __name__ == "__main__":
	num = 1994
	answer = int_to_roman(num)
	print(answer)