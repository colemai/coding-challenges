#!/usr/bin/env python3

"""
Author: Ian
Purpose: Coding challenge as per https://www.hackerrank.com/challenges/electronics-shop/problem
Input: 
Output: 
"""

def getMoneySpent(keyboards, drives, b):
    min_spend = min(keyboards) + min(drives)
    if min_spend > b:
    	return -1

    possible_spends = []
    for keyboard in keyboards:
    	possible_spends += [keyboard + x for x in drives]
    possible_spends = [x for x in possible_spends if x <= b]
    return max(possible_spends)


if __name__ == "__main__":
	b = 10
	keyboards = [3, 1]
	drives = [5, 2, 8]
	
	ans = getMoneySpent(keyboards, drives, b)

	print(ans)
	