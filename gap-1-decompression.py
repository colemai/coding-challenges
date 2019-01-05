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

def simple_convert(compressed):
	"""
	Process simplest chunks of compressed string (those with one '[')
	Input: STRING of shape 'num[string]' or 'num[string]string'
	Output: STRING, decompressed version of input
	"""
	decompressed = ''
	intermediates = compressed.split('[')
	num = int(intermediates[0])
	end_of_bracket = intermediates[1].find(']')
	string = intermediates[1][:end_of_bracket] 
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
	
	# If the compressed string is complex, break it into increasingly simple chunks
	if compressed.count('[') > 1:
		
		# This bit splits the top layer into logical pieces
		intermediate = compressed.split(']') 
		intermediate = list(filter(None, intermediate)) # remove empty strings
		to_del = [] # Will need to delete elements that have been stitched to others
		for i in range(0,len(intermediate) - 1):
			intermediate[i] += ']'
			if intermediate[i].count('[') > 1:
				intermediate[i] += intermediate[i+1] + ']'
				to_del.append(i+1)
		for index in sorted(to_del, reverse=True):
			del intermediate[index]

		# Now take the top layer pieces and tear open any that remain complex
		for i in range(0, len(intermediate)):
			if intermediate[i].count('[') > 1:
				# This bit recursively shirks off the top layer until single layered
				first_bracket = intermediate[i].find('[')
				prefix = intermediate[i].split('[')[0] + '['
				body = intermediate[i][first_bracket+1:-1]
				intermediate[i] = prefix + decompress_string(body) + ']'
		
		# Now we can run all pieces through this function again
		for x in intermediate:
			decompressed += decompress_string(x)

	elif compressed.count('[') ==1:
		decompressed += simple_convert(compressed)
	else:
		decompressed += compressed
	return decompressed


if __name__ == "__main__":
	compressed = get_input(argv[1])
	decompressed = decompress_string(compressed)
	print('Answer: ', decompressed)