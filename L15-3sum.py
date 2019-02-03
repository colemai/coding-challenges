#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Coding challenge as per
https://leetcode.com/problems/3sum/
Input: LIST ints
Output: LIST of lists, each containing three ints from input that sum to 0
"""

import pdb
from itertools import combinations
import numpy as np
from time import time

def sum3_o (nums):
    perms = combinations(nums, 3)
    # perms = [x.join for x in perms]
    # print(list(perms))
    # pdb.set_trace()
    winners = [x for x in perms if sum(x) == 0]
    winners = [sorted(x) for x in winners]
    winners = [list(x) for x in set(tuple(x) for x in winners)]
    return winners

def get_perms(nums):
    yield from [(x,sum(x)) for x in combinations(nums, 2)]

def compare_occurences (nums, tup, num):
    """Check if nums has more num than tuple"""
    if nums.count(num) > tup.count(num):
        return True
    else:
        return False

def sum3 (nums):
    perms = get_perms(nums)
    ans = []
    for tup,num in perms:
        if compare_occurences(nums, tup, num * -1):
            triplet = list(tup)
            triplet.append(num * -1)
            triplet = sorted(triplet)
            if triplet not in ans:
                ans.append(triplet)

    # ans += [(x,y) for x,y in perms if (compare_occurences(nums, x, y*-1))]
    return (ans)
    # perms = [x.join]
    # print(list(perms))
    # # pdb.set_trace()
    # winners = [x for x in perms if sum(x) == 0]
    # winners = [sorted(x) for x in winners]
    # winners = [list(x) for x in set(tuple(x) for x in winners)]
    # return winners

# def threeSum (nums):
#     for i in range(0, len(nums)):
#         for j in (nums[:i] + nums[i:]):
#             diff = nums[i] + j
#             if diff in (nums[:i] + nums[i:]).remove(j)


# ideal
# numpy array nums
# duplicate
# matrix excluding middle diagonal
# for each pair, is their (sum * -1) in list - them 


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    # t1 = time()
    # nums = [[x] for x in nums]
    # ans = sum3_o(nums)
    # print('time: o ', time()-t1)

    t1 = time()
    # nums = [[x] for x in nums]
    ans = sum3(nums)
    print('time: o ', time()-t1)
    print(ans)

