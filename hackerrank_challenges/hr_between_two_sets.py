#!/usr/bin/env python3

"""
Author: Ian
Purpose: Coding challenge as per https://www.hackerrank.com/challenges/between-two-sets/problem
Input: Two Arrays of ints
Output: Int

1. Brute Case
2. Edge Cases
3. Optimise
4. Readability, DRY
"""


def getTotalX(a, b):
	""""""
	smallest_fac = min(a)
	biggest_mult = max(b)
	multiplier = int(biggest_mult / smallest_fac)
	possible_hits = [smallest_fac * x for x in range(1, multiplier + 1)]
	possible_hits = [x for x in possible_hits if (x >= max(a))]
	possible_hits = [x for x in possible_hits if (x <= min(b))]
	for mult in b:
		possible_hits = [x for x in possible_hits if mult % x == 0]
	for fact in a:
		possible_hits = [x for x in possible_hits if x % fact == 0]

	return len(possible_hits)




if __name__ == "__main__":
	getTotalX([2, 6], [24, 36])

	assert getTotalX([2, 4], [16, 32, 96]) == 3
	assert getTotalX([2, 6], [24, 36]) == 2
