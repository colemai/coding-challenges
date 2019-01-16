#!/usr/bin/env Python3
"""
Author: Ian
Purpose: Coding challenge as per
https://leetcode.com/problems/binary-tree-right-side-view/
Input: LIST, binary tree
Output: LIST, bits of the binary tree that I can see from the right
"""

import pdb

"""
Assume: 
I can see the rightmost non-None node on every level???
"""

if __name__ == "__main__":
	bintree = [1,2,3,None,5,4, None]
	
	# Tests
	assert len(bintree) > 0, 'Input must be a valid binary tree'
	if len(bintree) == 1: print(bintree[0]); exit()
	assert len(bintree) % 2 != 0, 'Input must have odd length'

	rightmost = []

	# iterate through levels and add rightmost to output
	last_node = 0
	first_node = 0
	while last_node < len(bintree):
		this_level = bintree[first_node:last_node+1]
		this_level = [x for x in this_level if x is not None]
		print(this_level)
		rightmost.append(this_level[-1])
		prev_len = (last_node - first_node) + 1
		first_node = last_node + 1
		last_node = first_node + (prev_len * 2) - 1

	print('Ans: ', rightmost)