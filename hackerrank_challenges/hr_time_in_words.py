#!/usr/bin/env python3

"""
Author: Ian
Purpose: Coding challenge as per https://www.hackerrank.com/challenges/the-time-in-words/problem
Input: String time e.g 12:15
Output: String time in words
"""

import pdb

def timeInWords(h, m):
	""""""
	# hour_keys = range(1, 13)
	# hour_values = ["one", "two", "three", "four", "five", "six", "seven", \
	#   "eight", "nine", "ten", "eleven", "twelve"]
	# hour_dict = dict(zip(hour_keys, hour_values))

	num_to_word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
			 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
			11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
			15: 'quarter', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
			19: 'Nineteen', 20: 'Twenty', 30: 'Half'}
	# time = []
	if m == 0:
		time = "{} o' clock".format(num_to_word[h])
		return time.lower()

	time = []
	to = False
	if m > 30:
		to = True
		m = 60 - m
	if m in range(21,30):
		time.append("twenty {} minutes ".format(num_to_word[m % 10]))
	elif (m == 15) or (m == 30):
		time.append("{} ".format(num_to_word[m]))
	elif (m == 1):
		time.append("one minute ")
	else:
		time.append("{} minutes ".format(num_to_word[m]))
	
	if not to:
		time.append("past {}".format(num_to_word[h]))
	else:
		if h == 12:
			time.append("to one")
		else:
			time.append("to {}".format(num_to_word[h + 1]))
	time = ''.join(time)

	time = time.lower()	
	return time

if __name__ == "__main__":

	ans = timeInWords(1,1)
	print(ans)

	assert timeInWords(3,00) == "three o' clock"
	assert timeInWords(3,1) == "one minute past three"
	assert timeInWords(3,0) == "three o' clock"
	assert timeInWords(12,30) == "half past twelve"
	assert timeInWords(12,52) == "eight minutes to one"
	assert timeInWords(12,45) == "quarter to one"
	assert timeInWords(12,0) == "twelve o' clock"
	assert timeInWords(1,0) == "one o' clock"
	assert timeInWords(1,15) == "quarter past one"
	assert timeInWords(1,29) == "twenty nine minutes past one"
	assert timeInWords(1,31) == "twenty nine minutes to two"