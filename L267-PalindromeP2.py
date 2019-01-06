#!/usr/bin/env python3
"""
Author: Ian Coleman
Input: 
Output:

Challenge:
Given a string s, return all the palindromic permutations (without duplicates) of it.
Return an empty list if no palindromic permutation could be form.
For example:
Given s = "aabb", return ["abba", "baab"].
Given s = "abc", return [].
"""

from sys import argv
import pdb
from itertools import permutations
from sympy.utilities.iterables import multiset_permutations

# 1. Test case x
# 2. Brute  
# 3. Optimise
# 4. Run Edge cases
# 5. Write Tests

# TODO make sure even numbers of each letter
# make sure palindromic perm possible (only one uneven count)
#


# def make_permutations (s):
# 	"""
# 	Input: STRING s
# 	Output: List of permutations of s
# 	"""
# 	perms = permutations(s)
# 	perms = [''.join(x) for x in perms]
# 	return(list(perms))


# def is_palindrome (s):
# 	"""
# 	Input: STRING s
# 	Output: BOOLEAN, True if s is a palindrome
# 	"""
# 	if s[::-1] == s:
# 		return True
# 	else:
# 		return False

def get_symmetrical_half (s):
	""" 
	Input: STRING s, must have even numbers of each char (except optionally for one letter)
	Output: STRING, Symmetrical half of s
	"""
	assert isinstance(s, str), 'Argument must be string'


	even = len(s) % 2 == 0
	letters = list(set(list(s))) # crudely get unique letters
	counts = []
	symm_half = ''
	for letter in letters:
		counts.append(s.count(letter))

	# Actually let's get the odd letter here (in the case of uneven length)
	odd_letter = ''
	if not even:
		# Check string valid (odd length):
		if not len([x for x in counts if x % 2 != 0]) == 1: exit('[]')
		
		odd_letter = [x for x in letters if s.count(x) % 2 != 0][0]
		letters.remove(odd_letter)
		counts = [x for x in counts if x % 2 == 0]

	# Check valid string (even length):
	if not len([x for x in counts if x % 2 != 0]) == 0: exit('[]')

	for i in range(0, len(letters)):
		symm_half += ((counts[i]//2) * letters[i])
	
	return(symm_half, odd_letter)

def get_pal_perms (sym_half, odd_letter):
	"""
	Input: STRING sym_half - half the string as split by letter,
		   STRING odd_letter - the odd letter if there is one
	Output: LIST of all palindromic permutations of s
	"""
	perms = list(multiset_permutations(list(sym_half)))
	perms = [''.join(x) for x in perms]
	pal_perms = [x + odd_letter + x[::-1] for x in perms]
	return pal_perms


if __name__ == "__main__":
	s = 'aabbc'

	# Edge Cases
	if len(s) == 1:
		print(s)
		exit()
	elif len(s) == 0:
		print('Error: must give non-empty string')
		exit()

	sym_half, odd_letter = get_symmetrical_half(s)
	pal_perms = get_pal_perms(sym_half, odd_letter)
	print(pal_perms)
	

