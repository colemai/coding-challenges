#!/usr/bin/env python3
"""
Author: Ian
Purpose: Coding challenge as per
https://leetcode.com/problems/regular-expression-matching/
Input:
    STR s
    STR p
Output: 
    BOOL, True if p matches s else False
"""

import pdb
import re

def match (s,p):
    """
    Input:
        STR s
        STR p
    Output: 
        BOOL, True if p matches s else False
    """
    
    while len(s) > 0:
        if len(p) == 0: return False
        letter = s[0]
        pattern = p[0]

        # Special case (asterisk)
        if len(p) > 1 and p[1] == '*':
            # pdb.set_trace()
            print('Special case')
            # letter case
            if letter == pattern:
                print('Letter case')
                # x* matches 1/multiple letters
                # find first non matching pattern:
                # my_regex = r"\b(?=\w)" + re.escape(TEXTO) + r"\b(?!\w)"
                # pdb.set_trace()
                if re.search(r'[^' + letter + ']', s) is not None:
                    non_matching = re.search(r'[^' + letter + ']', s).start()
                    s = s[non_matching:]
                    p = p[2:]
                    continue
                else: 
                    return True

            # period case
            elif pattern == '.':
                print('period case')
                # 'aaab'
                # '.*'
                
                # if letter remaining
                if re.search(r'[A-Za-z]', p[2:]) is not None:
                    print('letter remains')
                    # find next letter after .*/.*..*.. etc in pattern
                    first_diff_ind = re.search(r'[A-Za-z]', p[2:]).start() + 2
                    first_diff_char = p[first_diff_ind]
                    # Get all occurences of this in the string
                    # For each occurence split before and after it and see if tangible
                    # pdb.set_trace()
                    # indices = [i for i, x in enumerate(s) if x == first_diff_char]
                    indices = []
                    for i,x in enumerate(s):
                        if x == first_diff_char:
                            indices.append(i)

                    matches = []
                    for i in indices:
                        half1s = s[:i]
                        half1p = p[:first_diff_ind]
                        half2s = s[i:]
                        half2p = p[first_diff_ind:]
                        # pdb.set_trace()
                        first_match = match(s[:i], p[:first_diff_ind])
                        second_match = match(s[i:], p[first_diff_ind:])
                        matches.append(first_match and second_match)
                    # matches = [match(s[:i], p[:first_diff_ind]) and match(s[i:], p[first_diff_ind:]) for i in indices]
                    if any(matches): return True
                    else: return False

                # if no letter remaining
                elif re.search(r'[.]', p[2:]) is not None:
                    print('no letter remains')
                    asterisk_left = '*' in p
                    if asterisk_left:
                        periods, asterisks = p.count('.'), p.count('*')
                        lone_periods = asterisks - periods 
                        if len(s) >= lone_periods: return True
                        else: return False
                    elif not asterisk_left:
                        if len(p) == len(s): return True
                        else: return False

                else:
                    # Nothing left of pattern but .* and s has chars still
                    return True
                
            else:
                print('zero case')
                # x* matches 0 letters
                p = p[2:]
                continue

        # Regular case (no asterisk)
        elif letter == pattern or pattern is '.':
            print('Regular case')
            # regular match
            p = p[1:] 
            s = s[1:]
            continue
        else:
            return False
    # All g, unless there's unmatched pattern left
    if len(p) > 0: 
        return False
    else:
        return True

if __name__ == "__main__":
    s = "bbbba"
    p = ".*a*a"
    answer = match(s,p)
    print(answer)