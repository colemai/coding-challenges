#!/usr/bin/env python3
"""
Author: Ian Coleman
Challenge:  Decompress a compressed string as per
https://techdevguide.withgoogle.com/paths/advanced/compress-decompression#code-challenge
"""

import pdb
from sys import argv

def get_input(input_file):
	"""
	Get input and output it as string
	"""
	with open(input_file) as file_object:
		compressed = file_object.readline()
		return(compressed)

# def count_noncross_perf_matches (nodes):
# 	"""
# 	Purpose: Count noncrossing perfect matches
# 	Input: INT nodes the number of nodes in the circular graph
# 	Output: INT total number of non-crossing perfect matches
# 	"""
# 	n = int(nodes/2)
# 	local_total = 0
# 	for m in range(2, nodes+1, 2):
# 		n_left = int((m - 2)/2)
# 		n_right = int((nodes - m)/2)

# 		# For each side of the 1-m bond, count noncross-perf-matches
# 		if n_left == 2:
# 			c_left = 2
# 		elif n_left == 1:
# 			c_left = 1
# 		elif n_left == 0:
# 			c_left = 1
# 		else: c_left = count_noncross_perf_matches(n_left * 2)

# 		if n_right == 2:
# 			c_right = 2 
# 		elif n_right == 1:
# 			c_right = 1 
# 		elif n_right == 0:
# 			c_right = 1 
# 		else: c_right = count_noncross_perf_matches(n_right * 2)
		
# 		local_total += c_left * c_right

# 	return local_total


def simple_convert(compressed):
	"""
	Process simplest chunks of compressed string (those with one '[')
	Input: STRING of shape 'num[string]' or 'num[string]string'
	Output: STRING
	"""
	decompressed = ''
	intermediates = compressed.split('[')
	# pdb.set_trace()
	num = int(intermediates[0])
	end_of_bracket = intermediates[1].find(']')
	string = intermediates[1][:end_of_bracket] # note I cut out the last char -> ]
	optional_end = intermediates[1][end_of_bracket+1:]
	decompressed = num * string
	decompressed += optional_end
	return decompressed

def decompress_string(compressed):
	"""
	Input: STRING compressed, of the form 3[ab]2[ac] etc.
	Output: STRING decompressed
	Example: decompress_string('5[k]3[2[ag]h]')
	"""
	decompressed = ''
	
	if compressed.count('[') > 1:
		
		# This chunk splits the string into logical pieces (top layer of num[str]'s)
		intermediate = compressed.split(']') 
		intermediate = list(filter(None, intermediate)) # remove empty strings
		# Iterate through the pieces, re-add delimiter and stitch pieces together where req'd
		to_del = [] # Will need to delete elements that have been stitched to others
		for i in range(0,len(intermediate) - 1):
			intermediate[i] += ']'
			if intermediate[i].count('[') > 1:
				intermediate[i] += intermediate[i+1] + ']'
				to_del.append(i+1)
		# Now delete all the pieces that were stitched to other pieces
		for index in sorted(to_del, reverse=True):
			del intermediate[index]

		# iterate thru pieces and if still more than one bracket then strip outtermost
		for i in range(0, len(intermediate)):
			if intermediate[i].count('[') > 1:
				# pdb.set_trace()
				first_bracket = intermediate[i].find('[')
				prefix = intermediate[i].split('[')[0] + '['
				body = intermediate[i][first_bracket+1:-1]
				print('body ', body)
				intermediate[i] = prefix + decompress_string(body) + ']'
				print('frank ', intermediate[i])
		# Now run all pieces through again
		for x in intermediate:
			decompressed += decompress_string(x)

	elif compressed.count('[') ==1:
		decompressed += simple_convert(compressed)
	else:
		decompressed += compressed
	return decompressed


if __name__ == "__main__":
	# First get input
	compressed = get_input(argv[1])
	decompressed = decompress_string(compressed)
	print('Answer: ', decompressed)