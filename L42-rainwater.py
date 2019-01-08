#!/usr/bin/env python3
"""
Author: Ian
Purpose: Calculate trapped rainwater as per
https://leetcode.com/problems/trapping-rain-water/
Input: LIST, positive ints
Output: INT, amount of rainwater trapped
"""

import pdb 

# 1. question
# 2. Brute test case
# 3. Edge cases
# 4. Optimise
# 5. Testing

"""
Questions:
- positive ints: yes
- ever empty

Edge cases:
- holds no water
"""

# shape = [0,1,0,2,1,0,1,3,2,1,2,1]
# water = 0
# i = 0
# wall1 = None, wall2 = None


def get_retained_water (shape):
	"""
	USES: calc_retained_water
	"""
	# Chop out evrey elem until one that's smaller than subsequent
	# Same for end
	# Iterate through elems and take firs two (elem for which next is smaller - except i + 1)
	water = 0

	# Iterate through and get substructures enclosed by two walls
	wall1 = None
	wall2 = None
	i = 0
	while i < len(shape) -1:
		if (not wall1) and (shape[i] > shape[i+1]):
			wall1 = i
			i += 1
		elif (wall1) and (shape[i] >= shape[wall1]):
			wall2 = i
			water += calc_retained_water(shape, wall1, wall2)
			wall1, wall2 = None, None
			i -= 1
		i += 1	

	# The above while loop will not capture the end of the shape, this will:
	last_tallest = 0
	while last_tallest < (len(shape) -1):
		if wall1 >= (len(shape) - 2): return water # as no more can be retained
		remaining_wall = shape[wall1+2:]
		top_remaining_height = max(remaining_wall)
		last_tallest = [i for i, j in enumerate(shape) if j == top_remaining_height][-1]
		water += calc_retained_water(shape, wall1, last_tallest)
		wall1 = last_tallest

	return water

def calc_retained_water (shape, wall1, wall2):
	"""
	USED IN: get_retained_water
	Take in a subset of shape and return water held by it
	Input:
		LIST shape, pos ints
		INT wall1, index of shape that starts substruc
		INT wall2, index of shape that ends substruc
	Output: 
		INT water held by substruc
	"""
	height = min(shape[wall1], shape[wall2])
	width = (wall2 - wall1) - 1
	potential_water = height * width

	# Now substract the smaller hills that are taking up water space
	detractors = 0
	for elem in shape[wall1+1:wall2]:
		detractors += elem

	water = potential_water - detractors
	return water


if __name__ == "__main__":
	# Input (manually for now):
	shape = [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]
	water = get_retained_water(shape)
	print('Answer: ', water)
