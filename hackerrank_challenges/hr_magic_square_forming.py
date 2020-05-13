#!/usr/bin/env python3

"""
NB THIS IS CURRENTLY WRONG
Author: Ian
Purpose: Coding challenge as per https://www.hackerrank.com/challenges/magic-square-forming/problem
Input: A 3*3 matrix of ints ranged 1 to 9 inclusive
Output: int, the minimum error correction to make the matrix a magic square
"""

import math
import pdb

def formingMagicSquare(s):
	"""Input: 3x3 matix of ints range 1 through 9
	Output: positive int"""
	# 1. Choose magic_num
	cols = []
	for ind,row in enumerate(s):
		col = [x[ind] for x in s]
		cols.append(col)
	fwd_diag = [s[x][x] for x in range(0, len(s))]
	rev_diag = [s[::-1][x][x] for x in range(0, len(s))]
	row_sums = [sum(x) for x in s]
	col_sums = [sum(x) for x in cols]
	diag_sums = [sum(x) for x in [rev_diag, fwd_diag]]
	mean = sum(row_sums + col_sums + diag_sums)/8
	magic_num = int(round(mean))

	# 2. Func to find MEC for given magic_num
	# collate all the triplets that are < magicnum
	# find the intersections of these, add one
	# repeat until none
	# rows = {}
	# cols = {}
	# for i in range(0,len(s)):
	# 	rows[i] = [(i,x) for x in range(0,len(s))]
	# 	cols[i] = [(x,i) for x in range(0,len(s))]
	rows = []
	cols = []
	for i in range(0,len(s)):
		rows.append([(i,x) for x in range(0,len(s))])
		cols.append([(x,i) for x in range(0,len(s))])
	diag_one = [(0,0), (1,1), (2,2)]
	diag_two = [(0,2), (1,1), (2,0)]
	all_triples = rows + cols + [diag_one] + [diag_two]

	# iterate through triples, find those less than magic
	less_than = [x for x in all_triples if sum_from_mat(x,s) < magic_num]
	more_than = [x for x in all_triples if sum_from_mat(x,s) > magic_num]
	score = 0
	while any(less_than + more_than):
		if less_than:
			intersect, move_on = find_intersect(less_than, fwd_diag, rev_diag)
			if move_on: 
				lessers = less_than[:]
				less_than = []
			else:
				s[intersect[0]][intersect[1]] += 1
				score += 1
				less_than = [x for x in all_triples if sum_from_mat(x,s) < magic_num]
		else:
			intersect, move_on = find_intersect(more_than, fwd_diag, rev_diag)
			if move_on: 
				morers = more_than[:]
				more_than = []
			else:
				s[intersect[0]][intersect[1]] -= 1
				score += 1
				more_than = [x for x in all_triples if sum_from_mat(x,s) > magic_num]

	# For each entry in morers and for each in the lessers, add 2 to score
	pdb.set_trace()
		

	# pdb.set_trace()
	# rows = {i: [(0,x) for x in range(0,len(s))], for i in range(0,len(s))}
	# row_a = [(0,x) for x in range(0,len(s))]
	# row_b = [(1,x) for x in range(0,len(s))]
	# row_c = [(2,x) for x in range(0,len(s))]
	# for 

	# 3. Repeat for magic nums within possible realm of beating ans
	return score

def sum_from_mat(index_list, s):
	nums = [s[x[0]][x[1]] for x in index_list]	
	return sum(nums)

def find_intersect(triples, fwd_diag, rev_diag):
	""" Find the position most common among a list of triple"""
	spilled_positions = [item for sublist in triples for item in sublist]
	intersects = sorted(spilled_positions, key=spilled_positions.count, reverse=True)
	intersect = intersects[0]
	counts = intersects.count(intersect)
	pdb.set_trace()
	# Alert if the intersect would change a working triple
	move_on = False
	if counts >= 3:
		move_on = False
	elif counts == 2 and ((intersect in fwd_diag) or (intersect in rev_diag)):
		move_on = False
	else:
		move_on = True
	return intersect, move_on
	# pdb.set_trace()
