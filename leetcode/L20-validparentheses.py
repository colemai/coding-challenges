#!/usr/bin/bash python
"""
Author: Ian
Purpose: coding challenge as per
https://leetcode.com/problems/valid-parentheses/
Input: STR - made up of only (){}[]
Output: Print BOOL if string is valid
"""

import pdb
import time

"""
1. Q
2. Test
3. Brute
4. Optim
5. Test
"""

## NOTE this isn't actually right...
# In my head '([)]' was valid which it is not

def generate_char (strung):
    """ Generator expression to yield string by chars   """
    yield from [x for x in strung]


def check_val_parenth (parenths):
    """
    Check if parenths in string are valid
    """
    count_brack = 0
    count_parenth = 0
    count_curls = 0
    counts = {'(':0, '{':0, '[':0}
    parenth_opposite = {')':'(','}':'{',']':'['}
    for shape in generate_char(parenths):
        try:
            # if it's an opening bracket add 1
            counts[shape] += 1
        except KeyError:
            # if it's a closing bracket minus 1
            counts[parenth_opposite[shape]] -= 1
            if counts[parenth_opposite[shape]] < 0:
                return False
        except:
            'whoopsie'          
    if sum(counts.values()) != 0:
        return False
    return True

if __name__ == "__main__":
    t1 = time.time()
    ans = check_val_parenth('([]{})([]{})([]{})([]{})')
    print(ans)
    print('time: ', time.time()-t1)
    assert check_val_parenth('()') == True, 'check_val_parenth fail for ()'
    assert check_val_parenth('([]{})') == True, 'check_val_parenth fail for ([]{})'
    assert check_val_parenth('(]') == False, 'check_val_parenth fail for (]'
    assert check_val_parenth('())') == False, 'check_val_parenth fail for ())'

