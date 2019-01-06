#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Calculate max no vacation days as per challenge
https://www.leetfree.com/problems/maximum-vacation-days.html
Input: flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
Output: INT max number of vacation days
"""

from sys import argv
import pdb
from itertools import product
from itertools import permutations


"""
Questions:
- can I fly on first day: yes
- is the input always valid

Edge cases:
- all zeros or multiple zeros in flights

"""

def check_feasible (days, flights):
	"""
	USED IN get_max_vacation
	Input: (1,0,1) int tuple
	Output:
	"""
	pass

def get_max_vacation (flights, days):
	"""
	Input: 
		LIST flights, a two dimensional matrix representing city-city flighta
		LIST days, a 2D matrix represnting days off per week per city
	Output:
		INT, max num vacation days
	"""


	# Brute force collect all the 3n combinations from the days
	# let's get the indices and combine those (easier)
	indices = list(range(0,len(days[0])))
	indice_perms = list(permutations(indices))
	perms = []

	for i in range(0, len(indice_perms)):
		# pdb.set_trace()
		tmp_perm = []
		for j in range(0, len(days[0])):
			tmp_perm.append(days[indice_perms[i][j]][j])
		perms.append(tmp_perm)
	
	print(perms)
	exit()
	# pdb.set_trace()
	combos = list(product(days))
	combos = list(set(list(combos))) # crudely get unique elements
	print(combos)
	# print([(a,b,c) for a,b,c in zip(days[0],days[1],days[2])])
	exit()

	# order these by sum
	# combos.sort(key=lambda x: sum(x), reverse=True)
	return combos
	# iterate through them and return the first one that is feasible by flights
	for combo in combos:
		pass



if __name__ == "__main__":
	# Get the input in the correct format (will do manually for now)
	flights = [[0,1,1],[1,0,1],[1,1,0]]
	days = [[1,3,1],[6,0,3],[3,3,3]]
	days = [[1,0,3], [4,5,6], [7,8,9]]
	answer = get_max_vacation(flights, days)
	print(answer)
	#