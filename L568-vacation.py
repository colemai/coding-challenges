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
from itertools import permutations


"""
Questions:
- can I fly on first day: yes
- is the input always valid

Edge cases:
- all zeros or multiple zeros in flights
- more weeks than cities

"""

def check_feasible (cities, flights):
	"""
	USED IN: get_max_vacation
	Input: 
		cities - LIST of lists, each representing a possible combination of cities
		flights - LIST of lists, matrix of flight status between cities
	Output:
		LIST of tuples, combinations of cities that are possible given flight statuses
	"""
	assert isinstance(cities, list), 'cities should be lists'
	assert not (not cities), 'cities should not be empty'

	untenable_combos = []
	for combo in cities:
		current_city = combo[0]
		for i in range(0, len(combo)-1):
			destination_city = combo[i+1]
			if (flights[current_city][destination_city] == 0 
						and destination_city != current_city):
				untenable_combos.append(combo)
				break
			else:
				current_city = destination_city

	cities = [x for x in cities if x not in untenable_combos]
	return cities

def get_max_vacation (flights, days):
	"""
	Input: 
		LIST flights, a two dimensional matrix representing city-city flighta
		LIST days, a 2D matrix represnting days off per week per city
	Output:
		INT, max num vacation days
	"""
	assert isinstance(flights, list), 'flights should be lists'
	assert isinstance(days, list), 'days should be lists'
	assert not (not days), 'days should not be empty'
	assert not (not flights), 'flights should not be empty'

	# Get all possible city combination
	cities = list(range(0,len(days[0]))) 
	city_combos = list(permutations(cities))
	perms = []
	cities = []

	# Reduce city combinations to only ones that are possible given flight status
	city_combos = check_feasible(city_combos, flights)
	if not city_combos: return sum(days[0]) # in case of no feasible combinations
	
	# Convert city combinations into 'vacation days' combinations
	for i in range(0, len(city_combos)):
		tmp_perm = []
		for j in range(0, len(days[0])):
			tmp_perm.append(days[city_combos[i][j]][j])
		perms.append(tmp_perm)


	# Order by total number of vacation days and print highest number
	perms.sort(key=lambda x: sum(x), reverse=True)
	return sum(perms[0])


if __name__ == "__main__":
	# Input: (will manually enter for now)
	flights = [[0,0,0],[0,0,0],[0,0,0]] # City status city
	days = [[1,1,1],[7,7,7],[7,7,7]]

	answer = get_max_vacation(flights, days)
	print(answer)
