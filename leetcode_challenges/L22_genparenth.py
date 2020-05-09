#!/usr/bin/env python3
"""
Author: Ian
Purpose: Coding challenge as per
https://leetcode.com/problems/generate-parentheses/
Input: INT n, pairs of parenth
Output: LIST of strings, all legal combos of parenths
"""

import pdb
from itertools import permutations
from lib import testing
import pytest

"""
1. q
2. brute
3. optimise
4. edge cases
5. testing
"""

def generateParenthesis(n):
    """Input: INT n, pairs of parenth
    Output: LIST of strings, all legal combos of parenths
    """
    intake = '()' * n
    perms = permutations(intake)
    perms = [''.join(x) for x in perms]
    # Retain all legal perms
    ans = [x for x in perms if legalParenths(x)]
    return (list(set(ans)))

def legalParenths(perm):
    """
    """
    closing = 0
    opening = 0
    for par in perm:
        if par == '(':
            opening += 1
        else:
            closing += 1
        if closing > opening:
            return False
    return True

def genParenth(num):
    """
    """
    # first and last positions always same so remove
    outputs = []
    opening = '('
    closing = ')'
    for i in num:
        outputs.append(opening+closing)

@testing.profile # A profiling decorator
def generatePa(n):
    # Stole this, way better than mine
        """
        :type n: int
        :rtype: List[str]
        """
        ans = [] 
        def backtrack(S = '', left = 0, right = 0):
            if(len(S) == 2*n):
                ans.append(S)
                return
            
            if(left < n):
                backtrack(S+"(", left+1, right)
                
            if(left > right and right < n):
                backtrack(S+")", left, right+1)   
        backtrack()
        return ans

def test_sum():
    assert sum([1,3]) == 4, 'Lister not right'

if __name__ == "__main__":
    n = 2
    ans = generatePa(n)
    test_sum()
    print(ans)