#!/usr/bin/env python3

"""
Author: Ian
Purpose: Coding challenge as per https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
Input: String
Output: Int
"""

import pdb
import math

def sherlockAndAnagrams(s):
	# For each size of sub string, collect all substrings
	# sort each substring alpabetically
	# count the occurence of each element
	# for each, add count -1 to anagrams
	anagrams = 0
	for substring_size in range(1, len(s)):
		substrings = []
		for position in range(0,(len(s) - substring_size) + 1):
			substrings.append(s[position:(position + substring_size)])
		substrings = [''.join(sorted(x)) for x in substrings]
		counts = dict((x,substrings.count(x)) for x in set(substrings))
		for count in counts.values():
			count -= 1
			if count > 0:
				anagrams += ((count * count) + count)/2
	return int(anagrams)

if __name__ == "__main__":
	s = "kkkk"
	ans = sherlockAndAnagrams(s)
	print(ans)

	assert sherlockAndAnagrams("mom") == 2
	assert sherlockAndAnagrams("abba") == 4
	assert sherlockAndAnagrams("abcd") == 0
	assert sherlockAndAnagrams("ifailuhkqq") == 3
	assert sherlockAndAnagrams("kkkk") == 10
	assert sherlockAndAnagrams("cdcd") == 5
	