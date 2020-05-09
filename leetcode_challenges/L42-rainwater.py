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
- Where the last hill is tallest
"""

def get_retained_water (height):
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
	while i < len(height) -1:
		if (not wall1) and (height[i] > height[i+1]):
			wall1 = i
			i += 1
		elif (wall1) and (height[i] >= height[wall1]):
			wall2 = i
			water += calc_retained_water(height, wall1, wall2)
			wall1, wall2 = None, None
			i -= 1
		i += 1	

	# The above while loop will not capture the end of the height, this will:
	last_tallest = 0
	while last_tallest < (len(height) -1):
		if wall1 >= (len(height) - 2): return water # as no more can be retained
		remaining_wall = height[wall1+2:]
		top_remaining_ht = max(remaining_wall)
		last_tallest = [i for i, j in enumerate(height) if j == top_remaining_ht][-1]
		water += calc_retained_water(height, wall1, last_tallest)
		wall1 = last_tallest

	return water

def calc_retained_water (height, wall1, wall2):
	"""
	USED IN: get_retained_water
	Take in a subset of height and return water held by it
	Input:
		LIST height, pos ints
		INT wall1, index of height that starts substruc
		INT wall2, index of height that ends substruc
	Output: 
		INT water held by substruc
	"""
	ht = min(height[wall1], height[wall2])
	width = (wall2 - wall1) - 1
	potential_water = ht * width

	# Now substract the smaller hills that are taking up water space
	detractors = 0
	for elem in height[wall1+1:wall2]:
		detractors += elem

	water = potential_water - detractors
	return water


if __name__ == "__main__":
	# Input (manually for now):
	height = [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]
	water = get_retained_water(height)
	print('Answer: ', water)