# def mec_matrix_to_magic_square (mat, magic_num):



if __name__ == "__main__":
	mat = [[4, 9, 2], [3, 5, 7], [8, 1, 5]] # ans 1 
	mat = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]  # ans 4
	ans = formingMagicSquare(mat)
	print(ans)


# def formingMagicSquare(s):
# 	# First get the average sum of the rows and cols
# 	cols = []
# 	for i in range(0, len(s)):
# 		cols.append([x[i] for x in s])
# 	rows = s
# 	rows_n_cols = rows + cols

# 	sums = [sum(x) for x in rows_n_cols]
# 	mean_sum = sum(sums) / len(sums)
# 	mean_sum = int(round(mean_sum))
# 	magic_num = mean_sum

# 	# Assuming magic_num is the mean, but need to check alternatives too
# 	current_ans = dist_to_magic_square(rows, cols, magic_num)
	
# 	# Make list of possible magic nums - all ints within float mean +/- min ans
# 	possible_magic_nums = []
# 	rows_sums = [sum(x) for x in rows] # redundantly written below but who's checking
# 	cols_sums =	[sum(x) for x in cols]
# 	lower_comparator = math.floor(sum(min(rows_sums, cols_sums)) / 3)
# 	higher_comparator = math.ceil(sum(max(rows_sums, cols_sums)) / 3)
# 	possible_magic_nums = list(range((lower_comparator - current_ans), (higher_comparator + current_ans) + 1))
# 	possible_magic_nums.remove(magic_num)

# 	for magic_number in possible_magic_nums:
# 		tmp_ans = dist_to_magic_square(rows, cols, magic_number)
# 		if tmp_ans < current_ans:
# 			current_ans = tmp_ans
# 	return current_ans

	
# def dist_to_magic_square(rows, cols, magic_num):
# 	# Hypoth - cost of single change is 1 if synergy, else 2
# 	rows_sums = [sum(x) for x in rows]
# 	cols_sums =	[sum(x) for x in cols]
# 	row_deltas = [(magic_num - x) for x in rows_sums]
# 	col_deltas = [(magic_num - x) for x in cols_sums]
# 	row_deltas_abs = [abs(magic_num - x) for x in rows_sums]
# 	col_deltas_abs = [abs(magic_num - x) for x in cols_sums]
# 	rows_total_delta = sum(row_deltas_abs)
# 	cols_total_delta = sum(col_deltas_abs)

# 	cost = 0
# 	neg_row_deltas = [x for x in row_deltas if x < 0]
# 	neg_col_deltas = [x for x in col_deltas if x < 0]
# 	pos_row_deltas = [x for x in row_deltas if x > 0]
# 	pos_col_deltas = [x for x in col_deltas if x > 0]
# 	sum_row_neg = sum(neg_row_deltas)
# 	sum_col_neg = sum(neg_col_deltas)
# 	sum_row_pos = sum(pos_row_deltas)
# 	sum_col_pos = sum(pos_col_deltas)

# 	if rows_total_delta >= cols_total_delta:
# 		adders = 2 * abs(sum_row_neg)
# 		adders -= min(abs(sum_row_neg), abs(sum_col_neg))
# 		cost += adders

# 		subtractors = 2 * (abs(sum_row_pos))
# 		subtractors -= min(abs(sum_row_pos), abs(sum_col_pos))
# 		cost += subtractors
# 	else:
# 		adders = 2 * abs(sum_col_neg)
# 		adders -= min(abs(sum_col_neg), abs(sum_row_neg))
# 		cost += adders

# 		subtractors = 2 * (abs(sum_col_pos))
# 		subtractors -= min(abs(sum_col_pos), abs(sum_row_pos))
# 		cost += subtractors
	
# 	return cost